#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    set_3 = [set(set_1), set(set_2)]

    return (set.difference(*set_3))
