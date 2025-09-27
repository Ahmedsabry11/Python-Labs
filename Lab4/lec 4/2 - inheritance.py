"""
======================================================
                Inheritance in OOP
======================================================

- Don't repeat yourself (DRY).
- Relationship: a subclass IS A superclass.
- Method overriding: customize logic for subclass.
- isinstance(object, class) → check if object belongs to a class (or subclass).
- issubclass(subclass, superclass) → check if a class inherits from another.

Note:
    INHERITANCE IS A ONE-WAY ROAD.    super => sup
"""

class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
    
    def say_hello(self):
        return f"Hello, my name is {self.name} and i work as {self.occupation}"
    
    def say_age(self):
        return self.age


class SuperHero(Person):
    def __init__(self, name, age, occupation, superhero_name, nemesis):
        super().__init__(name, age, occupation)
        self.superhero_name = superhero_name
        self.nemesis = nemesis
    
    def say_you_superhero(self):
        return f"i'm a superhero: {self.superhero_name}"
    
    #overriding method
    def say_hello(self):
        return f"Hello, i'm {self.name} and my nemesis is {self.nemesis}"
    
    def fly(self):
        return "i'm on sky"
    

Ezz = SuperHero("Ezz", 22, "SW", "Batman", "Fares")

print(Ezz.say_hello())

print(Ezz.say_age())

print(Ezz.fly())

Eslam = Person("Eslam", 24, "SW")
print(Eslam.say_hello())





# Multi level inheritance
class A:
    def say_hello_from_a(self):
        print("This is A")


class B(A):
    def say_hello_from_b(self):
        print("This is B")


class C(B):
    def say_hello_from_c(self):
        print("This is C")
        


class D(C):
    def say_hello_from_d(self):
        print("This is D")

obj_d = D()
obj_d.say_hello_from_a()
obj_d.say_hello_from_b()
obj_d.say_hello_from_c()
obj_d.say_hello_from_d()
print(issubclass(D, A))
print(isinstance(obj_d, A))

obj_a = A()
obj_a.say_hello_from_a()
