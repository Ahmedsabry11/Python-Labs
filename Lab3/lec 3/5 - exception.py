"""
    Errors in Python:

        1 - Syntax Errors:
            - Detected by the interpreter before the program runs
            - Example: missing colon, misspelled keyword

        2 - Runtime Errors (Exceptions):
            - Happen while the program is running
            - Defensive programming: handle possible failures
            - Structure:
                try:
                    # Code that might raise an error
                except:
                    # Code to handle the error
                else:
                    # Code that runs if no error occurred
                finally:
                    # Code that always runs (cleanup, DB close)

        3 - Logical Errors:
            - Program runs but produces incorrect results
            - Example:
                import math
                print(math.floor(10.5))   # → 10
                print(math.floor(-10.5))  # → -11
"""

# ---------------- Example 1: simple try-except ----------------
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"{result=}")
except ZeroDivisionError:
    print("division by zero not allowed")
except ValueError:
    print("please enter valid int")
except Exception as e:
    print("un expected error: ", e)
else:
    print("Division successfully !")
finally:
    print("finally block executed")


