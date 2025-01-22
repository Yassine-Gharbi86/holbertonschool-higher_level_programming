#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    y = []
    for x in my_list:
        if x % 2 == 0:
            y.append(True)
        else:
            y.append(False)
    return y
