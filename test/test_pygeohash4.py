from lib.pygeohash4 import GeoHash4

HASHER = GeoHash4()
COORDS = {"lon": -77.03651183831396, "lat": 38.89773309824841}


def test_init():
    """hasher initializes accurately"""
    assert HASHER.b4_bits == {"00": "a", "01": "b", "10": "c", "11": "d"}
    assert HASHER.invert == {"a": [0, 0], "b": [0, 1], "c": [1, 0], "d": [1, 1]}


def test_get_bits():
    """Tests the GeoHash4.get_bits method"""
    value = COORDS["lon"]
    min = -180
    max = 180
    assert HASHER.get_bits(value, min, max, 24) == "010010010011011111101110"
    assert HASHER.get_bits(value, min, max, 12) == "010010010011"
    value = COORDS["lat"]
    min = -90
    max = 90
    assert HASHER.get_bits(value, min, max, 24) == "101101110101001000111011"
    assert HASHER.get_bits(value, min, max, 12) == "101101110101"


def test_merge_bits():
    """Tests the GeoHash4.merge_bits method"""
    assert HASHER.merge_bits("00", "10") == "ca"
    assert HASHER.merge_bits("001010", "101101") == "cadcbc"


def test_encode():
    """Tests the GeoHash4.encode method"""
    lon = COORDS["lon"]
    lat = COORDS["lat"]
    assert HASHER.encode(lon, lat, 12) == "cbacdacdcadb"
    assert HASHER.encode(lon, lat, 6) == "cbacda"


def test_decode():
    """Tests the GeoHash4.decode method"""
    assert HASHER.decode("cbacdacdcadb") == {
        "longitude": -77.0361328125,
        "latitude": 19.44580078125,
        "latitude_margin": 0.02197265625,
        "longitude_margin": 0.0439453125,
    }
    assert HASHER.decode("cbacda") == {
        "longitude": -75.9375,
        "latitude": 18.28125,
        "latitude_margin": 1.40625,
        "longitude_margin": 2.8125,
    }
