#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        l = []
        i = 0
        c = x

        #for j in my_list:
        #    c+=1
        while i < x:
            if isinstance(my_list[i], int):
                #if x > c:
                #    x = c
                #l.append(my_list[i])
                print(my_list[i], end="")
            i += 1
        

        print()
        return x

    except:
        pass
