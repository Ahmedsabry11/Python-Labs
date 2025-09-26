"""
Task 3) Datetime Reminder Script
   - Ask user for a date (YYYY-MM-DD).
   - Calculate how many days remain until that date.
   - If it is in the past, print "This date has already passed."
   - Otherwise, save the reminder into "reminders.txt" in format:
        "{date} -> {days_left} days left"
   - Append multiple reminders without overwriting.
"""

from datetime import datetime

def reminder():
    while True:
            
        try:
            date = input("Enter a date (YYYY-MM-DD) or -1 to exit: ")
            if date == "-1":
                return
            correct_date = datetime.strptime(date, "%Y-%m-%d").date()
            today = datetime.today().date()
            days_left = (correct_date - today).days

            if days_left < 0:
                print("This date has already passed.")
            else:
                with open("reminders.txt", "a") as reminder_file:
                    reminder_file.write(f"{correct_date} -> {days_left} days left\n")
                print(f"Reminder set for {correct_date}.")
            
            print("reminders.txt content:")
            try:
                with open("reminders.txt", "r") as reminder_file:
                    print(reminder_file.read())
            except FileNotFoundError:
                print("No reminders set yet.")

        except Exception as e:
            print(f"An error occurred: {e}")

