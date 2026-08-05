# Workshop: Object-Oriented Programming in Python

---

## Introduction

### Background

**Object-oriented programming (OOP)** is a way of organising code around
*objects* — bundles that combine related data and behaviour in one place.

Instead of writing loose variables and functions, you define a **class** (a
blueprint) and create as many **objects** (instances) from it as you need.
Each object keeps its own data but shares the same behaviour defined in the
class.

OOP becomes valuable as programs grow: it keeps related code together, avoids
repetition through inheritance, and makes large codebases easier to understand
and maintain.

**The four core concepts covered in this workshop:**

| Concept | What it means |
|---|---|
| **Class** | A blueprint that defines attributes and methods |
| **Object** | A specific instance created from a class |
| **Inheritance** | A child class reuses and extends a parent class |
| **Encapsulation** | Keeping data and the code that uses it together |

### Setting Up the Development Environment

No packages required. Run with:

```bash
python oop_basics.py
```

---

## Task 1 — Creating a Class and an Object

Define a class called `Dog` with a **class attribute** `species` set to
`"Canis familiaris"`. Create two instances and print the `species` attribute
from each.

A **class attribute** is shared by all instances of the class.

<details>
<summary>Solution</summary>

```python
class Dog:
    species = "Canis familiaris"

dog1 = Dog()
dog2 = Dog()

print(dog1.species)   # "Canis familiaris"
print(dog2.species)   # "Canis familiaris"
print(Dog.species)    # Can also access directly on the class
```

**Key points:**
- Class names use **PascalCase** (`Dog`, `MyClass`) by convention.
- A class attribute is defined directly in the class body, outside any method.
- All instances share the same class attribute — changing `Dog.species` would
  update it for every instance at once.

</details>

---

## Task 2 — `__init__` and Instance Attributes

Add an `__init__` method to `Dog` that accepts `name` and `age` and stores
them as **instance attributes**. Create two dogs with different names and ages
and print their attributes.

`__init__` is the **constructor** — Python calls it automatically every time
you create a new object. `self` refers to the object being created.

<details>
<summary>Solution</summary>

```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Rex", 3)
dog2 = Dog("Bella", 5)

print(dog1.name)   # "Rex"
print(dog2.name)   # "Bella"
print(dog1.age)    # 3
```

**Key points:**
- `self` must be the first parameter of every method — Python passes it
  automatically and uses it to know which object you are working with.
- **Instance attributes** (`self.name`) are unique to each object. Changing
  `dog1.name` does not affect `dog2.name`.
- `__init__` never uses `return` — its job is only to set up the object.

</details>

---

## Task 3 — Instance Methods

Add three methods to `Dog`:
1. `bark()` — prints `"<name> says: Woof!"`
2. `describe()` — prints `"<name> is <age> years old."`
3. `birthday()` — increments `age` by 1 and prints a birthday message.

<details>
<summary>Solution</summary>

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof!")

    def describe(self):
        print(f"{self.name} is {self.age} years old.")

    def birthday(self):
        self.age += 1
        print(f"Happy birthday {self.name}! Now {self.age}.")

dog = Dog("Rex", 3)
dog.bark()        # Rex says: Woof!
dog.describe()    # Rex is 3 years old.
dog.birthday()    # Happy birthday Rex! Now 4.
dog.describe()    # Rex is 4 years old.
```

**Key points:**
- Every instance method receives `self` as its first parameter. You never
  pass it yourself — Python injects it automatically when you call
  `dog.bark()`.
- Methods can read *and* modify instance attributes via `self`.
- `self.age += 1` modifies only *this* object's age — other Dog instances
  are not affected.

</details>

---

## Task 4 — The `__str__` Method

Without `__str__`, printing a Dog object shows a cryptic memory address like
`<__main__.Dog object at 0x10f3b2a90>`.

Add a `__str__` method to `Dog` that returns:
`"Dog(name=Rex, age=3)"` — substituting the actual values.

<details>
<summary>Solution</summary>

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Dog(name={self.name}, age={self.age})"

dog = Dog("Rex", 3)
print(dog)   # Dog(name=Rex, age=3)
```

**Key points:**
- `__str__` is called automatically by `print()` and `str()`.
- Methods with double underscores on both sides (`__init__`, `__str__`) are
  called **dunder methods** (short for "double underscore"). Python calls them
  automatically in specific situations.
- `__str__` must always `return` a string — never `print()` inside it.

</details>

---

## Task 5 — Inheritance

Create a parent class `Animal` with `__init__(name, age)`, a `describe()`
method, and a generic `speak()` method.

Then create two child classes:
- `Dog(Animal)` — overrides `speak()` to print `"<name> says: Woof!"`
- `Cat(Animal)` — overrides `speak()` to print `"<name> says: Meow!"`

Both children should inherit `describe()` without redefining it.

<details>
<summary>Solution</summary>

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"{self.name} is {self.age} years old.")

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")

dog = Dog("Rex", 3)
cat = Cat("Whiskers", 5)

dog.describe()   # Inherited from Animal
cat.describe()   # Inherited from Animal
dog.speak()      # Dog's own version
cat.speak()      # Cat's own version
```

**Key points:**
- Write the parent class in parentheses: `class Dog(Animal)`.
- A child class automatically has all attributes and methods of the parent.
- **Overriding** means defining a method in the child with the same name as
  the parent — the child's version takes priority.

</details>

---

## Task 6 — `super()`

`super()` calls a method from the parent class. It is most commonly used in
`__init__` to run the parent's setup before adding child-specific attributes.

Extend `Dog` to also accept a `breed` argument. Use `super().__init__()` to
handle `name` and `age`, then store `breed` separately.

<details>
<summary>Solution</summary>

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"{self.name} is {self.age} years old.")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)   # Run Animal's __init__ to set name and age
        self.breed = breed            # Then add the dog-specific attribute

    def __str__(self):
        return f"Dog(name={self.name}, breed={self.breed}, age={self.age})"

    def speak(self):
        print(f"{self.name} says: Woof!")

dog = Dog("Rex", 3, "Labrador")
print(dog)       # Dog(name=Rex, breed=Labrador, age=3)
dog.describe()   # Rex is 3 years old.
dog.speak()      # Rex says: Woof!
```

**Key points:**
- Without `super().__init__()`, `self.name` and `self.age` would never be
  set, and calling `describe()` would crash with an `AttributeError`.
- `super()` can also be used to call any parent method, not just `__init__`.
- `super().__str__()` in a child class reuses the parent's string and lets
  you append extra information without duplicating code.

</details>

---

## Task 7 — Putting It All Together

Build a small library system:

1. Create a `Book` class with attributes `title`, `author`, `pages`, and
   `is_checked_out` (starts as `False`). Add:
   - `__str__` showing title, author, pages, and availability status.
   - `checkout()` — sets `is_checked_out = True`, but prints a warning if
     the book is already checked out.
   - `return_book()` — sets `is_checked_out = False`.

2. Create an `Ebook(Book)` child class with an extra `file_size_mb` attribute.
   Override `__str__` to append `[eBook, X MB]` to the parent's string.

<details>
<summary>Solution</summary>

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_checked_out = False

    def __str__(self):
        status = "checked out" if self.is_checked_out else "available"
        return f'"{self.title}" by {self.author} ({self.pages} pages) [{status}]'

    def checkout(self):
        if self.is_checked_out:
            print(f'"{self.title}" is already checked out.')
        else:
            self.is_checked_out = True
            print(f'"{self.title}" checked out successfully.')

    def return_book(self):
        self.is_checked_out = False
        print(f'"{self.title}" returned.')


class Ebook(Book):
    def __init__(self, title, author, pages, file_size_mb):
        super().__init__(title, author, pages)
        self.file_size_mb = file_size_mb

    def __str__(self):
        base = super().__str__()
        return f"{base} [eBook, {self.file_size_mb} MB]"


book = Book("The Pragmatic Programmer", "Hunt & Thomas", 352)
ebook = Ebook("Clean Code", "Robert Martin", 464, 4.2)

print(book)
print(ebook)

book.checkout()
book.checkout()    # Already checked out — shows warning
book.return_book()
print(book)
```

**Key points:**
- `status = "checked out" if self.is_checked_out else "available"` is an
  **inline conditional expression** (ternary operator) — a concise one-line
  `if/else` for assigning a value.
- `super().__str__()` in `Ebook` reuses `Book`'s string rather than
  duplicating it — if `Book.__str__` changes, `Ebook` automatically benefits.
- Setting `is_checked_out = False` in `__init__` is an example of
  **encapsulation** — the object manages its own state, and callers interact
  with it only through `checkout()` and `return_book()`.

</details>
