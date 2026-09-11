#%%  #13. Bygg en setning

adjective_1 = input("Please enter an adjective 1: ")
adjective_2 = input("Please enter an adjective 2: ")
noun = input("Please enter an noun: ")
verb = input("Please enter a verb: ")
print(f"{adjective_1.capitalize()} {adjective_2} {noun} {verb}." )

#%% #14. Enkel valutaomregning

amount = float(input("Please enter an amount: "))
exchange_rate = float(input("Please enter a course: "))
target_amount = amount * exchange_rate
print(f"{amount:.2f} × {exchange_rate} = {target_amount:.2f}")

#%% 15. Mini-prosjekt: totalpris

product_name = input("Please enter a product name: ")
unit_price = float(input("Please enter an unit price: "))
quantity = int(input("Please enter an quantity: "))
total_price = unit_price * quantity
print(f"Total price: {product_name} - {total_price:.2f}.")

#%% 16. Pris med rabatt

item_price = float(input("Please enter an item price: "))
discount = float(input("Please enter an discount: "))
discount_amount = item_price * discount / 100
discounted_price = item_price - discount_amount
print(f"The discounted price is {discounted_price:.2f}")
