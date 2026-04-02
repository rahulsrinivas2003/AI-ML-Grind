from twttr import shorten

def main():

    test_lowercase_vowels()
    test_uppercase_vowels()
    test_mixed_case()
    test_numbers_punctuation()
    test_empty()

def test_lowercase_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("rahul") == "rhl"

def test_uppercase_vowels():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("AEIOU") == ""

def test_mixed_case():
    assert shorten("Hello") == "Hll"

def test_numbers_punctuation():
    assert shorten("rahul5903!") == "rhl5903!"

def test_empty():
    assert shorten("") == ""

if __name__ == "__main__":
    main()
