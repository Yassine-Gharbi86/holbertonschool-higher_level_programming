#!/usr/bin/python3
def search_replace(my_list, search, replace):
    x = []
    for i in my_list:
        if i == search:
            x.append(replace)
        else:
            x.append(i)
    return x
