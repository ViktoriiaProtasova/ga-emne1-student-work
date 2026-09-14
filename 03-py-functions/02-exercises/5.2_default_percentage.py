def calculate_tip(amount, tip_percent = 0):
    tip_amount = amount * tip_percent / 100
    print(f"Tip amount: ${tip_amount:.2f}")

calculate_tip(50, 10)
calculate_tip(100, 15)
calculate_tip(15, 5)
calculate_tip(20)

