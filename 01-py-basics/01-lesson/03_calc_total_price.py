product_name = input("Product name: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))
total_price = price * quantity

print(f"{product_name}: {total_price:.2f}kr.")
