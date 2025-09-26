"""
Task 6) Random Data Generator
   - Ask user how many random numbers to generate.
   - Save them into "random_numbers.csv" as:
        index,value
        1, 42
        2, 87
        ...
   - Print total count and average of the generated numbers.
"""
import random

def generator():
    try:
        count = int(input("How many random numbers to generate? "))
        if count <= 0:
            print("Enter positive integer.")
            return

        numbers = [random.randint(1, 100) for i in range(count)]
        print("Generated numbers:", numbers)
        
        with open("random_numbers.csv", "w") as file:
            file.write("index,value\n")
            for index, value in enumerate(numbers, start=1):
                file.write(f"{index},{value}\n")

        average = sum(numbers) / count
        print(f"Count {count}, Average {average}")
    except ValueError:
        print("Invalid input, enter a numeric value.")
    except Exception as e:
        print(f"An error occurred: {e}")
