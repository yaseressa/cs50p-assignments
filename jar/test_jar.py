from jar import Jar


def test_init():
    assert Jar(5).capacity == 5

jar = Jar()
def test_str():
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_withdraw():
    jar.withdraw(11)
    assert str(jar) == "🍪"

def test_dep():
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"
