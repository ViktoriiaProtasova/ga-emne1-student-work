-- Oppgave 3 – SELECT og utforsking av data

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


