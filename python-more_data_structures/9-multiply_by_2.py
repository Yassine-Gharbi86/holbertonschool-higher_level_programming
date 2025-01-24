#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    x = dict()
    for i in a_dictionary:
        x[i] = a_dictionary[i] * 2
    return x
