import math
import re

# - write a program that prints hello world

print("Hello World!")

# - application to take a number in binary form from the user, and print it as a decimal

while True:
    binary = input("Enter a binary number: ")
    if binary == "":
        print("Invalid Binary")
        continue
    elif not binary.isnumeric():
        print("Invalid Binary")
        continue
    try:
        decimal = int(binary, 2)
        print(decimal)
        break
    except Exception as e:  
        print("Invalid Binary")

# - write a function that takes a number as an argument and if the number
#     divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
#     divisible by both return "FizzBuzz"

def fizz_buzz():
    while True:
        try:
            num = int(input("Enter a number: ").strip())
            break
        except Exception as e:
            print("Enter Valid Number")
    
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")

fizz_buzz()


# - Ask the user to enter the radius of a circle print its calculated area and circumference

def circle ():
    while True:
        try:
            radius = int(input("Enter the radius of the circle: ").strip())
            break
        except:
            print("Enter Valid radius number")
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius

    print(f"Area {area}, Circumference {circumference}")

circle()

# - Ask the user for his name then confirm that he has entered his name (not an empty string/integers). 
# then proceed to ask him for his email and print all this data


def get_data():
    while True:
        name = input("Enter your name: ").strip()
        if name == "":
            print("Invalid")
        elif name.isdigit():
            print("Invalid")
        else:
            break

    while True:
        email = input("Enter your email: ").strip()
        if re.match("[a-zA-Z0-9]+@[a-zA-Z0-9]+",email) is None:
            print("Enter Valid Email")
        else:
            break

    print(f"Name: {name}, Email: {email}")

get_data()

# - Write a program that prints the number of times the substring 'iti' occurs in a string
string = input("Enter string: ").strip()
count = string.count("iti")
print(f"Count of iit = {count}")