"""
Multiple Inheritance & Method Resolution Order (MRO)
---------------------------------------------------

Syntax:
    class C(A, B):
        pass

MRO:
    - The order in which Python resolves methods/attributes.
    - Depth-first, from left to right.
    - Use <Class>.__mro__ to inspect it. (method-resolution-order)

# ---------------- Reference ----------------
# Great read: http://python-history.blogspot.com/2010/06/method-resolution-order.html
"""

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class Athlete:
    def __init__(self, sport):
        self.sport = sport

class StudentAthlete(Student, Athlete):
    def __init__(self, name, grade, sport):
        Student.__init__(self, name, grade)
        Athlete.__init__(self, sport)

person = StudentAthlete("Eslam", 100, "football")
print(person.name, person.grade, person.sport)


class A:
    def say_hello(self):
        print("This is A")


class B:
    def say_hello(self):
        print("This is B")


class C(A, B):
    pass


obj = C()
obj.say_hello()
print(C.__mro__)


class A:
    pass

class B:
    pass

class C(A, B):
    pass

class D(C, B):
    pass


obj_d = D()
print(D.__mro__)



