from plates import is_valid

def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("CS50") == True

def test_start_letters():
    assert is_valid("50CS") == False
    assert is_valid("CS50") == True

def test_zero_rule():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True

def test_number_placement():
    assert is_valid("CS50P") == False
    assert is_valid("CS") == True

def test_symbols():
    assert is_valid("CS.50") == False
