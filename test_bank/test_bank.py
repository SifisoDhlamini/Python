from bank import value

def test_hello():
    assert value("hello zibanibani!") == 0

def test_h():
    assert value("hi sorenso!") == 20


def test_other():
    assert value("Sanibonani Bonkhosi!") == 100


def test_space():
    assert value(" ") == 100


def test_null():
    assert value("") == 100


def test_digits():
    assert value("12345") == 100


def test_caps():
    assert value("HELLO ZIpencepence") == 0

