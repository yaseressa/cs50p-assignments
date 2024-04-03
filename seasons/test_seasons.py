from seasons import get_min
import pytest

def test_seasons():
    assert get_min("1991-01-01") == "Seventeen million, three hundred seventeen thousand, four hundred forty minutes"
    with pytest.raises(SystemExit):
        get_min("January, 1 1999")
    with pytest.raises(SystemExit):
        get_min("hello")
    with pytest.raises(SystemExit):
        get_min("787+97")
