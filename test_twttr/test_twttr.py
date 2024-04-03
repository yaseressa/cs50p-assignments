from twttr import shorten

def test_default():
    assert shorten('') == ''
def test_with_vowels():
    assert shorten('Twitter') == 'Twttr'
def test_with_nums():
    assert shorten('Twitter1') == 'Twttr1'
def test_with_puncs():
    assert shorten('Twitter!') == 'Twttr!'
def test_with_cap_vowels():
    assert shorten('TwIttEr') == 'Twttr'
def test_without_vowels():
    assert shorten('Dry') == 'Dry'
