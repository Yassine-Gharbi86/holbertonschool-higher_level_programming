#!/usr/bin/python3
for x in range(122, 96, -1):
    print("{}".format(chr(x - 32) if x % 2 == 1 else chr(x)), end="")
