from um import count

def test_count():
    assert count('um') == 1
def test_match():
    assert count('Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?') == 2
def test_yum():
    assert count('UM') == 1
