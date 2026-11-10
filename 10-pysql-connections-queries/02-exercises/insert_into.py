import  mysql.connector
from mysql.connector import Error

try:
    print("Connecting to the database...")
    with mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="gokstad",
            database='my_database'
    ) as connection:
        print("Connected to MySQL!")
        with connection.cursor() as cursor:
            sql ="""
    INSERT INTO products (
        name,
        price,
        stock
    )
    VALUES ('Laptop Pro 15',  12999.00, 8),
       ('Wireless mouse',  399.00, 45),
       ('Mechanical keyboard',  899.00, 22);
"""
            cursor.execute(sql)
            connection.commit()
except Error as e:
    print(f"Error using MySQL: {e}")
