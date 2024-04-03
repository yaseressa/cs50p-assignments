import validators
def main():
    print(validate(input('Enter Email: ').strip().lower()))


def validate(s):
    if validators.email(s):
        return('Valid')
    return 'Invalid'


if __name__ == "__main__":
    main()
