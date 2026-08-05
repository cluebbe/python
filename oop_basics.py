# Object-Oriented Programming (OOP) Basics in Python
#
# This tutorial introduces classes, objects, methods, and inheritance —
# the four pillars that make up object-oriented programming in Python.
#
# SETUP
# -----
# No dependencies required — everything here is built into Python.
# Run with:
#   python oop_basics.py

print("=" * 40)
print("  OOP Basics Tutorial")
print("=" * 40)


# ---------------------------------------------------------------------------
# 1. CLASSES AND OBJECTS
# ---------------------------------------------------------------------------
# A class is a blueprint for creating objects.
# An object is a specific instance created from that blueprint.

print("\n--- 1. Classes and Objects ---")

class Dog:                          # Define a class with the "class" keyword; name uses PascalCase
    species = "Canis familiaris"    # Class attribute — shared by ALL instances of Dog

dog1 = Dog()                        # Create an object (instance) from the class
dog2 = Dog()                        # Create a second, independent object

print(dog1)                         # Prints something like <__main__.Dog object at 0x...>
print(dog1.species)                 # Access the class attribute via the instance
print(dog2.species)                 # Both instances share the same class attribute
print(Dog.species)                  # Can also access it directly on the class


# ---------------------------------------------------------------------------
# 2. THE __init__ METHOD AND INSTANCE ATTRIBUTES
# ---------------------------------------------------------------------------
# __init__ is the constructor — it runs automatically when a new object is created.
# "self" refers to the specific object being created; it must be the first parameter.
# Instance attributes are unique to each object.

print("\n--- 2. __init__ and Instance Attributes ---")

class Dog:                                  # Redefine the class with an __init__ method
    species = "Canis familiaris"            # Class attribute — same for all dogs

    def __init__(self, name, age):          # Constructor: called automatically on Dog(...)
        self.name = name                    # Instance attribute — unique to this object
        self.age = age                      # Instance attribute — unique to this object

dog1 = Dog("Rex", 3)                        # Python calls __init__(dog1, "Rex", 3)
dog2 = Dog("Bella", 5)                      # A second, separate object with different values

print(dog1.name)                            # "Rex"
print(dog2.name)                            # "Bella" — each object has its own name
print(dog1.age)                             # 3
print(dog1.species)                         # "Canis familiaris" — class attribute, same for both


# ---------------------------------------------------------------------------
# 3. INSTANCE METHODS
# ---------------------------------------------------------------------------
# A method is a function defined inside a class.
# Every instance method receives "self" as its first argument — Python passes
# it automatically so the method knows which object it is operating on.

print("\n--- 3. Instance Methods ---")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):                                 # Method with only self — no extra arguments needed
        print(f"{self.name} says: Woof!")           # self.name accesses this object's name

    def describe(self):                             # Another method on the same object
        print(f"{self.name} is {self.age} years old.")

    def birthday(self):                             # Method that modifies an instance attribute
        self.age += 1                               # Increment this object's age by 1
        print(f"Happy birthday {self.name}! Now {self.age}.")

dog1 = Dog("Rex", 3)
dog1.bark()                                         # Call the method on dog1
dog1.describe()
dog1.birthday()                                     # Modifies dog1.age
dog1.describe()                                     # Age is now 4


# ---------------------------------------------------------------------------
# 4. THE __str__ METHOD
# ---------------------------------------------------------------------------
# __str__ controls what is printed when you use print() on an object.
# Without it, print() shows a cryptic memory address.

print("\n--- 4. The __str__ Method ---")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):                              # Called automatically by print() and str()
        return f"Dog(name={self.name}, age={self.age})"  # Return a readable string representation

    def bark(self):
        print(f"{self.name} says: Woof!")

dog1 = Dog("Rex", 3)
print(dog1)                                         # Now prints: Dog(name=Rex, age=3)


# ---------------------------------------------------------------------------
# 5. INHERITANCE
# ---------------------------------------------------------------------------
# Inheritance lets a new class (child) reuse all attributes and methods
# from an existing class (parent), then add or change what it needs.
# The child class passes the parent in parentheses: class Child(Parent)

print("\n--- 5. Inheritance ---")

class Animal:                                       # Parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"{self.name} is {self.age} years old.")

    def speak(self):                                # Generic method — children will override this
        print(f"{self.name} makes a sound.")

class Dog(Animal):                                  # Dog inherits from Animal
    def speak(self):                                # Override the parent's speak() with a dog-specific version
        print(f"{self.name} says: Woof!")

class Cat(Animal):                                  # Cat also inherits from Animal
    def speak(self):                                # Override with a cat-specific version
        print(f"{self.name} says: Meow!")

dog = Dog("Rex", 3)
cat = Cat("Whiskers", 5)

dog.describe()                                      # Inherited from Animal — no need to redefine it
cat.describe()                                      # Same inherited method
dog.speak()                                         # Dog's own version
cat.speak()                                         # Cat's own version


# ---------------------------------------------------------------------------
# 6. super() — EXTENDING THE PARENT
# ---------------------------------------------------------------------------
# super() calls a method from the parent class.
# Use it in __init__ to run the parent's setup before adding child-specific attributes.

print("\n--- 6. super() ---")

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"{self.name} is {self.age} years old.")

class Dog(Animal):
    def __init__(self, name, age, breed):           # Dog needs an extra "breed" attribute
        super().__init__(name, age)                 # Run Animal's __init__ first to set name and age
        self.breed = breed                          # Then add the dog-specific attribute

    def __str__(self):
        return f"Dog(name={self.name}, breed={self.breed}, age={self.age})"

    def speak(self):
        print(f"{self.name} says: Woof!")

dog = Dog("Rex", 3, "Labrador")
print(dog)                                          # Dog(name=Rex, breed=Labrador, age=3)
dog.describe()                                      # Inherited from Animal
dog.speak()


# ---------------------------------------------------------------------------
# 7. PUTTING IT ALL TOGETHER
# ---------------------------------------------------------------------------
# A small library system using everything covered above.

print("\n--- 7. Putting It All Together ---")

class Book:                                         # Parent class
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_checked_out = False                 # All books start as available

    def __str__(self):
        status = "checked out" if self.is_checked_out else "available"  # Inline conditional expression
        return f'"{self.title}" by {self.author} ({self.pages} pages) [{status}]'

    def checkout(self):                             # Method that changes the object's state
        if self.is_checked_out:                     # Guard against checking out an already-taken book
            print(f'"{self.title}" is already checked out.')
        else:
            self.is_checked_out = True
            print(f'"{self.title}" checked out successfully.')

    def return_book(self):                          # Method to return the book
        self.is_checked_out = False
        print(f'"{self.title}" returned.')

class Ebook(Book):                                  # Ebook inherits from Book
    def __init__(self, title, author, pages, file_size_mb):
        super().__init__(title, author, pages)      # Reuse Book's __init__
        self.file_size_mb = file_size_mb            # Ebook-specific attribute

    def __str__(self):
        base = super().__str__()                    # Reuse Book's __str__ output
        return f"{base} [eBook, {self.file_size_mb} MB]"  # Append the extra info

book1 = Book("The Pragmatic Programmer", "Hunt & Thomas", 352)
book2 = Ebook("Clean Code", "Robert Martin", 464, 4.2)

print(book1)
print(book2)

book1.checkout()
book1.checkout()                                    # Try checking it out again — shows the guard message
book1.return_book()
print(book1)
