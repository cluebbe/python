# Workshop: Web Development with Flask

---

## Introduction

### Background

**Flask** is a small web framework for Python. It takes an incoming HTTP
request (someone opening a URL in a browser), finds the Python function you
registered for that URL, calls it, and sends whatever it returns back as the
response.

The connection between *a URL* and *a Python function* is called a **route**,
and it is written like this:

```python
@app.route("/hello")
def hello():
    return "Hello!"
```

That `@app.route(...)` line is the part most beginners find mysterious. It is
not Flask magic — it is a general Python language feature called a
**decorator**. Task 1 to 3 of this workshop build one from scratch so that
every later route makes sense.

| Concept | What it means |
|---|---|
| **Decorator** | A function that takes a function and returns a function, applied with `@` |
| **Route** | A URL pattern registered to a Python function |
| **View function** | The function that runs when a route is requested |
| **Request** | The incoming data: URL, method, form fields, query string |
| **Response** | What the view function returns: text, HTML, or JSON |

### Setting Up the Development Environment

Unlike the earlier workshops, this one needs a third-party package. Install it
in a virtual environment so it stays isolated from your system Python:

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install flask
```

Run with:

```bash
python flask_basics.py
```

Then open <http://127.0.0.1:5000> in your browser. Stop the server with
`Ctrl+C`.

---

## Task 1 — Functions Are Objects

Before decorators make sense, you need one fact: in Python a function is a
value like any other. You can assign it to a variable and pass it around.

Write a function `greet(name)` that returns a greeting. Then assign the
function *itself* to a second variable and call it through that new name.

<details>
<summary>Solution</summary>

```python
def greet(name):
    return f"Hello, {name}!"

say_hello = greet           # No parentheses — assigning the function, not calling it
print(say_hello("Alice"))   # "Hello, Alice!"

print(greet)                # <function greet at 0x...> — a normal object
```

**Key points:**
- `greet` is the function object; `greet()` *calls* it. Leaving off the
  parentheses is the whole trick.
- Because functions are objects, they can be stored in lists and dicts, passed
  as arguments, and returned from other functions.
- This is called being a **first-class object**, and every decorator depends
  on it.

</details>

---

## Task 2 — Writing a Decorator by Hand

A **decorator** is a function that takes a function and returns a replacement
for it.

Write a function `shout(func)` that returns a new function. The new function
should call `func` and return its result in uppercase. Apply it to `greet`
manually — no `@` yet.

<details>
<summary>Solution</summary>

```python
def shout(func):                # Takes a function as its argument
    def wrapper(name):          # Defines a replacement function
        result = func(name)     # Calls the original
        return result.upper()   # Modifies the result
    return wrapper              # Returns the function object — no parentheses, not called

def greet(name):
    return f"Hello, {name}!"

loud_greet = shout(greet)       # Wrap it
print(loud_greet("Bob"))        # "HELLO, BOB!"
print(greet("Bob"))             # "Hello, Bob!" — the original is untouched
```

**Key points:**
- `wrapper` is defined *inside* `shout`, so it can still see `func` after
  `shout` has returned. That captured variable is called a **closure**.
- `return wrapper` returns the function object. Writing `return wrapper()`
  would call it immediately and return its result instead — a very common
  beginner bug.
- Nothing has been decorated yet. `shout` is just a normal function that
  happens to accept and return functions.

</details>

---

## Task 3 — The `@` Syntax

`@decorator` above a `def` is **pure shorthand** for reassigning the function
to the decorator's result:

```python
@shout
def greet(name): ...
```

is exactly the same as:

```python
def greet(name): ...
greet = shout(greet)
```

Rewrite Task 2 using the `@` syntax and confirm the output is identical.

<details>
<summary>Solution</summary>

```python
def shout(func):
    def wrapper(name):
        return func(name).upper()
    return wrapper

@shout                          # Applied at definition time, once
def greet(name):
    return f"Hello, {name}!"

print(greet("Carol"))           # "HELLO, CAROL!"
```

**Key points:**
- The decorator runs **once**, when Python reads the `def` — not on every
  call. From then on the name `greet` simply points at `wrapper`.
- The `@` line must sit directly above the `def`.
- **`@shout` REPLACES your function.** Afterwards `greet` *is* `wrapper`, so
  calling it can only ever give you the shouted version — the plain
  `"Hello, Carol!"` is gone for good. Remember this when you reach Task 4:
  Flask's decorator deliberately does the opposite.
- You can stack decorators. They apply bottom-up: the one closest to the `def`
  wraps first.

</details>

---

## Task 4 — A Decorator That Registers Instead of Wraps

Flask's decorator does *not* replace your function. It **registers** it in a
lookup table and hands the original back unchanged.

### First: what is the `"/home"` in `@route("/home")`?

Every decorator so far was written bare, as `@shout`. But a route needs to know
*which URL* it is for, so you have to pass a value in. That changes the shape of
the decorator, and it is the part beginners trip over.

The rule: **`@` applies whatever the line evaluates to.**

- `@shout` — `shout` is already a decorator, so `@` applies it directly.
- `@route("/home")` — this **calls** `route("/home")` first, and applies
  *whatever it returns* to the function below.

So `route` itself is not the decorator. It is a function that *builds* one:

```python
@route("/home")
def home(): ...
```

happens in two steps:

```python
decorator = route("/home")      # Step 1: call route with the URL -> returns a decorator
home      = decorator(home)     # Step 2: @ applies that decorator to home
```

or in one line — note the **two** sets of parentheses:

```python
home = route("/home")(home)
```

That is why `route` needs an extra level of nesting compared to `shout`: the
outer function takes the **URL**, the inner one takes the **function**.

```python
def route(path):            # Outer: receives "/home"
    def decorator(func):    # Inner: receives the function home
        ...
        return func
    return decorator        # Outer returns the inner one
```

`path` stays available inside `decorator` even after `route` has returned — the
same closure you used in Task 2. That is how each route remembers its own URL.

**Rule of thumb:** parentheses in the `@` line mean one extra layer of nesting
in the definition.

### Now build it

1. Build a tiny version yourself: a dict `routes`, and a decorator `route(path)`
   that stores the decorated function under `path` and returns it untouched.
   Register two functions, then call one by looking up its URL.

2. Now prove the difference to Task 3. Write the **same** function twice under
   different names, decorate one with `@shout` and the other with
   `@route("/hello")`, then call both. Which one can still produce its original
   output — and what did each decorator do to the function you wrote?

<details>
<summary>Solution</summary>

**Step 1** — the registry and the decorator:

```python
routes = {}                     # The "URL -> function" table

def route(path):                # Takes the URL ...
    def decorator(func):        # ... and returns the actual decorator
        routes[path] = func     # The side effect: register the function
        return func             # Hand back the original, unchanged
    return decorator

@route("/home")                 # Means: home = route("/home")(home)
def home():
    return "This is the home page"

@route("/about")
def about():
    return "This is the about page"

print(routes)                   # {'/home': <function home>, '/about': <function about>}
print(routes["/home"]())        # "This is the home page"
print(home())                   # "This is the home page" — still works normally
```

**Step 2** — the two decorators side by side on identical functions. This is
*the* thing to understand about Flask routes:

```python
@shout                          # Replacing decorator: returns a NEW function
def hello_replaced(name):
    return f"Hello, {name}!"

@route("/hello")                # Registering decorator: returns the ORIGINAL function
def hello_registered(name):
    return f"Hello, {name}!"

print(hello_replaced("Dave"))       # "HELLO, DAVE!"  <- changed; plain greeting is gone
print(hello_registered("Dave"))     # "Hello, Dave!"  <- untouched, exactly as written
print(routes["/hello"]("Dave"))     # "Hello, Dave!"  <- and now reachable via its URL too
```

`hello_replaced` **lost** its original behaviour. `hello_registered` lost
nothing and **gained** a URL.

**Key points:**
- `route("/home")` is a **decorator factory**: it is called first with the
  URL, and *returns* the decorator that then receives the function. That extra
  layer is why `@app.route("/")` has parentheses while `@shout` does not.
- `return func` instead of `return wrapper` is the whole difference. The
  hidden assignment becomes `home = home`, so nothing is replaced: calling
  `home()` behaves exactly as before, and the only effect is the new entry in
  `routes`. The decorator **adds** a capability rather than swapping the
  function out.
- Look up the requested URL in that dict, call the function, send back the
  result — that is a web framework in miniature. Flask adds HTTP parsing,
  pattern matching, and a server around this same idea.

</details>

### When does the decorator's code actually run?

Add a `print` to each of the two decorators and something surprising happens:

```python
def shout(func):
    def wrapper(name):
        print("shout here!")                    # never appears until you CALL greet
        return func(name).upper()
    return wrapper

def route(path):
    def decorator(func):
        print(f"registering {path}")            # appears immediately, on its own
        routes[path] = func
        return func
    return decorator
```

Just *defining* the decorated functions prints `registering /home` — but not
`shout here!`. Before reading on: why?

<details>
<summary>Solution</summary>

The two prints sit at **different nesting levels**, even though on screen they
look parallel. Line the two decorators up by *role* instead of by indentation:

| Level | Receives | Runs | In `shout` | In `route` |
|---|---|---|---|---|
| 1 | the decorator's argument (`path`) | at the `@` line | — | `route` |
| 2 | the **function** (`func`) | at the `@` line | `shout` | `decorator` |
| 3 | the **call arguments** (`name`) | on every call | `wrapper` | — |

`shout` takes no argument, so it starts at level 2. `route` takes a URL, so it
starts at level 1 and its inner `decorator` is level 2.

That is the whole answer: **`decorator` is the counterpart of `shout` itself,
not of `wrapper`.** `wrapper` has no counterpart in the `route` version at
all — `route` does not wrap anything, it returns `func` untouched.

Trace each one:

```python
@shout
def greet(name): ...
```
Python runs `shout(greet)` once, right there. That body is only
`def wrapper...` + `return wrapper` — the print is not in it. `wrapper`'s body
does not execute until someone writes `greet("Charlie")`.

```python
@route("/home")
def home(): ...
```
Python runs `route("/home")` → gets back `decorator` → **immediately** runs
`decorator(home)`. Both happen at the `@` line, and the print lives inside
`decorator`, so it fires as the module is read. Calling `home()` afterwards
runs the plain original function — no decorator code is involved at all.

Move each print one level and the behaviour swaps. `shout` printing at
decoration time:

```python
def shout(func):
    print("hello")                  # decoration time now
    def wrapper(name):
        return func(name).upper()
    return wrapper
```

`route` printing at call time — which needs a wrapper it did not have before:

```python
def route(path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("hello")          # call time now
            return func(*args, **kwargs)
        routes[path] = wrapper
        return wrapper              # note: no longer the original function
    return decorator
```

**Key points:**
- A decorator body runs **once, when the function is defined**. Only code
  inside a returned `wrapper` runs **on each call**.
- Counting `def`s is not enough — ask *what does this level receive?* A level
  that receives `func` is decoration time; a level that receives the caller's
  arguments is call time.
- This is why `@app.route("/")` registers URLs at import time, and why
  `flask routes` can list every URL of your app without a single request
  arriving. Registration is decoration-time work.
- It also explains the most common decorator bug: forgetting `return func` (or
  `return wrapper`) leaves the decorator returning `None`, so the name is bound
  to `None` and calling it raises
  `TypeError: 'NoneType' object is not callable` — at call time, far from the
  `@` line that caused it.

</details>

---

## Task 5 — Your First Flask App

Create a Flask application object and register a view function for the URL
`/` that returns `"Hello, Flask!"`. Start the development server.

<details>
<summary>Solution</summary>

```python
from flask import Flask

app = Flask(__name__)           # The application object

@app.route("/")                 # Register index() for the URL "/"
def index():                    # This is the "view function"
    return "Hello, Flask!"      # A returned string becomes the response body

if __name__ == "__main__":
    app.run(debug=True)         # Start the development server
```

**Key points:**
- `__name__` tells Flask where the app lives on disk so it can locate
  `templates/` and `static/` relative to your file.
- `app.route` is a **method** on the app object, but works exactly like the
  `route` factory from Task 4 — it registers `index` in the app's URL map.
- `debug=True` restarts the server when you save a file and shows a detailed
  error page in the browser. **Never use it in production** — it exposes an
  interactive Python console to anyone who can reach the page.
- The server runs on <http://127.0.0.1:5000> by default. Stop it with
  `Ctrl+C`.

</details>

---

## Task 6 — Several Routes

Add routes for `/about` and `/contact`. Then make one single view function
answer both `/help` and `/faq`.

<details>
<summary>Solution</summary>

```python
@app.route("/about")
def about_page():
    return "This app is a Flask workshop."

@app.route("/contact")
def contact():
    return "Reach us at hello@example.com"

@app.route("/help")             # Stacked decorators: both URLs ...
@app.route("/faq")              # ... register the same function
def help_page():
    return "Help is on the way."
```

**Key points:**
- Every view function needs a **unique name**. Flask uses the function name as
  the internal endpoint name, so two functions called `about` raise
  `AssertionError: View function mapping is overwriting an existing endpoint`.
- Stacking route decorators works because each one registers the function and
  returns it unchanged — so the next decorator up receives the same function.
- Routes are matched in the order Flask's URL map resolves them, not strictly
  top to bottom; keep patterns distinct to avoid surprises.

</details>

---

## Task 7 — Dynamic Routes

Hard-coding one route per user does not scale. Capture part of the URL instead
by putting a variable name in angle brackets.

Write:
1. `/user/<username>` — greets the user by name.
2. `/post/<int:post_id>` — confirms the id and shows that it is a real `int`.

<details>
<summary>Solution</summary>

```python
@app.route("/user/<username>")          # /user/alice -> username = "alice"
def show_user(username):
    return f"Profile page of {username}"

@app.route("/post/<int:post_id>")       # /post/42 -> post_id = 42 (an int)
def show_post(post_id):
    return f"Post number {post_id} (type: {type(post_id).__name__})"
```

**Key points:**
- The name in the brackets must match the function parameter name exactly —
  Flask passes it as a keyword argument.
- Without a converter the value is always a **string**. `<int:post_id>` gives
  you a real integer and makes `/post/abc` return **404** automatically,
  because the pattern does not match.
- Available converters: `string` (default), `int`, `float`, `path` (like
  string but also matches `/`), and `uuid`. Note that `float` requires an
  actual decimal point — `<float:amount>` matches `/price/10.50` but **not**
  `/price/10`.

</details>

---

## Task 8 — Query Parameters

Everything after `?` in a URL is the **query string**. It is not part of the
route pattern — you read it from the `request` object.

Write a `/search` route that reads `q` and `limit` from
`/search?q=python&limit=5`, and prints a hint when `q` is missing.

<details>
<summary>Solution</summary>

```python
from flask import request

@app.route("/search")
def search():
    query = request.args.get("q", "")                   # "" if the parameter is absent
    limit = request.args.get("limit", 10, type=int)     # Converts "5" to 5
    if not query:
        return "Add ?q=something to the URL"
    return f"Searching for '{query}', showing up to {limit} results"
```

**Key points:**
- `request` is a **global-looking object that is actually per-request** —
  Flask swaps in the right one for whichever request your function is handling,
  so it is safe even with several users at once.
- Use `request.args.get("q")` rather than `request.args["q"]`: the bracket
  form raises a `400 Bad Request` when the parameter is missing.
- Query values always arrive as strings; `type=int` converts them and falls
  back to the default if conversion fails.
- Use the query string for optional filters and search terms; use URL
  variables for identifying a specific resource.

</details>

---

## Task 9 — HTTP Methods

A route answers only `GET` requests unless you say otherwise. Write a
`/register` route that shows an HTML form on `GET` and processes the submitted
name on `POST`.

<details>
<summary>Solution</summary>

```python
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "anonymous")
        return f"Registered {name}!"
    return """
        <form method="post">
            <input name="name" placeholder="Your name">
            <button type="submit">Register</button>
        </form>
    """
```

Test the POST side from a second terminal:

```bash
curl -X POST -d "name=Alice" http://127.0.0.1:5000/register
```

**Key points:**
- `methods=["GET", "POST"]` must list **every** method you accept — adding
  `POST` alone would break the form page. Anything else returns
  **405 Method Not Allowed**.
- `request.form` holds submitted form fields; `request.args` holds the query
  string; `request.get_json()` holds a JSON body. They are separate.
- The convention: `GET` reads data and changes nothing, `POST` creates or
  changes something. Browsers may repeat a `GET` freely, so never let one
  modify data.

</details>

---

## Task 10 — Returning JSON

Return a `dict` from `/api/status` with a status and a version, and a `list`
of user dicts from `/api/users`.

<details>
<summary>Solution</summary>

```python
@app.route("/api/status")
def api_status():
    return {"status": "ok", "version": "1.0"}

@app.route("/api/users")
def api_users():
    return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
```

**Key points:**
- Flask serialises a returned `dict` or `list` to JSON automatically and sets
  the `Content-Type: application/json` header. No `jsonify` call needed
  (Flask 2.2+; older code used `jsonify(...)` explicitly, which still works).
- Only JSON-compatible values work: strings, numbers, booleans, `None`, lists,
  and dicts. A `datetime` or a custom class raises a `TypeError` — convert it
  yourself, e.g. `value.isoformat()`.
- Returning a plain string sends `text/html` instead, which is why the browser
  renders the HTML in Task 9.

</details>

---

## Task 11 — HTML Templates

Returning HTML as a Python string gets unreadable fast. Flask uses the
**Jinja2** template engine instead: `{{ ... }}` inserts a value and
`{% ... %}` runs logic.

Write a `/welcome/<name>` route that renders a heading with the name and a
bulleted list of to-do items — with a fallback message when the list is empty.

<details>
<summary>Solution</summary>

```python
from flask import render_template_string

PAGE = """
<h1>Welcome, {{ name }}!</h1>
{% if items %}
    <ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul>
{% else %}
    <p>Your list is empty.</p>
{% endif %}
"""

@app.route("/welcome/<name>")
def welcome(name):
    todo = ["Learn decorators", "Build a route", "Render a template"]
    return render_template_string(PAGE, name=name, items=todo)
```

**Key points:**
- Values are passed as **keyword arguments** and become variables inside the
  template.
- `{{ }}` outputs a value, `{% %}` controls flow. Blocks must be closed
  explicitly: `{% endif %}`, `{% endfor %}`.
- Jinja2 **escapes HTML automatically**, so a name like `<script>` is
  displayed as text rather than executed. This is your main defence against
  cross-site scripting.
- In a real project use `render_template("welcome.html")` with the file in a
  `templates/` folder next to your app. `render_template_string` is used here
  only to keep the workshop in a single file.

</details>

---

## Task 12 — Handling Errors

Register a friendly page for **404 Not Found**.

<details>
<summary>Solution</summary>

```python
@app.errorhandler(404)
def not_found(error):
    return "Sorry, that page does not exist.", 404
```

**Key points:**
- `@app.errorhandler` is the **same decorator mechanism** as `@app.route` —
  it just registers the function under a status code instead of a URL. Once
  you see decorators as "register this function somewhere", every Flask
  extension point becomes predictable.
- Returning a tuple `(body, status_code)` sets the HTTP status. Without the
  explicit `404`, your error page would be served with status `200 OK` and
  confuse clients and search engines.
- The handler receives the error object as its argument, even if you ignore it.

</details>

---

## Task 13 — Putting It All Together

Build a small task API on an in-memory list:

1. `GET /tasks` — return all tasks plus a count.
2. `GET /tasks/<int:task_id>` — return one task, or a 404 JSON error.
3. `POST /tasks` — create a task from a submitted `title`, rejecting an empty
   one with 400.

<details>
<summary>Solution</summary>

```python
tasks = [
    {"id": 1, "title": "Learn Flask", "done": False},
    {"id": 2, "title": "Write a route", "done": True},
]

@app.route("/tasks")
def list_tasks():
    return {"tasks": tasks, "count": len(tasks)}

@app.route("/tasks/<int:task_id>")
def get_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"error": "Task not found"}, 404

@app.route("/tasks", methods=["POST"])
def add_task():
    title = request.form.get("title")
    if not title:
        return {"error": "title is required"}, 400
    new_task = {"id": max(t["id"] for t in tasks) + 1, "title": title, "done": False}
    tasks.append(new_task)
    return new_task, 201
```

Try it:

```bash
curl http://127.0.0.1:5000/tasks
curl http://127.0.0.1:5000/tasks/1
curl http://127.0.0.1:5000/tasks/99
curl -X POST -d "title=Buy milk" http://127.0.0.1:5000/tasks
```

**Key points:**
- `/tasks` appears twice with **different methods**, so `list_tasks` and
  `add_task` never collide — the method is part of what Flask matches on.
- Status codes carry meaning: `200` OK, `201` Created, `400` bad input from
  the client, `404` not found. Returning `{"error": ...}` with `200` would
  tell the client everything went fine.
- `max(t["id"] for t in tasks) + 1` is a **generator expression** — it walks
  the list without building a temporary one. It crashes on an empty list, so a
  real app would use a database that assigns ids for you.
- The list lives in memory and resets on every restart. `debug=True` reloads
  on each save, so your added tasks will disappear as you edit — expected here.

</details>

---

## Where to Next

- **Blueprints** — split a growing app into modules instead of one long file.
- **Databases** — Flask-SQLAlchemy to store data that survives a restart.
- **Deployment** — `app.run()` is a development server only; production uses
  a WSGI server such as Gunicorn or Waitress.
- **Decorators again** — now that the pattern is clear, look at
  `@app.before_request`, `@login_required` in Flask-Login, and `@functools.wraps`
  for writing decorators that preserve the wrapped function's name and docstring.
