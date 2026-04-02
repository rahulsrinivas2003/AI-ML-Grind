from bank import value

def main():

    test_hello()
    test_h()
    test_else()

def test_hello():

    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
def test_h():

    assert value("hey") == 20
    assert value("How are you") == 20
def test_else():

    assert value("What's up") == 100
    assert value("Goodbye") == 100




if __name__ == "__main__":

    main()
