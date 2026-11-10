import mysql.connector
from mysql.connector import Error

def add_product(name, price, stock):

    with mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="gokstad",
            database='my_database'
    ) as connection:
        print("Connected to MySQL!")
        with connection.cursor() as cursor:
            print(cursor.rowcount)
            sql = ("INSERT INTO products (name, price, stock)"
                   "VALUES (%s, %s, %s)")
            cursor.execute(sql, (name, price, stock,))
            connection.commit()
            print(cursor.rowcount)

try:
    add_product('24-inch monitor', 2299.00, 10)
except Error as e:
    print(f"Error using MySQL: {e}")
