"""
    lambda functions:
        - Anonymous inline functions (no name).
        - Used for short, throwaway functions.
    helper functions:
        - map(), filter() and zip()

    Syntax:
        lambda arguments: expression

    Notes:
        - Expression must be a single line.
        - Commonly used as key functions in sorting, mapping, or filtering.
"""

square = lambda x: x * x
print(square(5))


add = lambda x, y: x + y
print(add(5, 10))


my_list = [{"key": 1},
            {"key": -1},
            {"key": 5}]

my_list.sort(key=lambda my_dict: my_dict["key"])

print(my_list)


numbers = [1, 2, 3, 4, 5, 6]

#filter(boolean_function, iterable)  => keep only that return True

even_numbers = list(filter(lambda x: x % 2 == 0 , numbers))
print(even_numbers)


#map(function, iterable)
squares = list(map(lambda x: x * x, numbers))
print(squares)


#zip()

names = ["Eslam", "Ali", "Ahmed"]
grades = [10, 12]

zipped = zip(names, grades)
print(zipped)
# print(list(zipped))
print(dict(zipped))