#%%
number_of_tickets = int(input("How many tickets? "))
tickets_price = 180
service_fee = 35
subtotal = tickets_price * number_of_tickets
total = subtotal + service_fee
price_per_person = total / number_of_tickets
print(f"Total costnad: {total:.2f}")
print(f"Price per person: {price_per_person:.2f}")

#%%

total_costnad = float(input("Total costnad: "))
antal_personer = int(input("Antal: "))
costnad_per_person = total_costnad / antal_personer
print(f"Costnad per person: {costnad_per_person:.2f}")