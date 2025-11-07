from working import convert
import pytest


def test_basic_times():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test_with_minutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:05 AM") == "22:30 to 08:05"


def test_invalid_inputs():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")  
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")  
