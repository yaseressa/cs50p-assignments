from datetime import date, datetime
import sys
import inflect


def main():
    print(get_min(input("Enter your date of birth (YYYY-MM-DD): ")))


def get_min(s):
    p = inflect.engine()
    try:
        y, m, d = s.split("-")
        birth = date(int(y), int(m), int(d))
        today = date.today()
        min = round((today - birth).total_seconds() / 60)
        return p.number_to_words(min, andword="").capitalize() + " minutes"
    except ValueError:
        sys.exit("Invalid date format. Please use YYYY-MM-DD.")


if __name__ == "__main__":
    main()
