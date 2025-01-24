#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    x = sorted(a_dictionary.keys())
    for i in x:
        y = a_dictionary[i]
        print("{}: {}".format(i, y))
