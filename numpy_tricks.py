# NumPy Tricks Tutorial
#
# This tutorial shows the core NumPy tricks that replace loops with
# fast, short array operations. Run this file to see the output of each
# section, then experiment by changing the values and re-running.
#
# SETUP
# -----
# Requires NumPy. Install it in a virtual environment:
#   python3 -m venv venv
#   source venv/bin/activate        # Windows: venv\Scripts\activate
#   pip install numpy
# Run with:
#   python numpy_tricks.py

import numpy as np

print("=" * 40)
print("  NumPy Tricks Tutorial")
print("=" * 40)


# ---------------------------------------------------------------------------
# 1. ARRAYS AND VECTORIZED MATH
# ---------------------------------------------------------------------------
# An array applies math to every item at once — no loop needed.

print("\n--- 1. Arrays and Vectorized Math ---")

prices = np.array([2.5, 4.0, 1.2, 8.9])

print(f"{prices * 2=}")          # Every item doubled
print(f"{prices + 1=}")          # Every item plus 1
print(f"{prices ** 2=}")         # Every item squared
print(f"{[2.5, 4.0] * 2=}")      # A list repeats instead: [2.5, 4.0, 2.5, 4.0]

quantities = np.array([3, 1, 10, 2])
print(f"{prices * quantities=}")            # Item by item
print(f"{(prices * quantities).sum()=}")    # Total cost
print(f"{np.round(prices * 1.19, 2)=}")     # Round every item at once


# ---------------------------------------------------------------------------
# 2. CREATING AND RESHAPING ARRAYS
# ---------------------------------------------------------------------------
# arange, linspace, zeros and ones build arrays; reshape changes the shape.

print("\n--- 2. Creating and Reshaping Arrays ---")

print(f"{np.arange(0, 10, 2)=}")      # Like range(): [0 2 4 6 8]
print(f"{np.linspace(0, 1, 5)=}")     # 5 evenly spaced numbers, end included
print(f"{np.zeros(3)=}")
print(f"{np.ones((2, 3))=}")          # Shape is a tuple: 2 rows, 3 columns

grid = np.arange(12).reshape(3, 4)   # 3 rows, 4 columns
print(grid)
print(f"{grid.shape=}")              # (3, 4)
print(f"{grid.reshape(2, -1).shape=}")   # -1 means "work it out": (2, 6)
print(f"{grid.T.shape=}")            # Transposed: (4, 3)


# ---------------------------------------------------------------------------
# 3. INDEXING 2D ARRAYS
# ---------------------------------------------------------------------------
# grid[row, column] — and slices work in both directions.

print("\n--- 3. Indexing 2D Arrays ---")

print(f"{grid[1, 2]=}")      # Row 1, column 2: 6
print(f"{grid[-1]=}")        # Last row
print(f"{grid[:, 0]=}")      # First column — impossible with a plain slice on lists
print(f"{grid[:2, 1:3]=}")   # Top 2 rows, columns 1 and 2
print(f"{grid[:, ::2]=}")    # Every second column — grid[::2] would take every second row


# ---------------------------------------------------------------------------
# 4. BOOLEAN MASKS
# ---------------------------------------------------------------------------
# A comparison gives an array of True/False; use it as an index to filter.

print("\n--- 4. Boolean Masks ---")

temps = np.array([18, 25, 31, 12, 28, 35, 9])

print(f"{temps > 25=}")                       # The mask
print(f"{temps[temps > 25]=}")                # Only the hot days
print(f"{temps[(temps > 10) & (temps < 30)]=}")   # & means and, | means or
print(f"{(temps > 25).sum()=}")               # True counts as 1: number of hot days
print(f"{temps[temps > 25].mean()=}")         # Average of the hot days only

warm = temps.copy()
warm[warm < 10] = 10                          # A mask on the left of = overwrites
print(f"{warm=}")


# ---------------------------------------------------------------------------
# 5. np.where
# ---------------------------------------------------------------------------
# np.where(condition, if_true, if_false) — an if/else for every item.

print("\n--- 5. np.where ---")

print(f"{np.where(temps > 25, 'hot', 'ok')=}")
print(f"{np.where(temps < 10, 10, temps)=}")    # Replace values below 10
print(f"{np.clip(temps, 10, 30)=}")             # Shortcut: limit to 10..30

grades = np.array([88, 54, 95, 72])
print(f"{np.where(grades >= 90, 'A', np.where(grades >= 75, 'B', 'C'))=}")   # Nested: if/elif/else


# ---------------------------------------------------------------------------
# 6. AGGREGATING ALONG AN AXIS
# ---------------------------------------------------------------------------
# axis=0 collapses the rows (one result per column),
# axis=1 collapses the columns (one result per row).

print("\n--- 6. Aggregating Along an Axis ---")

# 3 students (rows), 4 tests (columns)
scores = np.array([
    [80, 92, 75, 60],
    [55, 68, 90, 72],
    [95, 88, 85, 91],
])

print(f"{scores.mean()=}")            # Everything
print(f"{scores.mean(axis=0)=}")      # Per test (column)
print(f"{scores.mean(axis=1)=}")      # Per student (row)
print(f"{scores.max(axis=1)=}")       # Best score of each student
print(f"{(scores >= 80).sum(axis=1)=}")   # Scores of 80+ per student: mask + axis


# ---------------------------------------------------------------------------
# 7. BROADCASTING
# ---------------------------------------------------------------------------
# Arrays with different shapes are stretched to match automatically.

print("\n--- 7. Broadcasting ---")

bonus = np.array([5, 0, 0, 10])     # One bonus per test
print(scores + bonus)               # Added to every row

print(np.round(scores / scores.max(axis=0) * 100))   # Percent of each test's best score

centered = scores - scores.mean(axis=0)   # Distance from each test's average
print(np.round(centered, 1))

row_means = scores.mean(axis=1, keepdims=True)   # Shape (3, 1) instead of (3,)
print(np.round(scores - row_means, 1))           # Distance from each student's average


# ---------------------------------------------------------------------------
# 8. SORTING AND PICKING: argmax, argsort, fancy indexing
# ---------------------------------------------------------------------------
# The arg-functions return positions, not values. Use those positions
# as an index — even a whole list of them at once.

print("\n--- 8. argmax, argsort and Fancy Indexing ---")

names = np.array(["Anna", "Ben", "Clara"])
averages = scores.mean(axis=1)

print(f"{averages.argmax()=}")          # Position of the best: 2
print(f"{names[averages.argmax()]=}")   # Clara
order = averages.argsort()[::-1]        # Positions, best first
print(f"{order=}")
print(f"{names[order]=}")               # Fancy indexing: a list of positions
print(f"{names[[0, 2]]=}")              # Pick Anna and Clara
print(f"{scores[:, scores.mean(axis=0).argmax()]=}")   # Everyone's score on the best test


# ---------------------------------------------------------------------------
# 9. PUTTING IT ALL TOGETHER
# ---------------------------------------------------------------------------
# The grade report from the List Tricks workshop — without a single loop
# for the calculations.

print("\n--- 9. Putting It All Together ---")

students = np.array(["Anna", "Ben", "Clara", "David", "Emma", "Felix"])
grades   = np.array([88, 54, 95, 72, 61, 79])

print(f"Average: {grades.mean():.1f}")
print(f"Best: {students[grades.argmax()]} with {grades.max()}")
print(f"Passed: {students[grades >= 60]}")
print(f"Labels: {np.where(grades >= 60, 'pass', 'fail')}")
print(f"Top 3: {students[grades.argsort()[::-1][:3]]}")
print(f"Everyone passed: {(grades >= 60).all()}")
print(f"Curved (+5, max 100): {np.clip(grades + 5, 0, 100)}")
