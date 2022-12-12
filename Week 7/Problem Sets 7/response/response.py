import validators


def main():
    print(validate(input("What's your email address? ").strip()))


def validate(address):
    if validators.email(address):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()