#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    y = map(lambda x: x * number, my_list)
    b = list(y)
    return b
