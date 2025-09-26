"""
    Python Standard Library and Regex

    Paradigms:
        - syntax: ease of usage / quality of life
        - standard library: strength of built-in modules

    Most commonly used standard library packages:
        - math
        - re
        - datetime
        - os
        - random
        - sys
        - typing

    Regex basics:
        ^ : start of the string
        $ : end of the string
        + : one or more
        * : zero or more
        ? : zero or one time

    Useful tool: https://regex101.com/
"""
import os
import math
from datetime import datetime, date, timedelta
import re

print(os.getcwd())

print(math.ceil(10.6))
print(math.pi)


print(datetime.now())
print(date.today())
print(date.today() + timedelta(days=7))


name = "Kareem"
print(bool(re.search("ee", name)))
print(bool(re.match("Kar", name)))
print(bool(re.fullmatch("Kar", name)))
