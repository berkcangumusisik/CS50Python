from numb3rs import validate


def test_ipranges():
    assert validate("255.255.255.255") == True
    assert validate("192.168.1.1") == True
    assert validate("192.168.1.255") == True
    assert validate("0.0.0.0") == True
    assert validate("192.168.1") == False
    assert validate("192.168.1.256") == False
    assert validate("192.168.1.255.1") == False
    assert validate("512.512.512.512") == False
    assert validate("512.512.512.512.512") == False
    assert validate("cat") == False