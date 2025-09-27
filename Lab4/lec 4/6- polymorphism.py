"""
Polymorphism in Python
----------------------

Definition:
    - "Poly" = many, "morph" = forms → Many forms / many faces.
    - A concept where a single interface (same name) can be applied to different types.

Types of Polymorphism:
    1. Method Overloading:
        - Python does NOT support traditional overloading (like Java, C++).
        - Achieved using default arguments, *args, **kwargs.

    2. Method Overriding (via Inheritance):
        - Subclass redefines a method from its superclass.

    3. Operator Overloading:
        - Redefining operators like +, -, *, / using dunder methods:
            __add__, __iadd__, __sub__, __mul__, __lt__, __gt__, etc.

    4. Duck Typing:
        - "If it walks like a duck, and quacks like a duck, it's probably a duck."
        - Python focuses on what an object *can do*, not its type.
        - Example: functions that expect any object with a `quack()` method.
"""
# Built-in polymorphism

sum = 3 + 5    # int + int

my_str = "Eslam" + "Reda"   # str + str

lst = [1, 2, 3] + [4, 5, 6]  #list + list


# Operator Overloading

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Point(self.x + other.x , self.y + other.y)
    
    def __iadd__(self, other):   # in place add    x+=1
        self.x += other.x
        self.y += other.y
        return self
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

point1 = Point(1, 1)
point2 = Point(3, 4)

# print(point1)
# print(point2)

new_point = point1 + point2
print(new_point)

point1 += Point(5, 5)
print(point1)


# Duck Typing

class Duck:
    def quack(self):
        print("Quack")

class Person:
    def quack(self):
        print("I can imitat duck!")

class Lion:
    def speak():
        print("I'm a king")

def make_quack(thing):
    thing.quack()

duck = Duck()
person = Person()
lion = Lion()

make_quack(duck)
make_quack(person)
make_quack(lion)