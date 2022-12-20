#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    n = max(len(my_list_1), len(my_list_2))

    #if n > len(my_list_1) or n > len(my_list_2):
    #    raise IndexError

    try:
        for i in range(n):

            #if n > len(my_list_1) or n > len(my_list_2):
            #    raise IndexError
            result.append(my_list_1[i] / my_list_2[i])
        return list(result)

    except TypeError:
        print("wrong type")

    except IndexError:
        print("out of range")

    except ZeroDivisionError:
        print("division by 0")

    finally:
        return list(result)
