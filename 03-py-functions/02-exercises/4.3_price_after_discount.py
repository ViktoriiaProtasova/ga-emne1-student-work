def calculate_discounted_price(price, discount_percent):
    return price - (price * discount_percent / 100)

discounted_price = calculate_discounted_price(100, 10)
print(f"Discounted price: {discounted_price:.2f}")

