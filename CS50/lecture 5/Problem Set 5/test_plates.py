from plates import is_valid


def test_valid_cases():
    assert is_valid("CS50") == True
    assert is_valid("AB123") == True
    assert is_valid("HELLO") == True


def test_invalid_start():
    assert is_valid("50") == False      
    assert is_valid("1ABC") == False
    assert is_valid("A1BC") == False


def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_number_rules():
    assert is_valid("AB012") == False
    assert is_valid("ABC1D") == False


def test_special_characters():
    assert is_valid("AB@12") == False
    assert is_valid("AB 12") == False
