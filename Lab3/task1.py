"""
Tasks 1) Math Automation
   - Create a file called "math_report.txt".
   - Ask the user for multiple numbers (comma-separated).
   - For each number, calculate:
        - floor, ceil, square root, area of a circle
   - Write the results into "math_report.txt".
   - Confirm file was created and print its content.
"""
import math

def math_report():
    try:
        numbers_str = input("Enter multiple numbers (comma-separated): ")
        numbers = [float(num.strip()) for num in numbers_str.split(",")]

        with open("math_report.txt", "w") as file:
            for number in numbers:
                floor_val = math.floor(number)
                ceil_val = math.ceil(number)
                sqrt_val = math.sqrt(number) if number >= 0 else "-1"
                area_circle = math.pi * (number ** 2) if number >= 0 else "-1"
                file.write(f"{number}, {floor_val}, {ceil_val}, {sqrt_val}, {area_circle}\n")
        
        print("math_report.txt created successfully")
        
        with open("math_report.txt", "r") as file:
            print("result: \n", file.read())
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
    except Exception as e:
        print(f"An error occurred: {e}")