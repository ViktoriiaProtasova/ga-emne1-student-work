from flask import Flask, request, render_template, redirect
from mysql.connector import Error

import database
from models import City

# from database import *

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    return render_template(
        "index.html",
        heading="Lesson 13: World exploring",
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
    return render_template(
        "city_form.html",
        name=city.name,
        city_id=city.id,
        country_code=city.country_code,
        district=city.district,
        population=city.population,
    )


@app.route("/add", methods=["GET", "POST"])
def add_city():
    # Uses GET to open input field page:

    if request.method == "GET":
        return render_template("city_form.html", name="", city_id=None)

    # Uses POST to store city data in DB:

    form = request.form
    errors = {}
    data = {}

    try:
        data["name"] = City.clean_name(form.get("name", ""))
    except ValueError as error:
        errors["name"] = str(error)

    try:
        data["country_code"] = City.clean_country_code(
            form.get("country_code", "")
        )

        if not database.country_exists(data["country_code"]):
            raise ValueError("Country code does not exist.")

    except ValueError as error:
        errors["country_code"] = str(error)

    try:
        data["district"] = City.clean_district(form.get("district", ""))
    except ValueError as error:
        errors["district"] = str(error)

    try:
        data["population"] = City.clean_population(form.get("population", ""))
    except ValueError as error:
        errors["population"] = str(error)

    if errors:
        return (
            render_template(
                "city_form.html", **form, city_id=None, errors=errors
            ),
            400,
        )

    database.insert_city(**data)
    return redirect(f"/cities?country={data['country_code']}", code=303)


@app.route("/edit/<int:city_id>", methods=["POST"])
def edit_city(city_id):

    form = request.form
    errors = {}
    data = {}

    try:
        data["name"] = City.clean_name(form.get("name", ""))
    except ValueError as error:
        errors["name"] = str(error)

    try:
        data["country_code"] = City.clean_country_code(
            form.get("country_code", "")
        )

        if not database.country_exists(data["country_code"]):
            raise ValueError("Country code does not exist.")

    except ValueError as error:
        errors["country_code"] = str(error)

    try:
        data["district"] = City.clean_district(form.get("district", ""))
    except ValueError as error:
        errors["district"] = str(error)

    try:
        data["population"] = City.clean_population(form.get("population", ""))
    except ValueError as error:
        errors["population"] = str(error)

    if errors:
        return (
            render_template(
                "city_form.html", **form, city_id=city_id, errors=errors
            ),
            400,
        )

    database.update_city(city_id, **data)
    return redirect(f"/cities?country={data['country_code']}", code=303)


@app.route("/delete/<int:city_id>", methods=["POST"])
def remove_city(city_id):
    city = database.get_city(city_id)

    if city is None:
        return "City not found", 404

    country_code = city.country_code
    database.delete_city(city_id)

    return redirect(f"/cities?country={country_code}", code=303)
