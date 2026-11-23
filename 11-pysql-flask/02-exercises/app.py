from flask import Flask, render_template, request
from mysql.connector import Error

from database import get_cities

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


@app.route("/cities")
def cities():
    code = request.args.get("country", "NOR").strip().upper()
    if len(code) != 3 or not code.isascii() or not code.isalpha():
        return "Invalid code", 400
    try:
        rows = get_cities(code)
    except Error:
        app.logger.exception("Database query failed")
        return "Database unavailable", 503
    return render_template(
        "cities.html", code=code, rows=rows, count=len(rows)
    )


# 1. Endre filnavnet til cities.html

#   Jeg prøvde å endre filnavnet, men PyCharm viste en advarsel om refaktorering
#   fordi filen brukes andre steder i prosjektet.
#   Jeg valgte «Cancel» for å unngå feil.
#   Dermed trengte jeg ikke å få feilmeldingen TemplateNotFound.

# 2. Feil antall verdier i Jinja-løkken

#   Jeg fikk feilmeldingen ValueError: too many values to unpack.
#   Jeg rettet Jinja-løkken i cities.html slik at den pakket ut tre verdier.

# 3. Endre action til /city

#   Jeg fikk feilmeldingen 404 Not Found i nettleseren.
#   Jeg rettet action i HTML-filen tilbake til den riktige ruten.

#   Resultat: Etter retting fungerte appen som normalt.
