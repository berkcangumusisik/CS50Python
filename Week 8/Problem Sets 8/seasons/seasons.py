import sys
import inflect
p = inflect.engine()
from datetime import date, datetime


def main():
    birthdate = input("Date of Birth: ")
    validDate = date_validate(birthdate)
    days_difference = calc_difference(validDate)
    output = add_text(days_difference)
    print(output)

def date_validate(birthdate):
    try:
        input = date.fromisoformat(birthdate)
        return input
    except ValueError:
        sys.exit("Invalid date")


def calc_difference(days):
    today = date.today()
    daysDiff = today - days
    daysDiff.days * 24 * 60
    return daysDiff.days * 24 * 60

def add_text(text):
    text = p.number_to_words(text, andword="")
    return text.capitalize() + " minutes"

if __name__ == "__main__":
    main()