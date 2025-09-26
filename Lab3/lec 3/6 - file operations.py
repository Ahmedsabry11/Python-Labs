"""
    File Operations in Python:

    Modes:
        - "w"  : write (overwrite if file exists)  (Creates a file if it does not exist.)
        - "a"  : append (write at the end of file) (Creates a file if it does not exist.)
        - "r"  : read (default mode)
        - "rb" : read in binary mode
        - "wb" : write in binary mode   (Creates a file if it does not exist.)
        - "ab" : append in binary mode  (Creates a file if it does not exist.)

    Tips:
        - Always use context managers ("with") when possible
        - A file handler is like a cursor → points to where you are in the file
        - Methods:
            - close()      : Closes the file. Always call after finishing work (or use "with" to auto-close).
            - write()      : Writes a string (or bytes in binary mode) to the file.
            - read()       : Reads the entire file content as a single string (or up to n characters if specified).
            - readlines()  : Reads the entire file and returns a list where each element is a line.
            - seek()       : Moves the file cursor to a given position (0 = start of file, etc.).
"""
file = open("iti.txt", "w")
file.write("Hello from, python course\n")
file.close

file = open("iti.txt", "a")
file.write("Hello from, python Day 3\n")
file.close



file = open("iti.txt", "r")
text = file.read()
print(text)


file = open("iti.txt", "r")
text = file.readlines()
print(text)

file = open("iti.txt", "r")
file.seek(10)
text = file.read()
print(text)
file.close()

def copy_fun(old_file, new_file):
    _file = open(old_file, "rb")
    _bytes = _file.read()
    _file.close()
    
    _file = open(new_file, "wb")
    _file.write(_bytes)
    _file.close()

copy_fun("image.jpg", "copied_image.jpg")


#context manger

with open("iti.txt", "r") as file:
    text = file.read()
    print(text)


try:
    with open("file.txt", "rb") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("binary file not found!")
