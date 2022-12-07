#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []
    [new_list.append(x) for x in my_list if x not in new_list]
    Sum = 0
    
    for i in range(len(new_list)):
        Sum += new_list[i]

    return (Sum)
