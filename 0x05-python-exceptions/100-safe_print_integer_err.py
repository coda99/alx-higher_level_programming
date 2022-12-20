#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print(int(value))
        return value
    except Exception as e:
        print("Exception: Unknown format code 'd' for object of type 'str'")
    except ValueError:
        return False

