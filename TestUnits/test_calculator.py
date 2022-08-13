import pytest
from calculator import square, get_x

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("cat")

def test_wrongInput():
    with pytest.raises(ValueError):
        get_x() == "Scifi"

def test_getX():
    with pytest.raises(ValueError):
        get_x() == 3
