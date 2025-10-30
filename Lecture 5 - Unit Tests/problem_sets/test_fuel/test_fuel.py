import pytest
from fuel import convert, gauge


def test_convert_basic():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("99/100") == 99

def test_convert_rounding():
    assert convert("1/3") == 33
    assert convert("2/3") == 67

def test_convert_invalid_values():
    with pytest.raises(ValueError):
        convert("5/2")

    with pytest.raises(ValueError):
        convert("a/b")

    with pytest.raises(ValueError):
        convert("3/")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"

def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_middle():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
