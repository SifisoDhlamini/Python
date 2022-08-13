from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)
    with pytest.raises(ValueError):
        jar = Jar(0)
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(3)
    assert jar2.capacity == 3


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.deposit(6)
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(2)
    assert jar.size == 5


def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(3)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(5)
    jar.withdraw(1)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)
