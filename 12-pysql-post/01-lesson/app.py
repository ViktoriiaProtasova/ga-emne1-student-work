from flask import Flask, request
from flask import render_template
from mysql.connector import Error

from database import get_cities

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    return render_template(
        "index.html",
        heading="World exploring Jinja",
    )


@app.route("/about")
def about():
    return render_template(
        "about.html",
        heading="About this webpage",
        author="Viktoriia Protasova",
    )


@app.route("/cities")
def cities():
    code = request.args.get("country", "NOR").strip().upper()
    if len(code) != 3 or not code.isascii() or not code.isalpha():
        return "Invalid code", 400

    # Query DB & return result.

    try:
        rows = get_cities(code)
    except Error:
        app.logger.exception("Database query failed")
        return "Database unavailable", 503
    return render_template("cities.html", code=code, rows=rows)
