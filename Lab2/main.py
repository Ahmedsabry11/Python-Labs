"""
    Python Practice Tasks
    =====================

    Rules:
        - Everything must be written inside functions.
        - The file should run as a script.
        - When the script starts, the user must see a menu of numbered scenarios  (1: List order, 2: Pepole with favorite color , .....).
        - The user chooses a number, and the program runs the corresponding function.
        - Each task should only run when chosen from the menu.
        - At ANY stage: if the user enters invalid input, the program must:
              * Show an error message
              * Display what valid input looks like
              * Let the user try again (do not crash or exit)

    Tasks:
    ------

    1 - Ask the user to enter 5 numbers.
        Store them, then display them in ascending order and descending order.

    2 - Write a function that takes two numbers: (length, start).
        Generate a sequence of numbers with the given length,
        starting from the given start number and increasing by one each time.
        Print the result.

    3 - Keep asking the user for numbers until they type "done".
        When finished, print:
            * The total of all numbers entered
            * The count of valid entries
            * The average
        If the user enters something invalid, show an error and continue.
        
    4 - Ask the user to enter a list of numbers.
        Remove any duplicates, sort the result, and display it.


    6 - Ask the user to enter a sentence.
        Count how many times each word appears in the sentence
        and display the result.

    7 - Create a small gradebook system:
        - The user enters 5 students names and their scores.
        - At the end, show:
            * The highest score
            * The lowest score
            * The average score.

    8 - Write a program that simulates a shopping cart:
        - The user can add items with a name and a price.
        - The user can remove items by name.
        - The user can view all items with their prices.
        - At the end, display the total cost.

    9 - Create a number guessing game:
        - The program randomly selects a number between 1 and 20.
        - The user keeps guessing until they get it right.
        - After each guess, show if the guess was too high or too low.
        - When correct, display the number of attempts.
"""
import random

# Task 1
def print_list():
    try:
        numbers = list(map(int, input("Enter 5 numbers separated by spaces: ").split()))
        if len(numbers) != 5:
            raise ValueError("You must enter exactly 5 numbers.")
        numbers.sort()
        print("Ascending order:", numbers)
        print("Descending order:", numbers[::-1])
    except ValueError as e:
        print("Invalid input:", e)

# Task 2
def generate_sequence():    
    try:
        length = int(input("Enter the length of the sequence: "))
        start = int(input("Enter the start number: "))
        sequence = [start + i for i in range(length)]
        sequence = [i for i in range(start, start + length)]
        print("result:", sequence)
    except ValueError as e:
        print("Invalid input:", e)

# Task 3
def stats():
    total = 0
    count_valid = 0
    while True:
        entry = input("Enter a number or 'done': ")
        if entry.lower() == "done":
            break
        try:
            number = float(entry)
            total += number
            count_valid += 1
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")

    if count_valid > 0:
        average = total / count_valid
        print("Total:", total)
        print("Count valid:", count_valid)
        print("Average:", average)
    else:
        print("No valid numbers were entered.")


# Task 4
def display_unique():
    try:
        numbers = set(map(int, input("Enter a list of numbers separated by spaces: ").split()))
        numbers = list(numbers)
        numbers.sort()
        print("numbers:", numbers)
    except ValueError as e:
        print("Invalid input:", e)

# Task 6
def word_counts():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    hash = {}
    for word in words:
        hash[word] = hash.get(word, 0) + 1
    print("Word count:", hash.items())

# Task 7
def grade():
    studnets = []
    scores = []
    i = 0
    while i < 5:
        name = input(f"Enter the name of student {i+1}: ").strip()
        while not name.isalpha():
            print("Invalid name. Please enter a valid name.")
            name = input(f"Enter the name of student {i+1}: ")

        while True:
            try:
                score = float(input(f"Enter the score for {name}: "))
                scores.append(score)
                studnets.append(name)
                break
            except ValueError:
                print("Invalid score. Please enter a numeric value.")

        i += 1
    max_score = max(scores)
    min_score = min(scores)
    avg_score = sum(scores) / len(scores)

    max_students = []
    min_students = []
    for index, score in enumerate(scores):
        if score == max_score:
            max_students.append(studnets[index])
        if score == min_score:
            min_students.append(studnets[index])

    print(f"Highest score: {max_score} Scored by ", *max_students)
    print(f"Lowest score: {min_score} Scored by ", *min_students)
    print("Average score:", avg_score)

# Task 8
def cart():
    cart = {}
    while True:
        operation = input("Choose an operation: add, remove, view, total, exit: ").lower().strip()
        if operation == "add":
            name = input("Enter the item name: ")
            while True:
                try:
                    price = float(input("Enter the item price: "))
                    cart[name] = price
                    print(f"Added {name} with price {price}.")
                    break
                except ValueError:
                    print("Invalid price. Please enter a numeric value.")
        elif operation == "remove":
            name = input("Enter the item name to remove: ")
            if cart.get(name, None) is not None:
                del cart[name]
                print(f"Removed {name}.")
            else:
                print(f"{name} not found in the cart.")
        elif operation == "view":
            if cart:
                for item, price in cart.items():
                    print(f"{item}: {price}")
            else:
                print("The cart is empty.")
        elif operation == "total":
            total_cost = sum(cart.values())
            print(f"Total : {total_cost}")
        elif operation == "exit":
            break
        else:
            print("Invalid operation. on;y add, remove, view, total, or exit.")


# Task 9
def guess():
    while True:
        number = random.randint(1, 20)
        attempts = 0
        while True:
            try:
                guess = int(input("Guess a number between 1 and 20 or -1 to exit game: "))
                attempts += 1
                if guess == -1:
                    print("Exiting game.")
                    return
                elif guess < 1 or guess > 20:
                    print("Please guess a number within the range of 1 to 20.")
                elif guess < number:
                    print("Too low!")
                elif guess > number:
                    print("Too high!")
                elif guess == number:
                    print(f"Correct! The number was {number}. Attempts: {attempts}")
                    break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 20.")


def display_menu():
    print("\nMenu:")
    print("1: Display sorted and reversed")
    print("2: Generate sequence")
    print("3: Stats sum and avg")
    print("4: Remove duplicates and sort")
    print("6: Word count")
    print("7: Grade system")
    print("8: Cart")
    print("9: Guessing")
    print("0: Exit")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Choose a number (0-9): ")

        if choice == "1":
            print_list()
        elif choice == "2":
            generate_sequence()
        elif choice == "3":
            stats()
        elif choice == "4":
            display_unique()
        elif choice == "5":
            pass
        elif choice == "6":
            word_counts()
        elif choice == "7":
            grade()
        elif choice == "8":
            cart()
        elif choice == "9":
            guess()
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a number from 0 to 9.")
        
