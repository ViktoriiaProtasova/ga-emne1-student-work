import mysql.connector
from mysql.connector import Error

try:
    print("Connecting to the database...")
    with mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="gokstad"
    ) as connection:
        print("Connected to MySQL!")
        with connection.cursor() as cursor:
            sql_db = "CREATE DATABASE IF NOT EXISTS my_database"
            cursor.execute(sql_db)
            print("my_database was created")
            cursor.execute("USE my_database")
            sql_table ="""
    CREATE TABLE IF NOT EXISTS products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        price DECIMAL(10,2),
        stock INT
    )
"""
            cursor.execute(sql_table)

except Error as e:
    print(f"Error using MySQL: {e}")
