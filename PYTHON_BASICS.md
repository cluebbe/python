# Workshop: Python Basics

---

## Introduction

### Background

Python is a beginner-friendly programming language known for its clean,
readable syntax. It is widely used in data science, web development,
automation, and AI.

This workshop covers the core building blocks you need to write real Python
programs: storing data, making decisions, repeating actions, and organising
code into reusable functions.

### Setting Up the Development Environment

**1. Check that Python is installed**

```bash
python --version
```

You need Python 3.8 or higher. If it is not installed, download it from
[python.org](https://www.python.org/downloads/).

**2. Run the tutorial file**

```bash
python python_basics.py
```

No extra packages are needed — everything in this workshop is built into Python.

---

## Task 1 — Variables and Data Types

A **variable** is a named container that stores a value. Python detects the
type automatically.

| Type | Example | Description |
|---|---|---|
| `str` | `"Alice"` | Text, wrapped in quotes |
| `int` | `25` | Whole number |
| `float` | `1.68` | Number with a decimal point |
| `bool` | `True` / `False` | Logical true or false |

Create four variables — one of each type above — and print both their values
and their types using `type()`.

<details>
<summary>Solution</summary>

```python
name = "Alice"
age = 25
height = 1.68
is_student = True

print(name)
print(age)
print(height)
print(is_student)

print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_student))  # <class 'bool'>
```

**Key points:**
- You never need to declare the type — Python infers it from the value.
- `type()` is useful for debugging when you are unsure what a variable holds.
- Variable names use `snake_case` by convention: `my_variable`, not `myVariable`.

</details>

---

## Task 2 — String Formatting

**f-strings** let you embed variable values directly inside a string. Prefix
the string with `f` and wrap expressions in `{}`.

Write a line that prints: `Hello, Alice! You are 25 years old.`
using the variables from Task 1.

<details>
<summary>Solution</summary>

```python
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)
```

**Key points:**
- Any Python expression can go inside `{}` — not just variable names.
  `f"2 + 2 = {2 + 2}"` prints `2 + 2 = 4`.
- f-strings replace the older `"Hello " + name` string concatenation, which
  gets messy with multiple variables.

</details>

---

## Task 3 — User Input

`input()` pauses the program and waits for the user to type. It always returns
a **string** — convert it with `int()` or `float()` when you need a number.

Ask the user for their name and age, then print:
`In 10 years you will be X years old.`

<details>
<summary>Solution</summary>

```python
user_name = input("What is your name? ")
user_age = int(input("How old are you? "))

print(f"Nice to meet you, {user_name}!")
print(f"In 10 years you will be {user_age + 10} years old.")
```

**Key points:**
- `input()` always returns a `str`. Without `int()`, `user_age + 10` would
  crash with a `TypeError`.
- Wrap `input()` calls in a `try / except ValueError` in production code to
  handle the case where the user types text instead of a number.

</details>

---

## Task 4 — Conditionals

`if / elif / else` lets the program choose different paths based on conditions.
**Indentation** (4 spaces) defines which code belongs to each branch.

Write code that assigns a letter grade based on a `score` variable:
- 90 or above → `"A"`
- 75 or above → `"B"`
- 60 or above → `"C"`
- Below 60 → `"F"`

<details>
<summary>Solution</summary>

```python
score = 72

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: F")
```

**Key points:**
- Python checks conditions **top to bottom** and stops at the first `True`
  one. Order matters.
- `elif` is short for "else if" — it only runs if all previous conditions
  were `False`.
- Comparison operators: `==` `!=` `>` `<` `>=` `<=`
- Logical operators: `and` `or` `not`

</details>

---

## Task 5 — Lists

A **list** is an ordered collection of values in square brackets `[]`.
Items can be added, removed, and accessed by their position (index).
**Indexes start at 0.**

Create a list of three fruits. Then:
1. Print the first and last item.
2. Add a fourth fruit with `append()`.
3. Remove one fruit with `remove()`.
4. Print the final length with `len()`.

<details>
<summary>Solution</summary>

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])    # "apple"   — first item
print(fruits[-1])   # "cherry"  — last item (negative indexes count from the end)

fruits.append("mango")
print(fruits)       # ["apple", "banana", "cherry", "mango"]

fruits.remove("banana")
print(fruits)       # ["apple", "cherry", "mango"]

print(len(fruits))  # 3
```

**Key points:**
- `fruits[0]` is the first item; `fruits[-1]` is always the last — no need
  to know the length.
- `append()` adds to the end; `insert(i, value)` adds at a specific position.
- Accessing an index that does not exist raises an `IndexError`.

</details>

---

## Task 6 — Loops

A **`for` loop** repeats once for each item in a sequence.
A **`while` loop** repeats as long as a condition is `True`.

1. Use a `for` loop to print each fruit from your list prefixed with `"I like "`.
2. Use `range(5)` to print the numbers 0 through 4.
3. Use a `while` loop to count from 0 to 2.

<details>
<summary>Solution</summary>

```python
# for loop over a list
for fruit in fruits:
    print(f"I like {fruit}")

# for loop with range()
for i in range(5):       # range(5) produces 0, 1, 2, 3, 4
    print(i)

# while loop
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1           # += 1 is shorthand for count = count + 1
```

**Key points:**
- Forgetting `count += 1` in a `while` loop creates an **infinite loop** —
  use `Ctrl+C` to stop it.
- `range(start, stop, step)` — e.g. `range(0, 10, 2)` gives `0 2 4 6 8`.
- Use `break` to exit a loop early and `continue` to skip to the next
  iteration.

</details>

---

## Task 7 — Dictionaries

A **dictionary** stores **key-value pairs** in curly braces `{}`. Use the key
to look up its value — like a real dictionary where words map to definitions.

Create a dictionary with keys `"name"`, `"age"`, and `"city"`. Then:
1. Print the value of `"name"`.
2. Add a new key `"email"`.
3. Loop over all key-value pairs and print them.

<details>
<summary>Solution</summary>

```python
person = {
    "name": "Bob",
    "age": 30,
    "city": "Berlin",
}

print(person["name"])     # "Bob"

person["email"] = "bob@example.com"

for key, value in person.items():
    print(f"{key}: {value}")
```

**Key points:**
- Accessing a key that does not exist raises a `KeyError`. Use
  `person.get("phone", "N/A")` to return a default instead of crashing.
- Keys are usually strings, but can be any immutable type (int, tuple).
- `.keys()`, `.values()`, and `.items()` let you iterate over different parts
  of the dictionary.

</details>

---

## Task 8 — Functions

A **function** is a named, reusable block of code. Define it once with `def`,
then call it as many times as you need.

1. Write a function `greet(name)` that returns `"Hello, <name>!"`.
2. Write a function `add(a, b)` that returns the sum of two numbers.
3. Call each function and print the result.

<details>
<summary>Solution</summary>

```python
def greet(name):
    """Return a greeting string for the given name."""
    return f"Hello, {name}!"

def add(a, b):
    """Return the sum of a and b."""
    return a + b

print(greet("Carlos"))   # "Hello, Carlos!"
print(add(3, 5))         # 8
print(add(10, add(2, 3))) # 15 — functions can be nested
```

**Key points:**
- `return` sends a value back to the caller. Without it, the function returns
  `None`.
- The string on the first line inside a function (`"""..."""`) is a
  **docstring** — it documents what the function does.
- Parameters are local to the function — changing them inside does not affect
  variables outside.

</details>

---

## Task 9 — Putting It All Together

Write a function `describe_person(name, age, hobbies)` that:

1. Prints the person's name and age.
2. Uses a conditional to print whether they are a minor (under 18) or an adult.
3. Uses a loop to print each hobby prefixed with `"  - "`.

Then collect a name, age, and 3 hobbies from the user using `input()` and
call the function with that data.

<details>
<summary>Solution</summary>

```python
def describe_person(name, age, hobbies):
    """Print a short description of a person and their hobbies."""
    print(f"\n{name} is {age} years old.")
    if age < 18:
        print(f"{name} is a minor.")
    else:
        print(f"{name} is an adult.")
    print(f"{name}'s hobbies:")
    for hobby in hobbies:
        print(f"  - {hobby}")


user_name = input("What is your name? ")
user_age = int(input("How old are you? "))

hobbies = []
print("Enter 3 hobbies:")
for i in range(3):
    hobby = input(f"  Hobby {i + 1}: ")
    hobbies.append(hobby)

describe_person(user_name, user_age, hobbies)
```

**Key points:**
- This task combines all previous concepts: variables, f-strings, `input()`,
  conditionals, lists, loops, and functions.
- Collecting items in a loop with `append()` is a very common Python pattern.
- Defining functions that accept data as parameters (rather than reading input
  inside them) makes them reusable and easier to test.

</details>
