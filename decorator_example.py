#!/usr/bin/env python


def wrap(func):
    def wrapped_func(*args):
        print("Enter")
        result = func(*args)
        print(result)
        print("Exit")
        return result

    return wrapped_func


@wrap
def add(a, b):
    return a + b


@wrap
def mull(a, b):
    return a * b


# add = wrap(add) - The equal to @wrap ; def add(a, b):
# mul = wrap(mul) - The equal to @wrap ; def mul(a, b):


a, b = 3, 5

add(a, b)
mull(a, b)
