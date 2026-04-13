from datetime import date
import sys
import inflect


def main():
    dob = input("Date of Birth: ")

    try:
        birth_date = date.fromisoformat(dob)
    except ValueError:
        sys.exit("Invalid date")

    if birth_date > date.today():
        sys.exit("Invalid date")

    print(minutes_to_words(birth_date))


def minutes_to_words(birth_date):
    today = date.today()
    delta = today - birth_date
    minutes = delta.days * 24 * 60

    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")

    return words.capitalize() + " minutes"


if __name__ == "__main__":
    main()
