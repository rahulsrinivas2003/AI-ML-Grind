import pytest
from calculator import square

def main():

    test_square()

def test_square():

    #Longer version of the test function
    # try:

    #     assert  square(2) == 4
    
    # except AssertionError:
    #     print("Test failed: square(2) should be 4")
    
    # try:

    #     assert square(3) == 9
    # except AssertionError:
    #     print("Test failed: square(3) should be 9")

    # try:
    #     assert square(4) == 16
    # except AssertionError:
    #     print("Test failed: square(4) should be 16")

    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16
    assert square(-2) == 4
    assert square(0) == 0  



def test_str():

    with pytest.raises(TypeError):
        square("hello")

if __name__ == "__main__":
    main()