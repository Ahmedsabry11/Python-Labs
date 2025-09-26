"""
Tasks 2) Regex Log Cleaner
        - Create a file called "access.log" with 10 fake log lines
            (mix valid emails and invalid strings).
        - Use regex to extract all valid emails.
        - Save them into "valid_emails.txt".
        - Print how many unique emails were found.
"""
import re

def regex_log_cleaner():
    with open("access.log", "r") as log_file:
        log_content = log_file.readlines()

        # comment regex match emails with domain extensions
        # email_regex = r'\b[a-zA-Z0-9_]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
        # assume valid email is username@domain (no domain extension required)
        email_regex = r'\b[a-zA-Z0-9_]+@[a-zA-Z0-9.-]+\b'

        valid_emails = []
        valid_unique_emails = set()
        for line in log_content:
            matches = re.findall(email_regex, line)
            print(f"line: {line.strip()},  matches: {matches}")
            valid_emails.extend(matches)
            valid_unique_emails.update(matches)
        
        with open("valid_emails.txt", "w") as email_file:
            for email in valid_emails:
                email_file.write(email + "\n")

        with open("valid_unique_emails.txt", "w") as unique_email_file:
            for email in valid_unique_emails:
                unique_email_file.write(email + "\n")

        print(f"Total valid emails found: {len(valid_emails)}")
        print(f"Total unique valid emails: {len(valid_unique_emails)}")

