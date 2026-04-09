from um import count
import pytest

def test_count():

    assert count("hello, um, world") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_invalid():

    assert count("yummy") == 0
    assert count("123um") == 0
    assert count("....um") == 1
