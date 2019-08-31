from math import floor, log
import itertools


class GeoHash4:
    b4_bits = {"00": "a", "01": "b", "10": "c", "11": "d"}
    invert = {"a": [0, 0], "b": [0, 1], "c": [1, 0], "d": [1, 1]}

    def __init(self):
        pass

    def get_bits(self, value, min, max, num_bits):
        if num_bits == 0:
            return ""
        mid = (max + min) / 2
        if value < mid:
            return "0{}".format(self.get_bits(value, min, mid, num_bits - 1))
        else:
            return "1{}".format(self.get_bits(value, mid, max, num_bits - 1))

    def merge_bits(self, lng_bits, lat_bits):
        merged_bits = []
        for i in range(0, len(lng_bits)):
            two_bits = lat_bits[i] + lng_bits[i]
            merged_bits.append(self.b4_bits[two_bits])
        return "".join(merged_bits)

    def encode(self, lon, lat, precision=24):
        longitude = self.get_bits(lon, -180, 180, precision)
        latitude = self.get_bits(lat, -180, 180, precision)
        return self.merge_bits(longitude, latitude)

    def decode(self, geohash):
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
