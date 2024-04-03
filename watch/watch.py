import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r'^(.|\s)+src="https?://(www.)?youtube\.com/embed/(\w+)".*$', s, re.IGNORECASE):
        if match.group(3):
            return f'https://youtu.be/{match.group(3)}'
        else:
            return None


if __name__ == "__main__":
    main()
