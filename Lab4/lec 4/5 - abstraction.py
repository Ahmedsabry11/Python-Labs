"""
Abstraction in Python
---------------------

Definition:
    - Hiding implementation details and focusing on specifications (what should be done).
    - Forces subclasses to implement certain methods.

In Python:
    - We don't have "interfaces" like in Java or C#.
    - Instead, we use Abstract Base Classes (ABC).
    - Supports multiple inheritance.

Key:
    - Abstract classes cannot be instantiated.
    - Subclasses must implement all abstract methods, otherwise they are also abstract.
"""


from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def say_hello(self):
        pass

class Car(ABC):
    @abstractmethod
    def start_engin(self):
        pass

class SuperHero(Person, Car):
    def say_hello(self):
        print("Hello, I'm Super Hero")
    
    def start_engin(self):
        print("engien started .....")

obj = SuperHero()
obj.say_hello()
obj.start_engin()



class FileOprations(ABC):
    @abstractmethod
    def open(self):
        pass
    
    @abstractmethod
    def write(self):
        pass


class AwsS3(FileOprations):
    def open(self):
        print("Open AWS S3.......")
    
    def write(self):
        print("Write data in AWS S3")




class GoogleCloud(FileOprations):
    def open(self):
        print("Open GoogleCloud file.......")
    
    def write(self):
        print("Write data in GoogleCloud file")



aws = AwsS3()
aws.open()
aws.write()

gcloud = GoogleCloud()
gcloud.open()
gcloud.write()
