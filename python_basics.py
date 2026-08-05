# Python Basics Tutorial
#
# This tutorial introduces the core building blocks of Python.
# Run this file to see the output of each section, then experiment
# by changing the values and re-running.
#
# SETUP
# -----
# No dependencies required — everything here is built into Python.
# Run with:
#   python python_basics.py

print("=" * 40)
print("  Python Basics Tutorial")
print("=" * 40)


# ---------------------------------------------------------------------------
# 1. VARIABLES AND DATA TYPES
# ---------------------------------------------------------------------------
# A variable is a named container that stores a value.
# Python figures out the type automatically — no need to declare it.

print("\n--- 1. Variables and Data Types ---")

name = "Alice"          # str  — text, always wrapped in quotes
age = 25                # int  — whole number
height = 1.68           # float — number with a decimal point
is_student = True       # bool — either True or False

print(name)             # Print the value stored in each variable
print(age)
print(height)
print(is_student)

print(type(name))       # type() reveals what kind of value a variable holds
print(type(age))
print(type(height))
print(type(is_student))


# ---------------------------------------------------------------------------
# 2. STRING FORMATTING
# ---------------------------------------------------------------------------
# f-strings let you embed variable values directly inside a string.
# Prefix the string with f and wrap variable names in curly braces {}.

print("\n--- 2. String Formatting ---")

greeting = f"Hello, {name}! You are {age} years old."  # f-string: variables are inserted at the {} placeholders
print(greeting)

print(f"{name} is {height} m tall.")  # Any variable or expression can go inside {}
print(f"2 + 2 = {2 + 2}")             # Expressions are evaluated before being inserted


# ---------------------------------------------------------------------------
# 3. USER INPUT
# ---------------------------------------------------------------------------
# input() pauses the program and waits for the user to type something.
# It always returns a string, so convert with int() or float() if needed.

print("\n--- 3. User Input ---")

user_name = input("What is your name? ")          # Read a string from the keyboard
user_age = int(input("How old are you? "))        # Convert the input string to an integer

print(f"Nice to meet you, {user_name}!")
print(f"In 10 years you will be {user_age + 10} years old.")


# ---------------------------------------------------------------------------
# 4. CONDITIONALS
# ---------------------------------------------------------------------------
# if / elif / else lets the program make decisions based on conditions.
# Indentation (4 spaces) defines which code belongs to each branch.

print("\n--- 4. Conditionals ---")

score = 72  # Change this value to test the different branches

if score >= 90:             # Condition 1 — checked first
    print("Grade: A")
elif score >= 75:           # Condition 2 — only checked if condition 1 was False
    print("Grade: B")
elif score >= 60:           # Condition 3 — only checked if conditions 1 and 2 were False
    print("Grade: C")
else:                       # Fallback — runs if none of the conditions above were True
    print("Grade: F")

# Comparison operators:  ==  !=  >  <  >=  <=
# Logical operators:     and  or  not

if score >= 60 and score < 90:  # Both conditions must be True
    print("You passed but did not get an A.")


# ---------------------------------------------------------------------------
# 5. LISTS
# ---------------------------------------------------------------------------
# A list is an ordered collection of values enclosed in square brackets [].
# Items can be of any type and can be changed after creation.

print("\n--- 5. Lists ---")

fruits = ["apple", "banana", "cherry"]  # Create a list of three strings

print(fruits)           # Print the whole list
print(fruits[0])        # Index 0 is the first item
print(fruits[1])        # Index 1 is the second item
print(fruits[-1])       # Index -1 is always the last item

fruits.append("mango")  # append() adds a new item to the end of the list
print(fruits)

fruits.remove("banana") # remove() deletes the first occurrence of a value
print(fruits)

print(len(fruits))      # len() returns the number of items in the list


# ---------------------------------------------------------------------------
# 6. LOOPS
# ---------------------------------------------------------------------------
# A for loop repeats a block of code once for each item in a sequence.
# A while loop repeats as long as a condition remains True.

print("\n--- 6. Loops ---")

# for loop — iterate over each item in the list
for fruit in fruits:                    # fruit takes on each value in the list, one at a time
    print(f"I like {fruit}")            # This line runs once per item

# for loop with range() — repeat a fixed number of times
for i in range(5):                      # range(5) produces 0, 1, 2, 3, 4
    print(f"  Step {i}")

# while loop — repeat until the condition becomes False
count = 0               # Initialise the counter before the loop
while count < 3:        # Check the condition before each iteration
    print(f"  Count is {count}")
    count += 1          # Increment the counter — forgetting this causes an infinite loop


# ---------------------------------------------------------------------------
# 7. DICTIONARIES
# ---------------------------------------------------------------------------
# A dictionary stores key-value pairs enclosed in curly braces {}.
# Use the key to look up its value — like a real dictionary with words and definitions.

print("\n--- 7. Dictionaries ---")

person = {
    "name": "Bob",      # key: "name",  value: "Bob"
    "age": 30,          # key: "age",   value: 30
    "city": "Berlin",   # key: "city",  value: "Berlin"
}

print(person["name"])   # Access a value by its key
print(person["age"])

person["email"] = "bob@example.com"  # Add a new key-value pair
print(person)

# Loop over a dictionary
for key, value in person.items():    # .items() returns each key-value pair as a tuple
    print(f"  {key}: {value}")


# ---------------------------------------------------------------------------
# 8. FUNCTIONS
# ---------------------------------------------------------------------------
# A function is a reusable block of code with a name.
# Define it once with def, then call it as many times as you need.

print("\n--- 8. Functions ---")

def greet(name):                            # def starts the definition; "name" is a parameter
    """Return a greeting string for the given name."""  # Docstring — describes what the function does
    return f"Hello, {name}!"               # return sends a value back to the caller

result = greet("Carlos")                   # Call the function and store the returned value
print(result)
print(greet("Alice"))                      # Call it again with a different argument

def add(a, b):                             # Functions can take multiple parameters
    """Return the sum of a and b."""
    return a + b

print(add(3, 5))                           # Prints 8
print(add(10, add(2, 3)))                  # Functions can be nested — inner result passed to outer


# ---------------------------------------------------------------------------
# 9. PUTTING IT ALL TOGETHER
# ---------------------------------------------------------------------------
# A small interactive program that uses all the concepts above.

print("\n--- 9. Putting It All Together ---")

def describe_person(name, age, hobbies):
    """Print a short description of a person and their hobbies."""
    print(f"\n{name} is {age} years old.")
    if age < 18:                            # Conditional inside a function
        print(f"{name} is a minor.")
    else:
        print(f"{name} is an adult.")
    print(f"{name}'s hobbies:")
    for hobby in hobbies:                   # Loop inside a function
        print(f"  - {hobby}")

hobbies = []                               # Start with an empty list
print("Enter 3 hobbies:")
for i in range(3):                         # Collect 3 hobbies from the user
    hobby = input(f"  Hobby {i + 1}: ")   # Input inside a loop
    hobbies.append(hobby)                  # Add each hobby to the list

describe_person(user_name, user_age, hobbies)  # Call the function with values collected earlier
