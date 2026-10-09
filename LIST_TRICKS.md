# Workshop: List Tricks

---

## Introduction

### Background

What other languages call an **array** is usually a **list** in Python:
`[10, 20, 30]`. Lists are everywhere — in data processing, in AI pipelines,
in web apps — and Python has a set of short, readable tricks for working with
them that replace many lines of loop code.

This workshop builds on the lists and loops from the Python Basics workshop.
Each task introduces one trick, and the last task combines all of them.

### Setting Up the Development Environment

**1. Check that Python is installed**

```bash
python --version
```

You need Python 3.8 or higher. The optional `zip(..., strict=True)` in
Task 6 needs Python 3.10.

**2. Run the tutorial file**

```bash
python list_tricks.py
```

No extra packages are needed — everything in this workshop is built into Python.

**3. Create a practice file**

Type the tasks into your own file, for example `training.py`, and run it
after each task with `python training.py`. Typing the code yourself teaches
far more than reading the solutions.

> **Tip:** If your editor has an AI autocomplete (such as GitHub Copilot in
> VS Code), switch it off while practising — it will happily type the
> solutions for you. In VS Code, click the Copilot icon in the status bar and
> untick code completions, or set `"editor.inlineSuggest.enabled": false`.

---

## Task 1 — Indexing and Negative Indexes

Every item in a list has a position (its **index**), and counting starts at
**0**. Negative indexes count from the **end**: `-1` is the last item.

```
values:     10   20   30   40   50   60
positive:    0    1    2    3    4    5
negative:   -6   -5   -4   -3   -2   -1
```

A handy f-string trick for practising: `f"{expression=}"` prints the code
**and** its result, so `print(f"{numbers[0]=}")` prints `numbers[0]=10`.

With `numbers = [10, 20, 30, 40, 50, 60]`, print:
1. The first number
2. The last number, using a negative index
3. The number `40` — once with a positive index and once with a negative index

<details>
<summary>Solution</summary>

```python
numbers = [10, 20, 30, 40, 50, 60]

print(f"{numbers[0]=}")    # numbers[0]=10
print(f"{numbers[-1]=}")   # numbers[-1]=60
print(f"{numbers[3]=}")    # numbers[3]=40
print(f"{numbers[-3]=}")   # numbers[-3]=40
```

**Key points:**
- The first item is `numbers[0]`, not `numbers[1]`. This off-by-one mistake
  is the most common bug in programming.
- `numbers[-1]` replaces the clumsy `numbers[len(numbers) - 1]`.
- Without the `f`, the braces are printed literally:
  `print("{numbers[0]}")` prints `{numbers[0]}`.
- An index past the end, such as `numbers[10]`, crashes with an `IndexError`.

</details>

---

## Task 2 — Slicing

Indexing gets **one** item. **Slicing** gets a piece of the list:
`list[start:stop]`.

- `start` is **included**, `stop` is **not** — `numbers[1:4]` gives 3 items.
- Leave out `start` to begin at the start, leave out `stop` to go to the end.
- Negative indexes work here too.

With the same `numbers` list, print:
1. The first 3 numbers
2. The last 3 numbers, using a negative index
3. `[30, 40, 50]`
4. Everything **except** the first and the last number

<details>
<summary>Solution</summary>

```python
print(f"{numbers[:3]=}")     # [10, 20, 30]
print(f"{numbers[-3:]=}")    # [40, 50, 60]
print(f"{numbers[2:5]=}")    # [30, 40, 50]
print(f"{numbers[1:-1]=}")   # [20, 30, 40, 50]
```

**Key points:**
- `[-n:]` means "the last n items" and `[:-n]` means "everything except the
  last n" — both are very common in real code.
- `numbers[:]` is a copy of the whole list.
- Slicing never crashes: `numbers[2:100]` just stops at the end of the list.

</details>

---

## Task 3 — Slicing with a Step

A slice takes an optional third number, the **step**:
`list[start:stop:step]`. A step of 2 takes every second item. A **negative
step** walks backwards, which makes `[::-1]` the shortest way to reverse a
list — and it works on strings too.

1. Print `numbers` reversed
2. Print the numbers at even positions: `[10, 30, 50]`
3. Print the numbers at odd positions: `[20, 40, 60]`
4. Store your first name in a variable and print it backwards
5. Check whether `"racecar"` and `"python"` are palindromes (they read the
   same forwards and backwards) — print `True` or `False` for each

<details>
<summary>Solution</summary>

```python
print(f"{numbers[::-1]=}")   # [60, 50, 40, 30, 20, 10]
print(f"{numbers[::2]=}")    # [10, 30, 50]
print(f"{numbers[1::2]=}")   # [20, 40, 60]

name = "Alice"
print(name[::-1])            # ecilA

print("racecar"[::-1] == "racecar")   # True
print("python"[::-1] == "python")     # False
```

**Key points:**
- `[::2]` and `[1::2]` split a list into its even and odd positions.
- The step combines with start and stop: `numbers[::-2]` gives
  `[60, 40, 20]`.
- Put spaces around `=` and `==` — `name = "Alice"` reads more easily than
  `name="Alice"`.

</details>

---

## Task 4 — Unpacking

**Unpacking** pulls the values out of a list into variables in one line:
`x, y = [3, 7]`. The number of variables must match the number of items.

Two extras make it really useful:
- A variable with a **star** collects "the rest" into a list:
  `first, *rest = numbers`.
- By convention, `_` means "I don't need this value".

1. Unpack `person = ["Alice", "Developer", "Germany"]` into `name`, `job`
   and `country`, then print a sentence with them
2. Set `a = "left"` and `b = "right"`, swap them in one line, and print them
3. Unpack `numbers` into `first`, `middle` and `last` using `*`
4. From `scores = [95, 88, 72, 65, 50]`, get only the top two into `gold`
   and `silver` and ignore the rest
5. **Think about it:** what does `first, *middle, last = [1, 2]` give?
   Guess first, then run it.

<details>
<summary>Solution</summary>

```python
person = ["Alice", "Developer", "Germany"]
name, job, country = person
print(f"My name is {name}, I am a {job}, and I live in {country}.")

a = "left"
b = "right"
a, b = b, a
print(f"{a=} {b=}")                    # a='right' b='left'

first, *middle, last = numbers
print(f"{first=} {middle=} {last=}")   # first=10 middle=[20, 30, 40, 50] last=60

scores = [95, 88, 72, 65, 50]
gold, silver, *_ = scores
print(f"{gold=} {silver=}")            # gold=95 silver=88

first, *middle, last = [1, 2]
print(f"{middle=}")                    # middle=[]
```

**Key points:**
- `a, b = b, a` swaps two variables without a temporary variable.
- The star variable is always a **list** — possibly an empty one.
- A mismatch without a star crashes: `a, b = [1, 2, 3]` raises
  `ValueError: too many values to unpack`.

</details>

---

## Task 5 — List Comprehensions

A **list comprehension** builds a new list from an old one in a single line.
The loop

```python
doubled = []
for n in numbers:
    doubled.append(n * 2)
```

becomes `doubled = [n * 2 for n in numbers]` — read it as "n × 2, for each
n in numbers".

```
[ n * 2   for n in numbers   if n > 30 ]
  ─────   ────────────────   ─────────
  what    where it comes     optional
  to keep from               filter
```

To **choose between two values** instead of filtering, `if / else` goes at
the **front**: `["big" if n > 30 else "small" for n in numbers]`.

With `numbers` and `words = ["apple", "Banana", "cherry", "Date"]`:
1. Make a list with each number squared (`n ** 2`)
2. Make a list with only the numbers divisible by 20 (`n % 20 == 0`)
3. Make a list with only the words longer than 5 letters
4. Make a list with the first letter of each word: `['a', 'B', 'c', 'D']`
5. Make a list saying `"even"` or `"odd"` for each of `[1, 2, 3, 4, 5]`
6. Make a list of each word reversed

<details>
<summary>Solution</summary>

```python
words = ["apple", "Banana", "cherry", "Date"]

squared = [n ** 2 for n in numbers]
print(f"{squared=}")         # [100, 400, 900, 1600, 2500, 3600]

divisible_by_20 = [n for n in numbers if n % 20 == 0]
print(f"{divisible_by_20=}") # [20, 40, 60]

long_words = [w for w in words if len(w) > 5]
print(f"{long_words=}")      # ['Banana', 'cherry']

first_letters = [w[0] for w in words]
print(f"{first_letters=}")   # ['a', 'B', 'c', 'D']

even_odd = ["even" if n % 2 == 0 else "odd" for n in [1, 2, 3, 4, 5]]
print(f"{even_odd=}")        # ['odd', 'even', 'odd', 'even', 'odd']

reversed_words = [w[::-1] for w in words]
print(f"{reversed_words=}")  # ['elppa', 'ananaB', 'yrrehc', 'etaD']
```

**Key points:**
- `if` **at the end** filters: the new list can be shorter.
- `if / else` **at the front** picks a value: the new list always has the
  same length.
- Any expression can go at the front, including the tricks from earlier
  tasks like `w[0]` and `w[::-1]`.
- Name variables after what they hold: `first_letters`, not `capitals`, when
  some of the letters are lowercase.

</details>

---

## Task 6 — `enumerate` and `zip`

**`enumerate`** gives you the position and the item together, replacing
`for i in range(len(words))`:

```python
for i, word in enumerate(words):                # 0 apple, 1 Banana, ...
    print(i, word)

for rank, word in enumerate(words, start=1):    # 1 apple, 2 Banana, ...
    print(rank, word)
```

**`zip`** walks through two lists side by side, pairing the first with the
first, the second with the second, and so on:

```python
for name, age in zip(["Anna", "Ben"], [28, 35]):
    print(f"{name} is {age}")
```

Both hand out pairs that you **unpack** — the same trick as in Task 4.
`dict(zip(keys, values))` turns two lists into a dictionary, and
`zip(items, items[1:])` pairs each item with the next one.

1. Print `words` as a numbered list starting at 1: `1. apple`, `2. Banana`, …
2. Using `enumerate`, collect only the words at even positions, together
   with their position
3. With `cities = ["Berlin", "Paris", "Rome"]` and
   `countries = ["Germany", "France", "Italy"]`, print `Berlin is in Germany`
   and so on
4. Turn `cities` and `countries` into a dictionary
5. Using a comprehension with `zip`, make the list
   `['Berlin-Germany', 'Paris-France', 'Rome-Italy']`
6. With `scores = [50, 65, 72, 88, 95]`, find how much each score went up
   compared with the previous one

<details>
<summary>Solution</summary>

```python
for rank, word in enumerate(words, start=1):
    print(f"{rank}. {word}")

evens = [(i, w) for i, w in enumerate(words) if i % 2 == 0]
print(f"{evens=}")           # [(0, 'apple'), (2, 'cherry')]

cities = ["Berlin", "Paris", "Rome"]
countries = ["Germany", "France", "Italy"]

for city, country in zip(cities, countries):
    print(f"{city} is in {country}")

country_by_city = dict(zip(cities, countries))
print(f"{country_by_city=}") # {'Berlin': 'Germany', 'Paris': 'France', 'Rome': 'Italy'}

pairs = [f"{city}-{country}" for city, country in zip(cities, countries)]
print(f"{pairs=}")           # ['Berlin-Germany', 'Paris-France', 'Rome-Italy']

scores = [50, 65, 72, 88, 95]
increases = [b - a for a, b in zip(scores, scores[1:])]
print(f"{increases=}")       # [15, 7, 16, 7]
```

**Key points:**
- `zip` hands out pairs **in the order you pass the lists**. Writing
  `for city, country in zip(countries, cities)` puts each country into
  `city` — the variable names do not change what is inside.
- `zip` stops at the **shorter** list and silently drops the rest. Use
  `zip(a, b, strict=True)` (Python 3.10+) to get an error instead.
- `start=0` is the default for `enumerate`, so you only write `start=` when
  you want something else.
- Pairs are usually written as tuples `(i, w)` rather than lists `[i, w]`.

</details>

---

## Task 7 — Useful Built-ins

Python has one-word functions for common list jobs:

| Function | Result |
|---|---|
| `sum(x)`, `min(x)`, `max(x)`, `len(x)` | Total, smallest, largest, count |
| `sorted(x)` | A **new** sorted list; the original is unchanged |
| `sorted(x, reverse=True)` | Largest first |
| `sorted(x, key=len)` | Sorted by what `key` returns, here the length |
| `any(...)` / `all(...)` | Is **at least one** / is **every** item true? |
| `item in x` | Is the item in the list? |

`any`, `all`, `sum`, `min` and `max` accept a comprehension without the
square brackets: `any(s > 90 for s in scores)`. Counting matches is
`sum(1 for s in scores if s >= 70)`.

With `temps = [18, 22, 15, 30, 27, 12, 25]`:
1. Print the highest, the lowest and the average temperature
2. Print `temps` sorted from hottest to coldest, then print `temps` again to
   show it is unchanged
3. Print the 3 hottest temperatures
4. Check whether any day was colder than 15, and whether every day was above 10
5. Count the days that were 25 **or warmer**
6. Sort `cities` by length, longest first
7. **Think about it:** what does `print([3, 1, 2].sort())` print?

<details>
<summary>Solution</summary>

```python
temps = [18, 22, 15, 30, 27, 12, 25]

print(f"{max(temps)=} {min(temps)=}")      # max(temps)=30 min(temps)=12
print(f"{sum(temps) / len(temps)=}")       # 21.285714285714285

print(sorted(temps, reverse=True))         # [30, 27, 25, 22, 18, 15, 12]
print(temps)                               # [18, 22, 15, 30, 27, 12, 25]

print(sorted(temps, reverse=True)[:3])     # [30, 27, 25]

print(any(t < 15 for t in temps))          # True
print(all(t > 10 for t in temps))          # True

print(sum(1 for t in temps if t >= 25))    # 3

print(sorted(cities, key=len, reverse=True))   # ['Berlin', 'Paris', 'Rome']

print([3, 1, 2].sort())                    # None
```

**Key points:**
- `sorted(x)` returns a new list; `x.sort()` sorts `x` **in place** and
  returns `None`. Writing `result = x.sort()` leaves `result` as `None`.
- "25 or warmer" is `t >= 25`, not `t > 25`. This off-by-one bug runs
  without any error and simply gives the wrong count — read conditions
  carefully.
- Plain `sorted(words)` puts capitals first (`'Banana'` before `'apple'`).
  Use `key=str.lower` to ignore case.
- `max(words, key=len)` returns the longest word.

</details>

---

## Task 8 — Rounding

There are two ways to round, and they do different things:

| Goal | Use | Example |
|---|---|---|
| Show a nicely formatted number | `f"{x:.1f}"` | `f"{21.2857:.1f}"` → `21.3` |
| Keep calculating with the rounded value | `round(x, 1)` | `round(21.2857, 1)` → `21.3` |

`:.1f` means "show as a **f**loat with **1** digit after the decimal point".
It only changes the printed text; the number itself stays the same.

Two surprises:
- `int()` cuts the decimals off instead of rounding: `int(21.9)` is `21`.
- `round()` sends an exact `.5` to the nearest **even** number:
  `round(2.5)` is `2`, `round(3.5)` is `4` ("banker's rounding").

1. Print the average of `temps` three ways: with `round(..., 1)`, with `:.1f`,
   and with `int()`
2. Guess, then print, `round(0.5)`, `round(1.5)` and `round(2.5)`
3. Print the price `3.5` so that it looks like `3.50 €`

<details>
<summary>Solution</summary>

```python
average = sum(temps) / len(temps)

print(round(average, 1))     # 21.3
print(f"{average:.1f}")      # 21.3
print(int(average))          # 21

print(round(0.5), round(1.5), round(2.5))   # 0 2 2

price = 3.5
print(f"{price:.2f} €")      # 3.50 €
```

**Key points:**
- `round(5.0, 2)` gives `5.0`, but `f"{5.0:.2f}"` gives `5.00` — use the
  f-string form for prices.
- `round(x)` without a second number returns an `int`.
- `f"{1234567.891:,.2f}"` adds a thousands separator: `1,234,567.89`.

</details>

---

## Task 9 — Putting It All Together

There is nothing new here — this task mixes all the previous ones. Start with:

```python
students = ["Anna", "Ben", "Clara", "David", "Emma", "Felix"]
grades   = [88, 54, 95, 72, 61, 79]
```

The grades belong to the students in the same order. Print:

1. A numbered class overview: `1. Anna: 88`, `2. Ben: 54`, …
2. The average grade, rounded to 1 decimal place
3. The name and grade of the best student
4. A list of the names of everyone with 60 or more
5. Pass / fail labels: `['Anna: pass', 'Ben: fail', …]`
6. The top 3 students with their grades, best first
7. Whether everyone passed, and whether anyone got above 90
8. Unpack the full ranking from item 6 so that `winner` holds the top
   student and `others` holds everyone else

<details>
<summary>Solution</summary>

```python
students = ["Anna", "Ben", "Clara", "David", "Emma", "Felix"]
grades   = [88, 54, 95, 72, 61, 79]

# 1. Class overview
for rank, (student, grade) in enumerate(zip(students, grades), start=1):
    print(f"{rank}. {student}: {grade}")

# 2. Average
print(f"Average: {sum(grades) / len(grades):.1f}")       # Average: 74.8

# 3. Best student
best_grade, best_student = max(zip(grades, students))
print(f"Best: {best_student} with {best_grade}")         # Best: Clara with 95

# 4. Who passed
passed = [s for s, g in zip(students, grades) if g >= 60]
print(f"{passed=}")       # ['Anna', 'Clara', 'David', 'Emma', 'Felix']

# 5. Pass / fail labels
labels = [f"{s}: {'pass' if g >= 60 else 'fail'}" for s, g in zip(students, grades)]
print(f"{labels=}")

# 6. Top 3
ranking = sorted(zip(grades, students), reverse=True)
for grade, student in ranking[:3]:
    print(f"{student}: {grade}")    # Clara: 95, Anna: 88, Felix: 79

# 7. Everyone passed? Anyone above 90?
print(all(g >= 60 for g in grades))   # False
print(any(g > 90 for g in grades))    # True

# 8. Winner and the rest
winner, *others = ranking
print(f"{winner=}")       # winner=(95, 'Clara')
print(f"{others=}")
```

**Key points:**
- `enumerate(zip(...))` hands out `(rank, (student, grade))`, and the
  brackets in `for rank, (student, grade) in ...` unpack both levels at once.
- `zip(grades, students)` puts the grade **first** on purpose: pairs are
  compared by their first item, so `max` and `sorted` order them by grade.
- An alternative for item 3 is a dictionary:
  `grade_by_student = dict(zip(students, grades))` and then
  `max(grade_by_student, key=grade_by_student.get)`.
- Inside an f-string that uses double quotes, use single quotes for strings:
  `{'pass' if g >= 60 else 'fail'}`.

</details>
