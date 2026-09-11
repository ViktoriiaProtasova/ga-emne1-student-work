#%% Oppgave 2.1: Beregn kostnaden for en kjøretur

distance = float(input("Enter mileage in kilometers: "))
fuel_per_100_km = float(input("Fuel consumption per 100 kilometers: "))
fuel_price = float(input("Fuel price per liter: "))
fuel_quantity = distance / 100 * fuel_per_100_km
fuel_total_cost = fuel_price * fuel_quantity
print(f"Total trip cost: {fuel_total_cost:.2f}")

#%% Oppgave 2.2: Regning med to tall

first_number = round(float(input("Enter first number: ")), 2)
second_number = round(float(input("Enter second number: ")), 2)
addition = first_number + second_number
difference = first_number - second_number
multiplication = first_number * second_number
if second_number == 0.0:
    print("You cannot divide to zero")
else:
    division = first_number / second_number
    integer_division = first_number // second_number
    remainder_of_division  = first_number % second_number
    print(f"Division: {division:.2f}")
    print(f"Integer division: {round(integer_division)}")
    print(f"Remainder: {remainder_of_division:.2f}")

print(f"Addition: {addition:.2f}")
print(f"Difference: {difference:.2f}")
print(f"Multiplication: {multiplication:.2f}")

#%% Oppgave 2.3: Potens og partall

integer = round(float(input("Enter integer: ")))
second_powers = integer ** 2
third_powers = integer ** 3
remainder = integer % 2

print(f"Integer is: {integer}")
print("Second powers: ", second_powers)
print("Third powers: ", third_powers)
print("Divided by 2: ", remainder)

if remainder == 0:
    print(f"The number is even")
else:
    print(f"The number is odd")



