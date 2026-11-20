import mysql.connector
import logging

# Konfigurer logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='myapp.log'  # Skriv til fil (utelat for konsolloutput)
)


def add_student(name, age, email, db_config):
    """
       Legg til en ny student i databasen.
       Returnerer en tuppel (melding, suksess).
    """

    # Validering av brukerdata

    try:
        if not name or not email:
            raise ValueError("Navn og e-post kan ikke være tomme")

        try:
            age = int(age)
        except (ValueError, TypeError):
            raise ValueError("Alder må være et heltall")

    except ValueError as err:
        logging.warning(f"Valideringsfeil: {err}")
        return str(err), False

    # Databaseoperasjon

    try:
        with mysql.connector.connect(**db_config) as con:
            with con.cursor() as cur:
                sql = "INSERT INTO students (name, age, email) VALUES (%s, %s, %s)"
                cur.execute(sql, (name, age, email))
            con.commit()
            logging.info("Student added successfully")
            return "Studenten ble lagt til", True


    except mysql.connector.IntegrityError as err:
        logging.error(f"MySQL-feil kode {err.errno}: {err.msg}")

        if err.errno == 1062:
            return "Duplikatverdi: Kontroller e-postadressen", False

        return "Kunne ikke lagre studenten", False

    except mysql.connector.OperationalError as err:
        # Tilkoblingsproblem
        logging.error(f"MySQL-feil kode {err.errno}: {err.msg}")
        return "Kunne ikke koble til databasen", False


    except mysql.connector.Error as err:
        logging.error(f"Databasefeil: {err}")
        return "En databasefeil oppstod", False
