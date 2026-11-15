import mysql.connector
from mysql.connector import Error

#region = input("Enter region: ")
# Unsafe: input becomes part of the SQL
# sql = ( "SELECT Name, Population FROM country "
# f"WHERE Region = '{region}'" )
# cursor.execute(sql)

region = input("Enter region: ")

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
                   "ORDER BY Name"
            )
            cursor.execute(sql, (region,))
            rows = cursor.fetchall()
            if not rows:
                print("No countries found.")
            else:
                for name, population in rows:
                    print(f"{name}: {population}")
except Error as e:
    print(f"Error using MySQL: {e}")