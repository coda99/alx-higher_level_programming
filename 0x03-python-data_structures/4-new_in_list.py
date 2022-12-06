#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    if(idx < 0):
        return my_list

    if (idx > len(my_list)):
        return my_list
    
    copied_list = list(my_list)
    copied_list[idx] = element
    return (copied_list)
