import pytest
from numb3rs import validate

def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("192.257.3.60") == False
    assert validate("257.168.3.60") == False
    assert validate("cat") == False
    assert validate("192..6..") == False
