import mysql.connector
from mysql.connector import Error

city_name = input("Enter city name: ")

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
            sql = ("SELECT Name, Population, CountryCode "
                   "FROM city "
                   "WHERE Name = %s"
            )
            cursor.execute(sql, (city_name,))
            rows = cursor.fetchall()
            if not rows:
                print("No cities found.")
            else:
                for city, population, country in rows:
                    print(f"{city}, {population}, {country}")
except Error as e:
    print(f"Error using MySQL: {e}")