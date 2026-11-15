import mysql.connector
from mysql.connector import Error


region = input("Enter region: ")

is_int = False

while not is_int:
    try:
        min_population = int(input("Enter population size: "))
        if min_population >= 0:
            is_int = True
        else:
            print('The population size must be a positive number.')
    except:
        print('The population size must be a number.')

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
            sql = ("SELECT Name, Population "
                   "FROM country "
                   "WHERE Region = %s "
                   "AND Population >= %s "
                   "ORDER BY Name"
            )
            cursor.execute(sql, (region, min_population,))
            rows = cursor.fetchall()
            if not rows:
                print("No countries found.")
            else:
                for name, population in rows:
                    print(f"{name}: {population}")
except Error as e:
    print(f"Error using MySQL: {e}")