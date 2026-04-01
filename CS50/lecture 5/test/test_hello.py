from hello import hello

def test_hello():

    assert hello() == "hello, world"
    assert hello("Alice") == "hello, Alice"
    assert hello("Bob") == "hello, Bob"

    for name in ["Alice", "Bob", "Charlie"]:
        assert hello(name) == f"hello, {name}" 

def test_default():

    assert hello() == "hello, world"

    