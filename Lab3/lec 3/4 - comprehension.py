"""
    List, Set, Dict Comprehensions:

        - Shorter and more readable way to create collections
        - Syntax:   [expression for item in iterable if condition]
                    {expression for item in iterable if condition}
                    {key: value for key, value in iterable}

    Advantages:
        - More concise than for-loops
        - Can include conditions
        - Works with list, set, and dict
"""

my_list = [i for i in range(1_000_001)]

my_new_list = [i for i in range(1_000_001) if not i % 2 ]

print(my_new_list[0:100])

my_set = {i for i in range(100)}
print(my_set)



names = ["Eslam", "Ali", "Ahmed"]

my_dict = {index: value for index, value in enumerate(names)}
print(my_dict)
