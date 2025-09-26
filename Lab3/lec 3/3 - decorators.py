"""
    functions are first-class citizens in Python:
        1 - They can be used as parameters
        2 - They can be saved inside variables
        3 - They can be returned from functions

    decorators:
        - Functions that take functions as input and return functions
        - Used to enhance or modify the behavior of functions
        - The basis for class methods, static methods, and frameworks like Flask/Django
"""

def exponent_creator(power):
    def exponent(number):
        return number ** power
    return exponent

exponent_of_3 = exponent_creator(3)

print(exponent_of_3(2))


def fun():
    print("Hello, ITI")

def beautify(function):
    def wrapper():
        print("*" * 40)
        function()
        print("*" * 40)
    return wrapper

final = beautify(fun)
final()




@beautify
def say_hello():
    print("Hello Every one")

say_hello()


import time


def timer(function):
    def wrapper(x, y):
        start = time.time()
        result = function(x, y)
        end = time.time()
        print(f"result is: {result}, in time: {end - start}")
    return wrapper


@timer
def fun(x, y):
    return x + y

fun(5, 6)
