import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search("^[0-9]+\.[0-9]+\.[0-9]+$",ip):
        list_of_numbers=ip.split(".")
        for number in  list_of_numbers:
            if number<0 or number>255:
                return False
            return True
    else:
        return False
if __name__ == "__main__":
    main()