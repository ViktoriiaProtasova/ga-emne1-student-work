import mysql.connector
from mysql.connector import Error

def get_products_under_price():
    max_price = 0.00
    is_number_correct = False

    while not is_number_correct:
        try:
            max_price = float(input('Write max price: '))
            is_number_correct = True
        except ValueError:
            print('Write a correct price: ')

    with mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="gokstad",
            database='my_database'
    ) as connection:
        print("Connected to MySQL!")
        with connection.cursor() as cursor:
            sql = ("SELECT name, price, stock "
                   "FROM products "
                   "WHERE price < %s"
            )
            cursor.execute(sql, (max_price,))
            rows = cursor.fetchall()
            if not rows:
                print("No products found.")
            else:
                for name, price, stock in rows:
                    print(f"{name}, {price}, {stock}")


try:
    get_products_under_price()
except Error as e:
    print(f"Error using MySQL: {e}")
