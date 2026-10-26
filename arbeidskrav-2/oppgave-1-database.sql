-- Task 1 – Create the database and the tables

DROP DATABASE IF EXISTS nettbutikk;

CREATE DATABASE nettbutikk;

USE nettbutikk;

CREATE TABLE customers(
    customer_id INT AUTO_INCREMENT NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    registered_date DATE NOT NULL,
    PRIMARY KEY (customer_id),
    UNIQUE (email)
);

CREATE TABLE products(
    product_id INT AUTO_INCREMENT NOT NULL,
    product_name VARCHAR(50) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
    PRIMARY KEY (product_id)
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT NOT NULL,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    order_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL,
    PRIMARY KEY (order_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

SELECT DATABASE();
SHOW TABLES;
DESCRIBE customers;
DESCRIBE products;
DESCRIBE orders;