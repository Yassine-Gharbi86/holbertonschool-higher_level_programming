#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = set()
    for i in my_list:
        x.add(i)
    total = sum(x)
    return total
