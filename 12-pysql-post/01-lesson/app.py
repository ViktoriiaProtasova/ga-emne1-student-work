from flask import Flask, request, render_template, redirect
from mysql.connector import Error

import database

# from database import *

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    return render_template(
        "index.html",
        heading="Lesson 12: World exploring",
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
        rows = database.get_cities(code)
    except Error:
        app.logger.exception("Database query failed")
        return "Database unavailable", 503
    return render_template("cities.html", code=code, rows=rows)


@app.route("/city/<int:city_id>")
def show_city(city_id):
    city = database.get_city(city_id)
    if city is None:
        return "City not found", 404
    return render_template("city_form.html", name=city.name, city_id=city.id)


@app.route("/add", methods=["GET", "POST"])
def add_city():
    # Uses GET to open input field page:

    if request.method == "GET":
        return render_template("city_form.html", name="", city_id=None)

    # Uses POST to store city data in DB:

    name = request.form.get("name", "").strip()
    if not name or len(name) > 35:
        # return "Invalid city name", 400
        return redirect("https://http.cat/400", code=400)

    database.insert_city(name)
    return redirect("/cities", code=303)


@app.route("/edit/<int:city_id>", methods=["POST"])
def edit_city(city_id):
    name = request.form.get("name", "").strip()
    if not name or len(name) > 35:
        return "Invalid city name", 400
    database.update_city(city_id, name)
    return redirect("/cities", code=303)


@app.route("/delete/<int:city_id>", methods=["POST"])
def remove_city(city_id):
    database.delete_city(city_id)
    return redirect("/cities", code=303)
