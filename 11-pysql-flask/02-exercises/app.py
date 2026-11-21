from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    return render_template("index.html", heading="Hello from my app!")


@app.route("/about")
def about():
    return render_template(
        "about.html",
        heading="About this webpage",
        author="Viktoriia Protasova",
    )


@app.route("/greet")
def greet():
    name = request.args.get("name", "Guest").strip()

    if not name:
        name = "Guest"

    if name.isalpha():
        return render_template("greet.html", greeting=f"Hello, {name}!")
    else:
        return "Invalid name. Please enter letters only.", 400
