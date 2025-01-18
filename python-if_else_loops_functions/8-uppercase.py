#!/usr/bin/python3
def uppercase(str):
    x = ""
    for char in str:
        if ord(char) in range(97, 123):
            x += chr(ord(char) - 32)
        else:
            x += char
    print(x)
