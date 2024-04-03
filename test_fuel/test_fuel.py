from fuel import convert, gauge
from pytest import raises

def test_zero_div():
    with raises(ZeroDivisionError):
        convert('8 / 0')
def test_greater_div():
    with raises(ValueError):
        convert('8 / 2')
def test_E():
    assert gauge(convert('1 / 100')) == 'E'
def test_F():
    assert gauge(convert('99 / 100')) == 'F'
def test_b():
    assert gauge(convert('55 / 100')) == '55%'
