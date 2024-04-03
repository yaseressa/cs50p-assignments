from plates import is_valid

def test_right():
    assert is_valid('CS50') == True
def test_wrong():
    assert is_valid('CS05') == False
def test_punc():
    assert is_valid('CS50!') == False
def test_alpha():
    assert is_valid('CSjfuid') == False
def test_num():
    assert is_valid('12313') == False
def test_else():
    assert is_valid('AAA22A') == False

