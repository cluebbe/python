# Python Workshops

Hands-on Python tutorials, starting from scratch. No prior programming
experience needed for the first workshops, and no third-party packages —
everything runs on a plain Python installation.

Each tutorial comes as a pair: a runnable `.py` file you can execute and
experiment with, and a `.md` workshop file with step-by-step tasks and
collapsible solutions.

---

## Getting Started

**Requirements:** Python 3.9 or newer. Nothing else.

```bash
# Check your Python version
python3 --version

# Run a tutorial
python3 python_basics.py
```

Work through the `.md` file alongside the code: read a section, try the task
yourself, then open the solution to compare.

---

## Tutorials

### 1. Python Basics
**Files:** [python_basics.py](python_basics.py) · [PYTHON_BASICS.md](PYTHON_BASICS.md)

The core building blocks of Python for complete beginners. Covers variables
and data types, string formatting with f-strings, user input, conditionals,
lists, loops, dictionaries, and functions — ending with a small interactive
program that uses all of them together.

### 2. Object-Oriented Programming
**Files:** [oop_basics.py](oop_basics.py) · [OOP_BASICS.md](OOP_BASICS.md)

The four pillars of OOP in Python: classes, objects, inheritance, and
encapsulation. Walks through creating a class with `__init__` and instance
methods, readable `__str__` output, inheriting from a parent class, and using
`super()` to extend it — all illustrated with a practical library system
example.

Start with Python Basics; the OOP workshop assumes you are comfortable with
functions, lists, and dictionaries. More advanced topics will be added here
over time.

---

## Where to Next

These workshops were extracted from
[python-ai-dev](https://github.com/cluebbe/python-ai-dev), which applies
Python to speech recognition, text to speech, local language models, and
AI-powered code generation.
