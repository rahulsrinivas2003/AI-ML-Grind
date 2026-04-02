
from fuel import convert, gauge
import pytest


def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25


def test_convert_edge():
    assert convert("0/1") == 0
    assert convert("1/1") == 100


def test_convert_invalid_value():
    with pytest.raises(ValueError):
        convert("3/2")

    with pytest.raises(ValueError):
        convert("a/b")

    with pytest.raises(ValueError):
        convert("-1/2")


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")



def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_middle():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
