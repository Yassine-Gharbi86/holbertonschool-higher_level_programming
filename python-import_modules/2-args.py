#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count_args = len(argv) - 1
    if count_args == 0:
        print("0 arguments.")
    elif count_args == 1:
        print("1 argument:")
    else:
        print(f"{count_args} arguments:")
    for x in range(1, len(argv)):
        print("{}: {}".format(x, argv[x]))
