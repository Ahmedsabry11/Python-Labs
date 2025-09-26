"""
    generators:
        - Special functions that return an iterator
        - They can pause execution and resume later
        - They are defined using the 'yield' keyword

    Notes:
        - Generators don’t store all values in memory at once.
        - Much more memory efficient than lists for large sequences.
        - lazy evaluation (generate data only when needed)
        - Base for async/await and co-routines in Python.
"""

def one_to_three():
    yield 1
    yield 2
    yield 3


# for element in one_to_three():
#     print(element)

# use next()
"""
gen = one_to_three()
print(next(gen))
print(next(gen))
print(next(gen))
"""



def my_range(start, end=None, step=1):
    if end is None:
        end = start
        start = 0
    
    while start < end:
        yield start
        start += step

for element in my_range(1, 10, 2):
    print(element)

#memory efficiency
import sys

#list vs gen

my_list = [i for i in range(1_000_000)]
my_iterator = my_range(1_000_000)

print("list size", sys.getsizeof(my_list))
print("gen size", sys.getsizeof(my_iterator))


print(type(my_iterator))


