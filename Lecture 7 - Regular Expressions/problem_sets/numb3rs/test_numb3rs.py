from numb3rs import validate

def test_valid_ips():
    assert validate("0.0.0.0") == True
    assert validate("127.0.0.1") == True
    assert validate("192.168.1.1") == True

def test_invalid_ips_out_of_range():
    assert validate("256.0.0.1") == False
    assert validate("1.2.3.1000") == False

def test_invalid_ips_leading_zeros():
    assert validate("192.168.01.1") == False
    assert validate("010.0.0.1") == False
    assert validate("001.002.003.004") == False

def test_invalid_format():
    assert validate("127.0.0") == False       
    assert validate("127.0.0.1.5") == False   
    assert validate("abc.def.ghi.jkl") == False
    assert validate("...") == False
    assert validate("") == False
    assert validate("123") == False