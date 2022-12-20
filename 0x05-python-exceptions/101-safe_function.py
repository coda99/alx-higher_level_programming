#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        return (fct(*args)) 
    except IndexError:
        print("Exception: list index out of range")
    except ZeroDivisionError:
        print("Exception: division by zero")

