import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    if not re.search( r"^\d+\.\d+\.\d+\.\d+$", ip):
        return False
    else:

        parts = ip.split(".")

        for part in parts:

            if len(part) > 1 and part[0] == "0":
                return False
            
            if  0 <=int(part)<=255:

                continue
            else:

                return False
        return True

if __name__ == "__main__":
    main()
