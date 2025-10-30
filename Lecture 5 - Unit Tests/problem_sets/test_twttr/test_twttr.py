from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("HELLO WORLD") == "HLL WRLD"

def test_mixedcase():
    assert shorten("CS50 is THE BEST Course") == "CS50 s TH BST Crs"

def test_punctuation():
    assert shorten("What's up?") == "Wht's p?"

def test_numbers():
    assert shorten("1234") == "1234"

def test_empty():
    assert shorten("") == ""
