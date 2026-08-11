# Flask Basics Tutorial
#
# This tutorial introduces Flask, a small web framework for Python, and the
# language feature it is built around: DECORATORS.
#
# Unlike the earlier workshops, this one needs a third-party package.
#
# SETUP
# -----
#   python3 -m venv venv
#   source venv/bin/activate        # Windows: venv\Scripts\activate
#   pip install flask
#
# Run with:
#   python flask_basics.py
#
# Then open http://127.0.0.1:5000 in your browser.
# Stop the server with Ctrl+C.

from flask import Flask, request, render_template_string

print("=" * 40)
print("  Flask Basics Tutorial")
print("=" * 40)


# ---------------------------------------------------------------------------
# 1. THE LANGUAGE FEATURE BEHIND ROUTES: DECORATORS
# ---------------------------------------------------------------------------
# Every Flask route looks like this:
#
#     @app.route("/hello")
#     def hello():
#         return "Hello!"
#
# The "@something" line is a DECORATOR. Before touching Flask, let's build one
# from scratch in plain Python — it is a normal language feature, not magic.

print("\n--- 1. Decorators (plain Python, no Flask) ---")

# Step A: in Python, functions are objects. You can pass them around like any
# other value — assign them to variables, put them in lists, hand them to
# other functions.

def greet(name):                    # An ordinary function
    return f"Hello, {name}!"

say_hello = greet                   # Assign the FUNCTION itself (no parentheses!)
print(say_hello("Alice"))           # "Hello, Alice!" — same function, second name

# Step B: because functions are objects, a function can TAKE a function as an
# argument and RETURN a new function that wraps it. That is a decorator.

def shout(func):                    # Takes a function ...
    def wrapper(name):              # ... defines a replacement for it ...
        result = func(name)         # ... which calls the original ...
        return result.upper()       # ... and modifies the result
    return wrapper                  # Returns the replacement (not calling it!)

loud_greet = shout(greet)           # Wrap greet by hand
print(loud_greet("Bob"))            # "HELLO, BOB!"

# Step C: the "@" syntax is nothing but shorthand for exactly that wrapping.

@shout                              # This line means: greet_loudly = shout(greet_loudly)
def greet_loudly(name):
    return f"Hello, {name}!"

print(greet_loudly("Carol"))        # "HELLO, CAROL!" — @shout was applied at definition time

# Note what @shout COST us: greet_loudly is the wrapper now, so the plain
# "Hello, Carol!" can no longer be produced. This decorator REPLACED the
# function. Flask's decorator deliberately does the opposite — see Step D.

# Step D: a decorator does not have to replace the function. It can simply
# REGISTER it somewhere and hand back the original, unchanged. This is what
# Flask's @app.route does.

routes = {}                         # Our own tiny "URL -> function" table

# About the "/home" argument: "@" applies whatever the line evaluates to.
# "@shout" is already a decorator, so it is applied directly. But "@route(...)"
# CALLS route first and applies whatever comes back, in two steps:
#
#     decorator = route("/home")    # 1. call route with the URL -> get a decorator
#     home      = decorator(home)   # 2. @ applies that decorator to home
#
# In one line (note the TWO sets of parentheses): home = route("/home")(home)
# Hence the extra nesting level: the outer function takes the URL, the inner
# one takes the function. Rule of thumb: parentheses in the "@" line mean one
# more layer in the definition.

def route(path):                    # Outer: receives the URL, e.g. "/home"
    def decorator(func):            # Inner: receives the function being decorated
        routes[path] = func         # "path" is still visible here — a closure, as in Step B
        return func                 # Give the function back untouched
    return decorator                # Outer hands back the inner function

@route("/home")                     # Means: home = route("/home")(home)
def home():
    return "This is the home page"

@route("/about")
def about():
    return "This is the about page"

print(routes)                       # {'/home': <function home>, '/about': <function about>}
print(routes["/home"]())            # Look up the URL, then call the function it maps to
print(home())                       # The original function still works normally

# That dictionary lookup is, in essence, what a web framework does: read the
# requested URL, find the registered function, call it, send back the result.


# Step E: REPLACE vs. ADD — the key difference, side by side.
# Two decorators, two identical functions, opposite outcomes.

@shout                              # Replacing decorator: returns a NEW function
def hello_replaced(name):
    return f"Hello, {name}!"

@route("/hello")                    # Registering decorator: returns the ORIGINAL function
def hello_registered(name):
    return f"Hello, {name}!"

print(hello_replaced("Dave"))       # "HELLO, DAVE!" — changed; the plain greeting is gone
print(hello_registered("Dave"))     # "Hello, Dave!" — untouched, exactly as written
print(routes["/hello"]("Dave"))     # "Hello, Dave!" — and now reachable via its URL too

# hello_replaced LOST its original behaviour; hello_registered lost nothing and
# GAINED a URL. That is why Flask can decorate your view functions without ever
# changing what they do — @app.route only adds them to the URL table.


# ---------------------------------------------------------------------------
# 2. A MINIMAL FLASK APP
# ---------------------------------------------------------------------------
# Flask() creates the application object. "__name__" tells Flask where the app
# lives on disk, so it can find templates and static files relative to it.

print("\n--- 2. Creating the Flask app ---")

app = Flask(__name__)               # The application object — routes attach to this

@app.route("/")                     # Register index() for the URL "/"
def index():                        # The "view function" for this route
    return "Hello, Flask!"          # Returning a string sends it as the HTTP response body

print(f"App created: {app.name}")


# ---------------------------------------------------------------------------
# 3. MULTIPLE ROUTES
# ---------------------------------------------------------------------------
# Each route needs its own view function with a UNIQUE name. Flask uses the
# function name as the internal endpoint name, so duplicates raise an error.

@app.route("/about")
def about_page():                   # Not "about" — that name is already taken above
    return "This app is a Flask workshop."

@app.route("/contact")
def contact():
    return "Reach us at hello@example.com"

# One function can serve several URLs — just stack decorators on top of it.
@app.route("/help")
@app.route("/faq")                  # Both URLs call the same view function
def help_page():
    return "Help is on the way."


# ---------------------------------------------------------------------------
# 4. DYNAMIC ROUTES (URL VARIABLES)
# ---------------------------------------------------------------------------
# Angle brackets capture part of the URL and pass it to the view function as a
# keyword argument. The parameter name must match the name in the brackets.

@app.route("/user/<username>")              # /user/alice -> username = "alice"
def show_user(username):                    # Default converter is string
    return f"Profile page of {username}"

@app.route("/post/<int:post_id>")           # <int:...> converts to a real int
def show_post(post_id):                     # /post/abc returns 404 — it is not an int
    return f"Post number {post_id} (type: {type(post_id).__name__})"

@app.route("/price/<float:amount>")         # Other converters: float, path, uuid
def show_price(amount):                     # /price/10.50 works, /price/10 does NOT —
    return f"Price: {amount * 1.19:.2f} EUR including VAT"   # float requires a decimal point


# ---------------------------------------------------------------------------
# 5. QUERY PARAMETERS
# ---------------------------------------------------------------------------
# Everything after "?" in a URL is a query string. It is NOT part of the route
# pattern — read it from the request object instead.
# Try: /search?q=python&limit=5

@app.route("/search")
def search():
    query = request.args.get("q", "")           # .get() avoids a KeyError if missing
    limit = request.args.get("limit", 10, type=int)   # type= converts the string for you
    if not query:
        return "Add ?q=something to the URL"
    return f"Searching for '{query}', showing up to {limit} results"


# ---------------------------------------------------------------------------
# 6. HTTP METHODS
# ---------------------------------------------------------------------------
# By default a route only answers GET requests. Pass methods= to allow others.
# Test POST from a second terminal:
#   curl -X POST -d "name=Alice" http://127.0.0.1:5000/register

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":                # Same URL, different behaviour per method
        name = request.form.get("name", "anonymous")   # .form holds submitted form data
        return f"Registered {name}!"
    return """
        <form method="post">
            <input name="name" placeholder="Your name">
            <button type="submit">Register</button>
        </form>
    """


# ---------------------------------------------------------------------------
# 7. RETURNING JSON
# ---------------------------------------------------------------------------
# Return a dict or a list and Flask serialises it to JSON automatically,
# setting the Content-Type header to application/json.

@app.route("/api/status")
def api_status():
    return {"status": "ok", "version": "1.0"}   # Becomes a JSON response

@app.route("/api/users")
def api_users():
    return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]


# ---------------------------------------------------------------------------
# 8. HTML TEMPLATES
# ---------------------------------------------------------------------------
# Flask renders HTML with the Jinja2 template engine: {{ ... }} inserts a
# value, {% ... %} runs logic such as loops and conditions.
# Real projects use render_template("page.html") with files in a templates/
# folder; render_template_string keeps this tutorial in a single file.

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
    return render_template_string(PAGE, name=name, items=todo)  # Values passed as keywords


# ---------------------------------------------------------------------------
# 9. ERROR HANDLING
# ---------------------------------------------------------------------------
# @app.errorhandler is another decorator — same mechanism, different registry.
# Flask stores the function under the status code instead of under a URL.

@app.errorhandler(404)
def not_found(error):                       # Receives the error object
    return "Sorry, that page does not exist.", 404   # (body, status_code) tuple


# ---------------------------------------------------------------------------
# 10. PUTTING IT ALL TOGETHER — A SMALL TASK API
# ---------------------------------------------------------------------------
# An in-memory list of tasks with routes to list, view, and add them.
# The data disappears when the server restarts — that is fine for learning.

tasks = [
    {"id": 1, "title": "Learn Flask", "done": False},
    {"id": 2, "title": "Write a route", "done": True},
]

@app.route("/tasks")                            # List all tasks
def list_tasks():
    return {"tasks": tasks, "count": len(tasks)}

@app.route("/tasks/<int:task_id>")              # One task by id
def get_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"error": "Task not found"}, 404     # Tuple sets the HTTP status code

@app.route("/tasks", methods=["POST"])          # Same URL as list_tasks, different method
def add_task():
    title = request.form.get("title")
    if not title:
        return {"error": "title is required"}, 400
    new_task = {"id": max(t["id"] for t in tasks) + 1, "title": title, "done": False}
    tasks.append(new_task)
    return new_task, 201                        # 201 = Created


# ---------------------------------------------------------------------------
# 11. STARTING THE SERVER
# ---------------------------------------------------------------------------
# This guard means the server only starts when the file is run directly,
# not when it is imported by another module or by a production server.

if __name__ == "__main__":
    print("\n--- Starting server on http://127.0.0.1:5000 (Ctrl+C to stop) ---")
    print("Try: /  /about  /user/alice  /post/42  /price/10.50")
    print("     /search?q=flask  /welcome/bob  /api/status  /tasks  /tasks/1")
    app.run(debug=True)             # debug=True: auto-reload on save + error pages in the browser
