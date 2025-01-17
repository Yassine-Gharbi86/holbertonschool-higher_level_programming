#!/usr/bin/python3
def print_alphabet(x):
    if x <= 122:
        print(chr(x), end="")
        print_alphabet(x + 1)
print_alphabet(97)