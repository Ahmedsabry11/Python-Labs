"""
Encapsulation in Python
-----------------------

In other languages (Java, C#, C++), we have keywords:
    - public
    - private
    - protected

In Python:
    - Privacy is not enforced by the interpreter.
    - It's only by convention, since "we are all grown-ups".
    - Conventions apply to both attributes and methods.

Conventions:
    - Protected:   _single_leading_underscore
    - Private:     __double_leading_underscore
                   → This is name mangling, not true privacy.
                   → Helps avoid name collisions in inheritance.
                   → Python renames it internally to: _ClassName__attribute

Programmers follow convention using:
    - Getters (accessors)
    - Setters (mutators)

Tips:
    - Use @property decorator for clean getters/setters.
    - Or use property() function directly.
"""

class Phone:
    def __init__(self, model, storage):
        self.__model = model      #private attribute
        self.__storage = storage
        
    def set_model(self, model):
        self.__model = model
    
    def get_model(self):
        return self.__model
    
    
    def set_storage(self, storage):
        self.__storage = storage
    
    def get_storage(self):
        return self.__storage



my_phone = Phone("s24", 512)

print(my_phone.get_model())
print(my_phone.get_storage())
my_phone.set_model("iphone 17")
print(my_phone.get_model())

# print(my_phone._Phone__model)
# print(my_phone._model)



#--------------------------------------------------------------------
class Phone:
    def __init__(self, model, storage):
        self.__model = model      #private attribute
        self.__storage = storage
        
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, model):
        self.__model = model
    
    @property
    def storage(self):
        return self.__storage
    @storage.setter
    def storage(self, storage):
        self.__storage = storage

my_phone = Phone("s24", 512)
print(my_phone.model)
print(my_phone.storage)

my_phone.storage = 1024
print(my_phone.storage)
#------------------------------------------------------
print("------------------------------------------")
class Phone:
    def __init__(self, model, storage):
        self.__model = model      #private attribute
        self.__storage = storage
        
    def set_model(self, model):
        self.__model = model
    
    def get_model(self):
        return self.__model
    
    model = property(get_model, set_model)
    
    
    def set_storage(self, storage):
        self.__storage = storage
    
    def get_storage(self):
        return self.__storage
    
    storage = property(get_storage, set_storage)

my_phone = Phone("S25", 1024)
print(my_phone.model)
print(my_phone.storage)

my_phone.model = "iphone 17"
print(my_phone.model)



