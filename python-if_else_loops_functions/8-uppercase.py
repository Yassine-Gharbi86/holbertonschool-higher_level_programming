#!/usr/bin/python3
def uppercase(str):
    x =""
    for char in str:
        if ord(char) in range(97, 123):
            y=chr(ord(char) - 32)
            x = x + y
        else:
            x = x + char
    print(x)
  