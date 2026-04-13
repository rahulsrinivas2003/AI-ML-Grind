from seasons import minutes_to_words
from datetime import date, timedelta


def test_same_day():
    today = date.today()
    assert minutes_to_words(today) == "Zero minutes"


def test_one_day():
    today = date.today()
    yesterday = today - timedelta(days=1)
    assert minutes_to_words(yesterday) == "One thousand four hundred forty minutes"


def test_format():
    birth = date(2000, 1, 1)
    result = minutes_to_words(birth)
    assert isinstance(result, str)
    assert result.endswith("minutes")
