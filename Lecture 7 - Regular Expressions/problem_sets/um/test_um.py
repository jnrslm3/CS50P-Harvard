from um import count

def test_single_um():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1

def test_punctuation():
    assert count("um?") == 1

def test_inside_words():
    assert count("yummy") == 0
    assert count("album") == 0

def test_multiple():
    assert count("um um um") == 3

