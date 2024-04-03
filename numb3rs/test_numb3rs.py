from numb3rs import validate


def test_valid():
    assert validate('127.0.0.1') == True
def test_first():
    assert validate('127.875.0.0') == False
def test_invalid():
    assert validate('257.0.0.1') == False
