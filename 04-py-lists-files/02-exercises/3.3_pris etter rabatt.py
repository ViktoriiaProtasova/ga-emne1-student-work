prices = [320.50, 256.99, 312.45, 687.00, 499.99]

print(f"{sum(prices):.2f}")

for price in prices:
    print(f"{(price - price * 0.2):.2f}")


