# Python Workshops

Hands-on Python tutorials, starting from scratch. No prior programming
experience needed for the first workshops, and the first two need no
third-party packages at all — they run on a plain Python installation.

Each tutorial comes as a pair: a runnable `.py` file you can execute and
experiment with, and a `.md` workshop file with step-by-step tasks and
collapsible solutions.

---

## Getting Started

**Requirements:** Python 3.9 or newer. Workshops 1 and 2 need nothing else;
workshop 3 additionally needs Flask.

```bash
# Check your Python version
python3 --version

# Run a tutorial
python3 python_basics.py

# Workshop 3 only — install Flask in a virtual environment first
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install flask
python flask_basics.py
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

### 3. Web Development with Flask
**Files:** [flask_basics.py](flask_basics.py) · [FLASK_BASICS.md](FLASK_BASICS.md)

Building a web application with Flask, starting from the language feature it
is built on: **decorators**. The workshop first constructs a decorator from
scratch in plain Python — including a miniature `@route` that registers
functions in a dictionary — so that `@app.route("/")` stops being magic. It
then covers dynamic URLs, query parameters, HTTP methods, JSON responses,
Jinja2 templates, and error handlers, ending with a small task API.

Start with Python Basics; the OOP workshop assumes you are comfortable with
functions, lists, and dictionaries, and the Flask workshop assumes both. More
advanced topics will be added here over time.

---

## Where to Next

These workshops were extracted from
[python-ai-dev](https://github.com/cluebbe/python-ai-dev), which applies
Python to speech recognition, text to speech, local language models, and
AI-powered code generation.
