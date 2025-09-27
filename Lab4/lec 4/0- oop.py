"""
    Object Oriented Programming:

    What is OOP:
    - Paradigm: think about data and objects instead of just logic and functions.
    - Each object has:
        1. Attributes (data)
        2. Actions (methods)

    why use oop:
        1 - re-usability: inheritance
        2 - modularity: you can insert an object inside an object, living in another object.
        3 - easy to think about, easy to reason with, easy to wrap your head around.
        4 - mimics real life objects: just like a normal human being does.


    Building blocks of oop:
                    Class, Object

        class:
            blueprint to create the object, its data, and its methods.

            class attributes:
                    public knowledge, general knowledgccese through all object
                    
            class methods:
                    public usage for the entire class, usually returns objects of the class, access class-level data 
            
        object:
            an instance of the class
            
            - Instance attributes: 
                    specific to each object
                    
            - Instance methods: 
                    access object-specific data
                        



        static methods:
            public usage for everything, no reference needed to object/class needed
            logically related to the class

        

            object methods and attributes:
                    special to that specific object

        Special Methods (dunder methods):
            - __init__ : constructor
            - __str__ : string representation
            - __repr__ : debugging representation

"""
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_age(self):
        return self.age
    
    def eat_food(self):
        print(f"hello i'm {self.name} and i'm {self.age} and i'm eating")


# Creating a person object
human = Person("Ahmed", 24)
print(human.name)
print(human.age)
print(human.get_age())
human.eat_food()

print("Circle")

class Circle:
    pi = 3.14    #class attribute
    
    def __init__(self, radius):
        self.radius = radius       # instance attribute
    
    def get_area(self):
        return Circle.pi * (self.radius ** 2)
    
    def __str__(self):
        return f"A circle with radius {self.radius}"
    
    def __repr__(self):
        return f"Circle(radius={self.radius})"
    
    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)
    
    


circle1 = Circle(5)
print(circle1.get_area())
print(circle1)               # calls __str__
print(repr(circle1))         # calls __repr__


circle2 = Circle.from_diameter(40)   #using classmethod
print(circle2.get_area())
print(circle2)




class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    
    @staticmethod
    def draw_axes():
        print("Drawing vertical axis: ")
        for i in range(10, 0, -1):
            print(i)
        
        print("Drawing horizontal axis: ")
        for i in range(10):
            print(i, end=" ")
            


my_point = Point(2, 3)

Point.draw_axes()




