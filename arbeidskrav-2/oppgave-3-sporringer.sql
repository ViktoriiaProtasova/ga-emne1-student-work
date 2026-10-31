-- Task 3 – SELECT and data exploration

-- 1. Product Overview:

SELECT product_name, category, price, stock
FROM products
WHERE price > 750.00 AND stock >= 10
ORDER BY price DESC;

-- Finds products that cost over 750 NOK and have at least 10 units in stock.
-- Displays the product name, category, price, and quantity in stock.
-- Sorts from most expensive to least expensive.


-- 2. Customers in selected cities:

SELECT first_name, last_name, city
FROM customers
WHERE city IN ('Oslo', 'Bergen', 'Trondheim')
ORDER BY city, last_name;

-- Finds customers who live in Oslo, Bergen, or Trondheim.
-- Sorts first by city and then by last name.


-- 3. Orders within a period:

SELECT order_id AS order_number, order_date, quantity, status
FROM orders
WHERE order_date LIKE '2025-07-%';

-- Finds all orders registered in July 2025.
-- Displays the order number, date, quantity, and status.


-- 4. Complete order overview:

SELECT order_id AS order_number, first_name, last_name, product_name, quantity, price, order_date, status
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id;

-- Creates an overview that retrieves information from all three tables.
-- Displays the order number, the customer's first and last name,
-- product name, quantity, price per product, order date, and status.


-- 5. Calculated value:

SELECT order_id AS order_number, first_name, last_name, product_name, quantity, price,
       (quantity * price)AS total_price, order_date, status
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id
ORDER BY total_price DESC;

-- Expands the order overview to also show a calculated value based on price * quantity.
-- Gives the calculated column an appropriate name and sorts from highest to lowest value.


-- 6. High-value orders:

SELECT first_name, last_name, product_name, quantity, price,
       (quantity * price)AS total_price
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id
WHERE (quantity * price) > 2000.00;

-- Finds orders with an estimated value of more than 2,000 NOK.
-- Displays the customer, product, quantity, price, and estimated value.


-- 7. Orders by status:

SELECT status, COUNT(*) AS status_count
FROM orders
GROUP BY status;

-- Finds out how many orders have each status.


-- 8. Average price per category:

SELECT category, ROUND(AVG(price),2) AS average_price
FROM products
GROUP BY category
ORDER BY average_price DESC;

-- Find the average price for the products in each category.
-- Rounds average price to two decimal places.
-- Sort from highest to lowest average price.


-- 9. Orders per customer:

SELECT last_name, first_name,
       COUNT(order_id) AS total_orders
FROM customers
LEFT JOIN  orders ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id, last_name, first_name
ORDER BY total_orders DESC;

-- Determines how many orders each customer has placed.
-- Sorts the customers with the most orders first.
-- The result include also customers who have 0 orders.


-- 10. Number of products sold:

SELECT product_name,
       COALESCE(SUM(quantity), 0) AS products_sold
FROM products
LEFT JOIN orders ON products.product_id = orders.product_id
GROUP BY products.product_id, product_name;

-- Determines the total number of units ordered for each product.
-- Products that do not appear in any order are also included in the result, shown with 0 units ordered.
-- Counts total number of units ordered in the `orders` table.


-- 11. Estimated value per product:

SELECT product_name,
       COALESCE(SUM(quantity), 0) AS products_sold,
       COALESCE(SUM(quantity * price), 0) AS total_value
FROM products
LEFT JOIN orders ON products.product_id = orders.product_id
GROUP BY products.product_id, product_name
ORDER BY total_value DESC;

-- Determines the total estimated value for each product based on the orders.
-- Displays the product name, the total number of units ordered, and the total estimated value.
-- Products with no orders are also included, shown with 0 units ordered and an estimated value of 0.
-- Sorts from highest to lowest value.


-- 12. Customers with multiple orders:

SELECT last_name, first_name, COUNT(order_id) AS total_orders
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id, last_name, first_name
HAVING COUNT(order_id) > 1;

-- Finds customers who have more than one order.
-- Displays the customer and the number of orders.
-- Uses HAVING to filter grouped results.


-- 13. Customers without orders:

SELECT last_name, first_name
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id
WHERE order_id IS NULL;

-- Finds the customer or customers who have no orders.


-- 14. Products without orders:

SELECT product_name
FROM products
LEFT JOIN orders ON products.product_id = orders.product_id
WHERE orders.product_id IS NULL;

-- Finds the product or products that do not appear in any order.


-- 15. Exploration task:

SELECT last_name, first_name,
       SUM(COALESCE((quantity * price), 0)) AS total_value
FROM customers
LEFT JOIN  orders ON customers.customer_id = orders.customer_id
LEFT JOIN products ON orders.product_id = products.product_id
GROUP BY customers.customer_id, last_name, first_name
ORDER BY total_value DESC
LIMIT 1;


-- I joined the customers, orders, and products tables to obtain the quantity and price for each order.
-- Then, I calculated quantity * price for each order and aggregated these totals by customer using SUM and GROUP BY.
-- Finally, I sorted the results from highest to lowest value and used LIMIT 1
-- to isolate the customer with the highest total value.


-- Query written using AI (Claude):

SELECT last_name, first_name,
       SUM(COALESCE((quantity * price), 0)) AS total_value
FROM customers
         LEFT JOIN orders ON customers.customer_id = orders.customer_id
         LEFT JOIN products ON orders.product_id = products.product_id
GROUP BY customers.customer_id, last_name, first_name
HAVING SUM(COALESCE((quantity * price), 0)) = (
    SELECT MAX(total_value)
    FROM (
             SELECT SUM(COALESCE((quantity * price), 0)) AS total_value
             FROM customers
                      LEFT JOIN orders ON customers.customer_id = orders.customer_id
                      LEFT JOIN products ON orders.product_id = products.product_id
             GROUP BY customers.customer_id
         ) AS sums
)
ORDER BY last_name;

-- I calculate the total value for each customer by summing quantity * price over all their orders.
-- A subquery then finds the highest of these totals using MAX.
-- In the main query, HAVING keeps every customer whose total equals this highest value.
-- This way, if several customers have the same highest total, all of them are shown instead of only one.


-- Task 4 – INSERT, UPDATE, DELETE, and transactions

-- 1. Register a new customer:

INSERT INTO customers (first_name, last_name, email, city, registered_date)
VALUES ('Henrik', 'Solberg','henrik.solberg@example.com','Lillehammer', '2026-10-26');

SELECT first_name, last_name
FROM customers
WHERE email = 'henrik.solberg@example.com';

-- 2. Register multiple products:

INSERT INTO products (product_name, category, price, stock)
VALUES ('USB-C cable', 'Accessories', 199.00, 50),
       ('Docking station', 'Accessories', 1899.00, 12),
       ('External SSD 2TB', 'Storage', 1999.00, 8);

SELECT product_name
FROM products
WHERE product_name IN ('USB-C cable', 'Docking station', 'External SSD 2TB');

-- 3. Register new orders:

INSERT INTO orders (customer_id, product_id, quantity, order_date, status)
VALUES ((SELECT customer_id FROM customers WHERE email = 'henrik.solberg@example.com'),
        (SELECT product_id FROM products WHERE product_name = 'Docking station'), 1, '2026-10-26', 'Processing'),
       ((SELECT customer_id FROM customers WHERE email = 'henrik.solberg@example.com'),
        (SELECT product_id FROM products WHERE product_name = 'USB-C cable'), 2, '2026-10-26', 'Processing'),
       ((SELECT customer_id FROM customers WHERE email = 'henrik.solberg@example.com'),
        (SELECT product_id FROM products WHERE product_name = 'External SSD 2TB'), 1, '2026-10-26', 'Processing');

SELECT first_name, last_name, product_name
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id
WHERE order_date = '2026-10-26';


-- 4. Price change:

SELECT product_id, product_name, price, price * 1.08 AS new_price
FROM products
WHERE category = 'Accessories';

UPDATE products
SET price = ROUND((price * 1.08), 2)
WHERE category = 'Accessories';

SELECT product_id, product_name, price
FROM products
WHERE category = 'Accessories';


-- 5. Stock replenishment:

SELECT product_id, product_name, stock
FROM products
WHERE stock < 15;

UPDATE products
SET stock = stock + 20
WHERE stock < 15;

SELECT COUNT(product_id) AS product_count
FROM products
WHERE stock < 15;


-- 6. Modify multiple values:

SELECT product_name, price, price * 1.15 AS new_price, stock, stock + 10 AS new_stock
FROM products
WHERE product_name = 'Gaming headset';

UPDATE products
SET price = ROUND((price * 1.15), 2),
    stock = stock + 10
WHERE product_name = 'Gaming headset';

SELECT product_name, price, stock
FROM products
WHERE product_name = 'Gaming headset';


-- 7. Update order status:

SELECT order_id, order_date, status
FROM orders
WHERE status = 'Shipped' AND order_date < '2025-08-10';

UPDATE orders
SET status = 'Delivered'
WHERE status = 'Shipped' AND order_date < '2025-08-10';

SELECT order_id, order_date, status
FROM orders
WHERE status = 'Shipped' AND order_date < '2025-08-10';


-- 8. Create and delete test data:

-- Task 4 – INSERT, UPDATE, DELETE, and transactions

-- 1. Register a new customer:

INSERT INTO customers (first_name, last_name, email, city, registered_date)
VALUES ('Henrik', 'Solberg','henrik.solberg@example.com','Lillehammer', '2026-10-26');

SELECT first_name, last_name
FROM customers
WHERE email = 'henrik.solberg@example.com';

-- 2. Register multiple products:

INSERT INTO products (product_name, category, price, stock)
VALUES ('USB-C cable', 'Accessories', 199.00, 50),
       ('Docking station', 'Accessories', 1899.00, 12),
       ('External SSD 2TB', 'Storage', 1999.00, 8);

SELECT product_name
FROM products
WHERE product_name IN ('USB-C cable', 'Docking station', 'External SSD 2TB');

-- 3. Register new orders:

INSERT INTO orders (customer_id, product_id, quantity, order_date, status)
VALUES ((SELECT customer_id FROM customers WHERE email = 'henrik.solberg@example.com'),
        (SELECT product_id FROM products WHERE product_name = 'Docking station'), 1, '2026-10-26', 'Processing'),
       ((SELECT customer_id FROM customers WHERE email = 'henrik.solberg@example.com'),
        (SELECT product_id FROM products WHERE product_name = 'USB-C cable'), 2, '2026-10-26', 'Processing'),
       ((SELECT customer_id FROM customers WHERE email = 'henrik.solberg@example.com'),
        (SELECT product_id FROM products WHERE product_name = 'External SSD 2TB'), 1, '2026-10-26', 'Processing');

SELECT first_name, last_name, product_name
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id
WHERE order_date = '2026-10-26';


-- 4. Price change:

SELECT product_id, product_name, price, price * 1.08 AS new_price
FROM products
WHERE category = 'Accessories';

UPDATE products
SET price = ROUND((price * 1.08), 2)
WHERE category = 'Accessories';

SELECT product_id, product_name, price
FROM products
WHERE category = 'Accessories';


-- 5. Stock replenishment:

SELECT product_id, product_name, stock
FROM products
WHERE stock < 15;

UPDATE products
SET stock = stock + 20
WHERE stock < 15;

SELECT COUNT(product_id) AS product_count
FROM products
WHERE stock < 15;


-- 6. Modify multiple values:

SELECT product_name, price, price * 1.15 AS new_price, stock, stock + 10 AS new_stock
FROM products
WHERE product_name = 'Gaming headset';

UPDATE products
SET price = ROUND((price * 1.15), 2),
    stock = stock + 10
WHERE product_name = 'Gaming headset';

SELECT product_name, price, stock
FROM products
WHERE product_name = 'Gaming headset';


-- 7. Update order status:

SELECT order_id, order_date, status
FROM orders
WHERE status = 'Shipped' AND order_date < '2025-08-10';

UPDATE orders
SET status = 'Delivered'
WHERE status = 'Shipped' AND order_date < '2025-08-10';

SELECT order_id, order_date, status
FROM orders
WHERE status = 'Shipped' AND order_date < '2025-08-10';


-- 8. Create and delete test data:

INSERT INTO customers (first_name, last_name, email, city, registered_date)
VALUES ('test_first_name', 'test_last_name', 'test@example.com', 'Oslo', '2026-10-31');

INSERT INTO products (product_name, category, price, stock)
VALUES ('Test_product', 'Test_category', 99.90, 10);

INSERT INTO orders (customer_id, product_id, quantity, order_date, status)
VALUES ((SELECT customer_id FROM customers WHERE email = 'test@example.com'),
        (SELECT product_id FROM products WHERE product_name = 'Test_product'),
        1, '2026-10-31', 'Processing');

SELECT first_name, last_name, product_name, order_id, order_date, quantity, status
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
JOIN products ON products.product_id = orders.product_id
WHERE product_name = 'Test_product';

DELETE FROM orders
WHERE customer_id = (SELECT customer_id FROM customers WHERE email = 'test@example.com');

DELETE FROM products
WHERE product_name = 'Test_product';

DELETE FROM customers
WHERE email = 'test@example.com';

SELECT first_name, last_name
FROM customers
WHERE email ='test@example.com';

SELECT product_name
FROM products
WHERE product_name = 'Test_product';

-- I delete the test data in this order: first the order in orders,
-- then the test customer in customers and the test product in products (the last two can go in either order).

-- The reason is that orders has foreign keys to both customers and products.
-- The foreign keys protect referential integrity.
-- MySQL does not allow deleting a customer or product that is still referenced by an order,
-- because the order would then point to something that no longer exists.
-- If I try to delete the customer first, MySQL returns a foreign key constraint error.
-- So I must delete the “child” row (the order) before the “parent” rows (the customer and product).

-- The order of creation is the opposite: parent rows (customers, products) first, then orders.


-- 9. Use a transaction:

START TRANSACTION;

INSERT INTO orders(customer_id, product_id, quantity, order_date, status)
VALUES (1,1,2, '2026-10-31', 'Processing');

UPDATE products
SET stock = stock - (SELECT quantity FROM orders WHERE order_id = LAST_INSERT_ID())
WHERE product_id = (SELECT product_id FROM orders WHERE order_id = LAST_INSERT_ID());

SELECT first_name, last_name, product_name, order_id, order_date, quantity, status, stock
FROM customers
         JOIN orders ON customers.customer_id = orders.customer_id
         JOIN products ON products.product_id = orders.product_id
WHERE order_id = LAST_INSERT_ID();

COMMIT;

-- What would ROLLBACK do instead of COMMIT?
-- If I used ROLLBACK instead of COMMIT, all changes made inside the transaction would be undone.
-- The new order would not exist in orders, and the stock of the product would stay at its original value,
-- as if nothing had happened.

-- What would happen without a transaction?
-- If the INSERT succeeded but the UPDATE failed, the order would be registered,
-- but the stock would not be reduced.
-- The database would then be inconsistent: it would show more items in stock than actually exist.

-- Why are transactions useful?
-- Transactions are useful when several changes belong together,
-- because they follow the ACID principles of relational databases, especially atomicity.
-- Atomicity means that either the whole transaction is carried out or none of it is.
-- It cannot happen that the INSERT is saved while the following UPDATE is not. A transaction guarantees this.




