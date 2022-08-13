from plates import is_valid

def test_too_long():
    assert is_valid("AAA22AA") == False

def test_alpha_after_num():
    assert is_valid("AAA22A") == False

def test_start_with_num():
    assert is_valid("2AA22A") == False

def test_start_with_one_alpha():
    assert is_valid("A22") == False


def test_too_short():
    assert is_valid("A") == False

def test_Acceptable():
    assert is_valid("AAA222") == True
    assert is_valid("AA") == True

def test_space():
    assert is_valid(" ") == False

def test_null():
    assert is_valid("") == False

def test_first_num_zero():
    assert is_valid("AA021") == False

def test_illegal_charracters():
    assert is_valid("AA22#") == False
    assert is_valid("AA*22") == False
    assert is_valid("_AA22") == False





