from seasons import DOB, convert_min
import pytest

def test_DOB():
    with pytest.raises(SystemExit):
        DOB("cat")
    with pytest.raises(SystemExit):
        DOB("2023-01-01")
    with pytest.raises(SystemExit):
        DOB("2020/01/01")
    with pytest.raises(SystemExit):
        DOB("January 1, 2000")
    with pytest.raises(SystemExit):
        DOB("")
    with pytest.raises(SystemExit):
        DOB("2020/20/01")
    with pytest.raises(SystemExit):
        DOB("cat")
    with pytest.raises(SystemExit):
        DOB("2020/12/51")




