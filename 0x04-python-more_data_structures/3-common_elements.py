#!/usr/bin/python3

def common_elements(set_1, set_2):
    set_3 = [set(set_1), set(set_2)]

    return (set.intersection(*set_3))
