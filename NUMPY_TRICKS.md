# Workshop: NumPy Tricks

---

## Introduction

### Background

**NumPy** is the package almost every data and AI library in Python is built
on — pandas, scikit-learn, PyTorch and matplotlib all use NumPy arrays under
the hood. A NumPy **array** looks like a list, but it does math on all its
items at once. That replaces most loops with one short line, and it runs much
faster.

This workshop builds on the List Tricks workshop: indexing, slicing and the
grade report from its last task all come back here. Each task introduces one
trick, and the last task combines all of them. Plan for about 30 minutes.

### Setting Up the Development Environment

**1. Check that Python is installed**

```bash
python --version
```

You need Python 3.9 or higher.

**2. Install NumPy in a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install numpy
```

**3. Run the tutorial file**

```bash
python numpy_tricks.py
```

**4. Create a practice file**

Type the tasks into your own file, for example `training.py`, starting with
`import numpy as np`, and run it after each task with `python training.py`.
For quick experiments, the interactive shell (`python` on its own) is handy
too.

> **Tip:** If your editor has an AI autocomplete (such as GitHub Copilot in
> VS Code), switch it off while practising — it will happily type the
> solutions for you.

---

## Task 1 — Math on a Whole Array

An array applies math to **every item at once**:

```python
prices = np.array([2.5, 4.0, 1.2])
prices * 2        # array([5. , 8. , 2.4])
prices + 1        # array([3.5, 5. , 2.2])
```

A plain list behaves differently: `[2.5, 4.0] * 2` **repeats** the list and
gives `[2.5, 4.0, 2.5, 4.0]`. Two arrays of the same length combine **item by
item**: `np.array([1, 2, 3]) * np.array([10, 20, 30])` gives
`array([10, 40, 90])`.

With

```python
prices     = np.array([2.5, 4.0, 1.2, 8.9])
quantities = np.array([3, 1, 10, 2])
```

1. Calculate the cost of each item (price × quantity)
2. Calculate the **total** cost — arrays have a `.sum()` method
3. Add 19 % VAT to every price and round the result to 2 decimal places

<details>
<summary>Solution</summary>

```python
costs = prices * quantities
print(f"{costs=}")                # array([ 7.5,  4. , 12. , 17.8])

total = costs.sum()
print(f"{total=}")                # np.float64(41.3)

with_vat = np.round(prices * 1.19, 2)
print(f"{with_vat=}")             # array([ 2.97,  4.76,  1.43, 10.59])
```

**Key points:**
- No loop and no list comprehension — `prices * quantities` does it all.
- `np.float64(41.3)` is just how NumPy shows a single number. It behaves
  like a normal float, and `print(total)` shows `41.3`.
- `np.round(array, 2)` rounds every item; the built-in `round()` only works
  on single numbers.
- `2.5 * 1.19` is stored as `2.9749999…`, so it rounds **down** to `2.97`.
  Floats are not exact — for money, round only for display.

</details>

---

## Task 2 — Creating and Reshaping Arrays

You rarely type arrays by hand:

```python
np.arange(0, 10, 2)      # array([0, 2, 4, 6, 8])  – like range()
np.linspace(0, 1, 5)     # array([0.  , 0.25, 0.5 , 0.75, 1.  ])  – end included
np.zeros(3)              # array([0., 0., 0.])
```

`.reshape(rows, columns)` turns a flat array into a **table** (a 2D array),
and `.shape` tells you its size:

```python
grid = np.arange(6).reshape(2, 3)
# [[0 1 2]
#  [3 4 5]]
grid.shape               # (2, 3)  →  2 rows, 3 columns
```

Write `-1` for one dimension and NumPy works it out: `reshape(3, -1)` on 6
items gives the shape `(3, 2)`.

1. Create the numbers 1 to 12 with `np.arange`
2. Reshape them into a table with 3 rows and 4 columns; print it and its shape
3. Reshape the same numbers into 2 rows using `-1`; print the shape
4. Create 5 evenly spaced values from 0 to 100 with `np.linspace`

<details>
<summary>Solution</summary>

```python
numbers = np.arange(1, 13)
print(numbers)                    # [ 1  2  3  4  5  6  7  8  9 10 11 12]

grid = numbers.reshape(3, 4)
print(grid)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
print(grid.shape)                 # (3, 4)

print(numbers.reshape(2, -1).shape)   # (2, 6)

print(np.linspace(0, 100, 5))     # [  0.  25.  50.  75. 100.]
```

**Key points:**
- Like `range`, `np.arange` **excludes** the stop value — 1 to 12 needs `13`.
- `np.linspace` is the opposite: it **includes** the end value.
- Reshape fills the new shape row by row. The total count must stay the same:
  `numbers.reshape(5, -1)` crashes, because 12 items do not fit into 5 rows.

</details>

---

## Task 3 — Indexing a Table

For a 2D array, put the row **and** the column in one pair of brackets:
`grid[row, column]`. Slices work in both directions, and `:` on its own means
"all":

```python
grid[1, 2]      # 7             → row 1, column 2 (counting from 0)
grid[-1]        # [ 9 10 11 12] → last row
grid[:, 0]      # [1 5 9]       → all rows, column 0: the first column
grid[:2, 1:3]   # [[2 3]
                #  [6 7]]
```

With the 3 × 4 table of 1 to 12 from Task 2, print:

1. The number `8`
2. The last column
3. The middle row
4. The bottom-right 2 × 2 block: `[[ 7  8] [11 12]]`
5. Every second column (columns 0 and 2)

<details>
<summary>Solution</summary>

```python
print(grid[1, 3])         # 8
print(grid[:, -1])        # [ 4  8 12]
print(grid[1])            # [5 6 7 8]
print(grid[-2:, -2:])     # [[ 7  8]
                          #  [11 12]]
print(grid[:, ::2])       # [[ 1  3]
                          #  [ 5  7]
                          #  [ 9 11]]
```

**Key points:**
- A whole column in one step — `grid[:, 0]` — is something plain lists
  cannot do.
- A single index or slice always applies to the **rows**: `grid[::2]` gives
  every second **row**. To reach the columns, say "all rows" first:
  `grid[:, ::2]`.
- `grid[1]` and `grid[1, :]` are the same thing.
- Collecting columns into a list, `[grid[:, 0], grid[:, 2]]`, gives a list of
  separate arrays — the table shape is lost. Prefer a slice.

</details>

---

## Task 4 — Boolean Masks

This is the most important NumPy trick. A comparison on an array gives an
array of `True` / `False` — a **mask**:

```python
temps = np.array([18, 25, 31, 12, 28, 35, 9])
temps > 25              # [False False  True False  True  True False]
```

Put the mask inside the brackets and you get only the items where it is
`True`:

```python
temps[temps > 25]       # [31 28 35]
```

Combine conditions with `&` (and) and `|` (or), with **brackets around each
condition**: `temps[(temps > 10) & (temps < 30)]`. Because `True` counts as
1, `.sum()` on a mask **counts** the matches.

With

```python
temps = np.array([18, 25, 31, 12, 28, 35, 9, 22, 30, 15])
```

1. Print all days that are 30 or warmer
2. Count how many days are below 15
3. Print the days that are colder than 12 **or** warmer than 32
4. Calculate the average temperature of the warm days only (above 20)
5. Set every temperature below 10 to `10` — a mask also works on the **left**
   side of `=`

<details>
<summary>Solution</summary>

```python
print(temps[temps >= 30])                       # [31 35 30]
print((temps < 15).sum())                       # 2
print(temps[(temps < 12) | (temps > 32)])       # [35  9]
print(temps[temps > 20].mean())                 # 28.5

temps[temps < 10] = 10
print(temps)          # [18 25 31 12 28 35 10 22 30 15]
```

**Key points:**
- Python's `and` / `or` do not work on arrays — use `&` / `|`.
- The brackets are required: `temps < 12 | temps > 32` is evaluated in the
  wrong order and crashes.
- `.mean()` replaces dividing the sum by the length yourself.
- `temps[mask] = value` changes the original array. Use `temps.copy()` first
  if you still need the old values.

</details>

---

## Task 5 — `np.where`

`np.where(condition, value_if_true, value_if_false)` is an if/else for every
item:

```python
temps = np.array([18, 25, 31, 12])
np.where(temps > 25, "hot", "ok")     # ['ok' 'ok' 'hot' 'ok']
np.where(temps < 15, 15, temps)       # [18 25 31 15]
```

The values can be whole arrays — NumPy picks item by item from one or the
other. For keeping values inside a range there is a shortcut:
`np.clip(temps, 15, 30)` gives `[18 25 30 15]`. Unlike the mask assignment in
Task 4, both return a **new** array and leave the original unchanged.

With

```python
grades = np.array([88, 54, 95, 72, 61, 79, 45])
```

1. Print `"pass"` or `"fail"` for each grade (pass = 60 or more)
2. Give a +10 bonus only to the failing grades
3. Add 8 points to everyone, but make sure no grade goes above 100
4. Label each grade `"A"` (90 or more), `"B"` (75 to 89) or `"C"` (below 75) —
   you can put an `np.where` inside another one

<details>
<summary>Solution</summary>

```python
print(np.where(grades >= 60, "pass", "fail"))
# ['pass' 'fail' 'pass' 'pass' 'pass' 'pass' 'fail']

print(np.where(grades < 60, grades + 10, grades))
# [88 64 95 72 61 79 55]

print(np.clip(grades + 8, 0, 100))
# [ 96  62 100  80  69  87  53]

print(np.where(grades >= 90, "A",
               np.where(grades >= 75, "B", "C")))
# ['B' 'C' 'A' 'C' 'C' 'B' 'C']
```

**Key points:**
- Nested `np.where` works like `if` / `elif` / `else`. For more than three
  categories, look at `np.select`.
- `np.clip` needs both a lower and an upper limit; `0` is a safe lower limit
  for grades.

</details>

---

## Task 6 — Sum, Mean and Max per Row or Column

On a table, `.sum()`, `.mean()`, `.max()` and `.min()` use **every** value.
With `axis` you choose the direction:

```python
# 3 students (rows) × 4 tests (columns)
scores = np.array([
    [80, 92, 75, 60],
    [55, 68, 90, 72],
    [95, 88, 85, 91],
])

scores.mean()          # 79.25                 → all values
scores.mean(axis=0)    # [76.7 82.7 83.3 74.3] → one result per column (test)
scores.mean(axis=1)    # [76.75 71.25 89.75]   → one result per row (student)
```

How to remember it: **the axis you name disappears.** `axis=0` collapses the
rows, so one value per column is left; `axis=1` collapses the columns, so one
value per row is left.

With the `scores` table above:

1. Print each student's best score
2. Print each test's lowest score
3. Print each student's total, and each test's average rounded to 1 decimal
4. Count how many scores of 80 or more each student has — combine Task 4 with
   this task

<details>
<summary>Solution</summary>

```python
print(scores.max(axis=1))                  # [92 90 95]
print(scores.min(axis=0))                  # [55 68 75 60]
print(scores.sum(axis=1))                  # [307 285 359]
print(np.round(scores.mean(axis=0), 1))    # [76.7 82.7 83.3 74.3]
print((scores >= 80).sum(axis=1))          # [2 1 4]
```

**Key points:**
- "Per student" means one value per **row**, so `axis=1`. "Per test" means
  one value per **column**, so `axis=0`.
- A mask keeps the table shape, so `(scores >= 80).sum(axis=1)` counts per
  row. Counting per row or column like this is very common.

</details>

---

## Task 7 — Broadcasting

When two arrays have different shapes, NumPy **stretches the smaller one** to
fit. A 1D array with one value per column is applied to **every row**:

```python
bonus = np.array([5, 0, 0, 10])     # one bonus per test
scores + bonus
# [[ 85  92  75  70]
#  [ 60  68  90  82]
#  [100  88  85 101]]
```

You already used this in Task 1: `prices * 1.19` stretches a single number
across the whole array.

**The rule:** NumPy compares the shapes **from the right**. Each pair of
sizes must be equal, or one of them must be 1.

- `(3, 4)` with `(4,)` → fits, applied to each row
- `(3, 4)` with `(3, 1)` → fits, applied to each column
- `(3, 4)` with `(3,)` → **error**, because 4 ≠ 3

With the `scores` table:

1. Add a bonus of 5 points to tests 2 and 3 (columns 1 and 2) for everyone
2. Show each score as a percentage of the best score on that test, rounded to
   whole numbers
3. Try `scores - scores.mean(axis=1)`. Why does it fail?
4. Fix it, so that you see how far each score is from **that student's**
   average. Hint: `.mean(axis=1, keepdims=True)`

<details>
<summary>Solution</summary>

```python
print(scores + np.array([0, 5, 5, 0]))
# [[80 97 80 60]
#  [55 73 95 72]
#  [95 93 90 91]]

print(np.round(scores / scores.max(axis=0) * 100))
# [[ 84. 100.  83.  66.]
#  [ 58.  74. 100.  79.]
#  [100.  96.  94. 100.]]

# scores - scores.mean(axis=1)
# ValueError: operands could not be broadcast together with shapes (3,4) (3,)

row_means = scores.mean(axis=1, keepdims=True)    # shape (3, 1)
print(np.round(scores - row_means, 1))
# [[  3.2  15.2  -1.8 -16.8]
#  [-16.2  -3.2  18.8   0.8]
#  [  5.2  -1.8  -4.8   1.2]]
```

**Key points:**
- `scores.mean(axis=1)` has shape `(3,)`. Compared from the right with
  `(3, 4)`, that is 3 against 4 — no match.
- `keepdims=True` keeps the collapsed axis with size 1, giving `(3, 1)`,
  which is stretched across the 4 columns.
- Per-column results (`axis=0`) broadcast without `keepdims`; per-row results
  (`axis=1`) need it.

</details>

---

## Task 8 — `argmax`, `argsort` and Fancy Indexing

`max()` gives the **value**; `argmax()` gives its **position**. Use that
position to look things up in another array:

```python
names    = np.array(["Anna", "Ben", "Clara"])
averages = scores.mean(axis=1)       # [76.75 71.25 89.75]

averages.argmax()                    # 2
names[averages.argmax()]             # 'Clara'
```

`argsort()` returns the positions in sorted order, smallest first. An array
also accepts a **list of positions** as its index — this is called **fancy
indexing**:

```python
averages.argsort()                   # [1 0 2]
names[[0, 2]]                        # ['Anna' 'Clara']
```

With `names` and `scores`:

1. Print the name of the student with the best average
2. Print all names ranked by average, best first
3. Print the score rows of Anna and Clara
4. Print the names of everyone with an average of 75 or more
5. Find the test with the highest average and print everyone's score on it

<details>
<summary>Solution</summary>

```python
averages = scores.mean(axis=1)

print(names[averages.argmax()])           # Clara

order = averages.argsort()[::-1]          # [2 0 1]
print(names[order])                       # ['Clara' 'Anna' 'Ben']

print(scores[[0, 2]])
# [[80 92 75 60]
#  [95 88 85 91]]

print(names[averages >= 75])              # ['Anna' 'Clara']

best_test = scores.mean(axis=0).argmax()  # 2
print(scores[:, best_test])               # [75 90 85]
```

**Key points:**
- `argsort()[::-1]` reverses the order, using the slicing step from the List
  Tricks workshop.
- A mask built from one array can filter **another** array of the same
  length: `names[averages >= 75]`. This replaces `zip` plus a list
  comprehension.
- `names[order]` replaces `sorted(zip(averages, names), reverse=True)`.

</details>

---

## Task 9 — Putting It All Together

There is nothing new here — this task mixes all the previous ones. It is the
grade report from the List Tricks workshop, this time without any loops:

```python
students = np.array(["Anna", "Ben", "Clara", "David", "Emma", "Felix"])
grades   = np.array([88, 54, 95, 72, 61, 79])
```

Print:

1. The average grade, rounded to 1 decimal place
2. The name of the best student and their grade
3. The names of everyone with 60 or more, and how many that is
4. Pass / fail labels for every grade
5. The top 3 students, best first
6. Whether everyone passed, and whether anyone got above 90 — arrays have
   `.all()` and `.any()`
7. The grades curved by +8 points, capped at 100

<details>
<summary>Solution</summary>

```python
students = np.array(["Anna", "Ben", "Clara", "David", "Emma", "Felix"])
grades   = np.array([88, 54, 95, 72, 61, 79])

# 1. Average
print(f"Average: {grades.mean():.1f}")                    # Average: 74.8

# 2. Best student
print(f"Best: {students[grades.argmax()]} with {grades.max()}")   # Clara with 95

# 3. Who passed, and how many
passed = grades >= 60
print(f"Passed: {students[passed]}")       # ['Anna' 'Clara' 'David' 'Emma' 'Felix']
print(f"Count: {passed.sum()}")            # Count: 5

# 4. Pass / fail labels
print(np.where(passed, "pass", "fail"))    # ['pass' 'fail' 'pass' 'pass' 'pass' 'pass']

# 5. Top 3
print(f"Top 3: {students[grades.argsort()[::-1][:3]]}")   # ['Clara' 'Anna' 'Felix']

# 6. Everyone passed? Anyone above 90?
print(passed.all())                        # False
print((grades > 90).any())                 # True

# 7. Curve
print(np.clip(grades + 8, 0, 100))         # [ 96  62 100  80  69  87]
```

**Key points:**
- Storing the mask in a variable (`passed`) lets you reuse it for filtering,
  counting, labelling and `.all()`.
- `.all()` and `.any()` are the array versions of the built-ins `all()` and
  `any()` from the List Tricks workshop.
- `grades.argsort()[::-1][:3]` reads left to right: positions sorted, then
  reversed, then the first 3.
- Compare this with the List Tricks solution: `zip`, `sorted` and list
  comprehensions are gone, because the arrays stay lined up by position.

</details>
