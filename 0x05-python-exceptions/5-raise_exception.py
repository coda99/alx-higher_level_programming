#!/usr/bin/python3

def raise_exception():
    try:
        raise Exception("Exception raised")
    except Exception as e:
        print(e)
