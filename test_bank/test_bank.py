from bank import value

def test_incorrect():
    assert value('sup') == 100
def test_case():
    assert value('HELLO') == 0
def test_entire():
    assert value('hello, newman') == 0
