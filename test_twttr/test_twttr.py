from twttr import shorten

def test_shorten():
    assert shorten("Sifiso") == "Sfs"
    assert shorten("12345") == "12345"
    assert shorten("AEIOUaeiou") == ""
    assert shorten("a123fguimn67") == "123fgmn67"
    assert shorten("..Lucolo..") == "..Lcl.."
