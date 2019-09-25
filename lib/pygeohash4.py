"""A python implmentation of https://github.com/rangle/geohash4."""


class GeoHash4:
    """Convert a value to bits."""

    def __init__(self):
        """Initializes the GeoHash4 class."""
        self.b4_bits = {"00": "a", "01": "b", "10": "c", "11": "d"}
        self.invert = {"a": [0, 0], "b": [0, 1], "c": [1, 0], "d": [1, 1]}

    def get_bits(self, value, min, max, num_bits):
        """Convert a value to bits.

        Args:
            self (GeoHash4): this class.
            value (float): the value to convert to bits.
            min (int): the minimum possible value. -180 for longitude, -90 for latitude.
            max (int): the maximum possible value. 180 for longitude, 90 for latitude.
            num_bits (int): the number of bits to return

        Returns:
            string: value converted to bits.

        """
        if num_bits == 0:
            return ""
        mid = (max + min) / 2
        if value < mid:
            return "0{}".format(self.get_bits(value, min, mid, num_bits - 1))
        else:
            return "1{}".format(self.get_bits(value, mid, max, num_bits - 1))

    def merge_bits(self, lng_bits, lat_bits):
        """Merge longitude and latitude bits.

        Args:
            self (GeoHash4): this class.
            lng_bits (str): bits from the longitude.
            lat_bits (str): bits from the latitude.

        Returns:
            string: merged bits

        """
        merged_bits = []
        for i in range(0, len(lng_bits)):
            two_bits = lat_bits[i] + lng_bits[i]
            merged_bits.append(self.b4_bits[two_bits])
        return "".join(merged_bits)

    def encode(self, lon, lat, precision=24):
        """Encode a given set of coordinates to a given precision.

        Args:
            self (GeoHash4): this class.
            lon (float): longitude.
            lat (float): latitude.

        Returns:
            string: geohashed coordinates.

        """
        longitude = self.get_bits(lon, -180, 180, precision)
        latitude = self.get_bits(lat, -90, 90, precision)
        return self.merge_bits(longitude, latitude)

    def decode(self, geohash):
        """Decode a given set of coordinates.

        Args:
            self (GeoHash4): this class.
            geohash (str): geohashed coordinates.

        Returns:
            dict: decoded coordinates with a margin of error.

        """
        lat = -90
        lon = -180
        cur_size = 90
        for i in range(0, len(geohash)):
            bits = self.invert[geohash[i]]
            lat += cur_size * bits[0]
            lon += 2 * cur_size * bits[1]
            cur_size = cur_size / 2

        return {
            "longitude": lon + cur_size * 2,
            "longitude_margin": cur_size * 2,
            "latitude": lat + cur_size,
            "latitude_margin": cur_size,
        }
