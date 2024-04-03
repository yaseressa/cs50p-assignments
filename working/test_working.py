import pytest
from working import convert

def test_convert_valid_input():
    assert convert("9:00 AM to 2:30 PM") == "09:00 to 14:30"
def test_omit():
    with pytest.raises(ValueError):
        assert convert("9:00 AM 2:30 PM")
def test_out():
    with pytest.raises(ValueError):
        assert convert("9:70 AM to 2:70 PM")
