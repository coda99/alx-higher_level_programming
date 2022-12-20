#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        i, c = 0, 0

        for j in my_list:
            c+=1
        while i < x:
            if x > c:
                x = c
            print(my_list[i], end="")
            i += 1
        
        print()
        return x

    except:
        print("You hit the except block")
