# List Tricks Tutorial
#
# This tutorial shows short, readable ways to work with lists in Python.
# Run this file to see the output of each section, then experiment
# by changing the values and re-running.
#
# SETUP
# -----
# No dependencies required — everything here is built into Python.
# Run with:
#   python list_tricks.py

print("=" * 40)
print("  List Tricks Tutorial")
print("=" * 40)


# ---------------------------------------------------------------------------
# 1. INDEXING AND NEGATIVE INDEXES
# ---------------------------------------------------------------------------
# Every item has a position (index), and counting starts at 0.
# Negative indexes count from the end: -1 is the last item.

print("\n--- 1. Indexing and Negative Indexes ---")

numbers = [10, 20, 30, 40, 50, 60]

print(f"{numbers[0]=}")     # First item — f"{x=}" prints the code and its value
print(f"{numbers[-1]=}")    # Last item
print(f"{numbers[3]=}")     # 40, counted from the start
print(f"{numbers[-3]=}")    # 40, counted from the end


# ---------------------------------------------------------------------------
# 2. SLICING
# ---------------------------------------------------------------------------
# list[start:stop] returns a piece of the list.
# start is included, stop is not. Either can be left out.

print("\n--- 2. Slicing ---")

print(f"{numbers[1:4]=}")   # Positions 1, 2, 3 — stop (4) is not included
print(f"{numbers[:3]=}")    # The first 3 items
print(f"{numbers[-3:]=}")   # The last 3 items
print(f"{numbers[:-2]=}")   # Everything except the last 2
print(f"{numbers[1:-1]=}")  # Everything except the first and the last
print(f"{numbers[2:100]=}") # Slicing never crashes — it stops at the end


# ---------------------------------------------------------------------------
# 3. SLICING WITH A STEP
# ---------------------------------------------------------------------------
# list[start:stop:step] takes every step-th item.
# A negative step walks backwards, so [::-1] reverses.

print("\n--- 3. Slicing with a Step ---")

print(f"{numbers[::2]=}")   # Even positions
print(f"{numbers[1::2]=}")  # Odd positions
print(f"{numbers[::-1]=}")  # Reversed

word = "level"
print(f"{word[::-1]=}")             # Works on strings too
print(f"{word == word[::-1]=}")     # Palindrome check


# ---------------------------------------------------------------------------
# 4. UNPACKING
# ---------------------------------------------------------------------------
# Pull the values of a list into variables in one line.
# A *star variable collects "the rest"; _ marks values you don't need.

print("\n--- 4. Unpacking ---")

x, y = [3, 7]                       # Number of variables must match
print(f"{x=} {y=}")

a, b = "left", "right"
a, b = b, a                         # Swap without a temporary variable
print(f"{a=} {b=}")

first, *middle, last = numbers      # middle becomes a list
print(f"{first=} {middle=} {last=}")

gold, silver, *_ = [95, 88, 72, 65, 50]  # Keep the first two, ignore the rest
print(f"{gold=} {silver=}")


# ---------------------------------------------------------------------------
# 5. LIST COMPREHENSIONS
# ---------------------------------------------------------------------------
# [expression for item in list if condition] builds a new list in one line.
# if at the end filters; if/else at the front chooses a value.

print("\n--- 5. List Comprehensions ---")

words = ["apple", "Banana", "cherry", "Date"]

doubled = [n * 2 for n in numbers]                  # Transform every item
big = [n for n in numbers if n > 30]                # Keep only some items
first_letters = [w[0] for w in words]               # Indexing inside a comprehension
labels = ["big" if n > 30 else "small" for n in numbers]  # Choose between two values

print(f"{doubled=}")
print(f"{big=}")
print(f"{first_letters=}")
print(f"{labels=}")


# ---------------------------------------------------------------------------
# 6. ENUMERATE AND ZIP
# ---------------------------------------------------------------------------
# enumerate() gives position and item together.
# zip() walks through several lists side by side.

print("\n--- 6. enumerate and zip ---")

for rank, w in enumerate(words, start=1):   # Count from 1 instead of 0
    print(f"{rank}. {w}")

cities = ["Berlin", "Paris", "Rome"]
countries = ["Germany", "France", "Italy"]

for city, country in zip(cities, countries):  # Pairs come in the order the lists are passed
    print(f"{city} is in {country}")

country_by_city = dict(zip(cities, countries))  # Two lists → dictionary
print(f"{country_by_city=}")

temps = [12, 15, 14, 18, 21]
changes = [b - a for a, b in zip(temps, temps[1:])]  # Each item paired with the next
print(f"{changes=}")


# ---------------------------------------------------------------------------
# 7. USEFUL BUILT-INS
# ---------------------------------------------------------------------------
# sum, min, max, len, sorted, any, all — no loop needed.

print("\n--- 7. Useful Built-ins ---")

scores = [50, 65, 72, 88, 95]

print(f"{sum(scores)=} {min(scores)=} {max(scores)=} {len(scores)=}")
print(f"{sorted(scores, reverse=True)=}")    # A new list — scores is unchanged
print(f"{sorted(words, key=str.lower)=}")    # Sort ignoring upper/lower case
print(f"{max(words, key=len)=}")             # The longest word
print(f"{any(s > 90 for s in scores)=}")     # At least one above 90?
print(f"{all(s >= 50 for s in scores)=}")    # Everyone 50 or more?
print(f"{sum(1 for s in scores if s >= 70)=}")  # Count matches
print(f"{[3, 1, 2].sort()=}")                # .sort() sorts in place and returns None


# ---------------------------------------------------------------------------
# 8. ROUNDING
# ---------------------------------------------------------------------------
# round() returns a new number; :.1f only changes how it is printed.

print("\n--- 8. Rounding ---")

average = sum([18, 22, 15, 30, 27, 12, 25]) / 7   # 21.285714285714285

print(round(average, 1))        # 21.3 — a number you can keep calculating with
print(f"{average:.1f}")         # 21.3 — formatted text
print(int(21.9))                # 21 — int() cuts off, it does not round
print(round(2.5), round(3.5))   # 2 4 — .5 goes to the nearest even number
print(f"{3.5:.2f} €")           # 3.50 € — always exactly 2 digits


# ---------------------------------------------------------------------------
# 9. PUTTING IT ALL TOGETHER
# ---------------------------------------------------------------------------
# A small grade report that uses all the tricks above.

print("\n--- 9. Putting It All Together ---")

students = ["Anna", "Ben", "Clara", "David", "Emma", "Felix"]
grades   = [88, 54, 95, 72, 61, 79]

for rank, (student, grade) in enumerate(zip(students, grades), start=1):  # Nested unpacking
    print(f"{rank}. {student}: {grade}")

print(f"Average: {sum(grades) / len(grades):.1f}")

ranking = sorted(zip(grades, students), reverse=True)  # Grade first, so pairs sort by grade
winner, *others = ranking
print(f"Best: {winner[1]} with {winner[0]}")

passed = [s for s, g in zip(students, grades) if g >= 60]
print(f"{passed=}")
print(f"Everyone passed: {all(g >= 60 for g in grades)}")
print(f"Top 3: {[s for _, s in ranking[:3]]}")
