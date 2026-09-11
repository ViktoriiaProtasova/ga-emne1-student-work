purchase_amount = float(input("Enter purchase amount: "))

if purchase_amount >= 1000:
    print(f"Final price: {purchase_amount * 0.8:.2f}")
elif purchase_amount >= 500:
    print(f"Final price: {purchase_amount * 0.9:.2f}")
else :
    print(f"Final price: {purchase_amount:.2f}")
print("Tanks!")