"""
    Modules and __name__ attribute:

        - Modules are files containing Python code (functions, classes, variables)
        - You can import them into other Python scripts

    Important attributes:
        __name__:
            - Stores the name of the module
            - If the module is run directly: __name__ == "__main__"

    Notes:
        - Organize imports: standard library first, third-party next, internal imports last
        - Use if __name__ == "__main__": to allow scripts to be run or imported without executing main code
"""

# Standard library imports
import os
from datetime import datetime

# Third-party imports
# import numpy as np

# Internal imports
from iti.welcom import say_welcom
from hello import say_hello


def main():
    say_hello()
    say_welcom()

print("Hello from main")


if __name__ == "__main__":
    main()
