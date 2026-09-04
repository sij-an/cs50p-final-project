from project import (
    convert_length,
    convert_temperature,
    convert_mass,
    convert_area,
    convert_volume,
    convert_speed,
    convert_time
)


def test_convert_length():
    assert convert_length(1, "km", "m") == 1000
    assert convert_length(100, "cm", "m") == 1
    assert convert_length(1, "m", "cm") == 100


def test_convert_temperature():
    assert convert_temperature(0, "C", "F") == 32
    assert convert_temperature(100, "C", "F") == 212
    assert convert_temperature(0, "C", "K") == 273.15
    assert convert_temperature(32, "F", "C") == 0


def test_convert_mass():
    assert convert_mass(1, "kg", "g") == 1000
    assert convert_mass(1000, "g", "kg") == 1
    assert round(convert_mass(1, "lb", "kg"), 5) == 0.45359


def test_convert_area():
    assert convert_area(1, "m2", "cm2") == 10000
    assert convert_area(10000, "cm2", "m2") == 1
    assert convert_area(1, "km2", "m2") == 1000000


def test_convert_volume():
    assert convert_volume(1, "l", "ml") == 1000
    assert convert_volume(1000, "ml", "l") == 1
    assert convert_volume(1, "m3", "l") == 1000


def test_convert_speed():
    assert convert_speed(36, "kph", "mps") == 10
    assert round(convert_speed(1, "mph", "kph"), 5) == 1.60934


def test_convert_time():
    assert convert_time(1, "hour", "minute") == 60
    assert convert_time(1, "day", "hour") == 24
    assert convert_time(1, "week", "day") == 7

