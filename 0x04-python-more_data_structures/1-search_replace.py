#!/usr/bin/python3

def search_replace(my_list, search, replace):
    copied = list(my_list)
    for i in range(len(copied)):
        if (copied[i] == search):
            copied[i] = replace

    return (copied)
