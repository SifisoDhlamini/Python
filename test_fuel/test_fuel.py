import pytest
from fuel import gauge, convert

def test_correct():
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("2/3") == 67


def test_valError():
    with pytest.raises(ValueError):
      convert("three/four")
    with pytest.raises(ValueError):
        convert("1.5/4")
    with pytest.raises(ValueError):
        convert("3/5.5")
    with pytest.raises(ValueError):
       convert("5-10")
    with pytest.raises(ValueError):
        convert("4/2")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")

def test_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"


def test_percent():
    assert gauge(75) == "75%"
    assert gauge(25) == "25%"





