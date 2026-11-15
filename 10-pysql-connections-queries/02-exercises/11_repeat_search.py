import mysql.connector
from mysql.connector import Error

def language_search(country_code):
    try:
        print("Connecting to the database...")
        with mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="gokstad",
                database="world"
        ) as connection:
            print("Connected to MySQL!")
            with connection.cursor() as cursor:
                sql = ("SELECT Language, Percentage,  IsOfficial "
                       "FROM countrylanguage "
                       "WHERE CountryCode = %s "
                       "ORDER BY Language"
                       )
                cursor.execute(sql, (country_code,))
                rows = cursor.fetchall()
                if not rows:
                    print("No countries found.")
                else:
                    for language, percentage, isofficial in rows:
                        print(f"{language}: {percentage}% - {isofficial}")
    except Error as e:
        print(f"Error using MySQL: {e}")

while True:
    country_code = input("Enter country code: ")
    if country_code == '':
        print("Done!")
        break
    else:
        language_search(country_code)




