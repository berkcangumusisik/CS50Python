import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    try:
        address = ip.split(".", maxsplit=3)
        for iprange in address:
            if int(iprange) > 255 or len(address) < 4:
                return False

    except ValueError:
        return False

    else:
        return True


if __name__ == "__main__":
    main()