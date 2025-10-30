from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("hello nurik") == 0
    assert value("Hello") == 0

def test_h_letter():
    assert value("How it's going?") == 20
    assert value("How are you?") == 20

def test_else():
    assert value("Good morning!") == 100
    assert value("Welcome") == 100
    assert value("123hi") == 100