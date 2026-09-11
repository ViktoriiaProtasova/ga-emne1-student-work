#%% Oppgave 3.1: Sammenlign med 10
from math import remainder

number = round(float(input("Enter integer: ")))
print(f"Integer is: {number}")

if number > 10:
    print("Number is greater than 10")
elif number < 10:
    print("Number is less than 10")
else:
    print("Number is equal to 10")

#%% Oppgave 3.2: Sammenlign to tall

first_number = round(float(input("Enter first number: ")), 2)
second_number = round(float(input("Enter second number: ")), 2)

if first_number > second_number:
    print("First number is greater than second number")
elif first_number < second_number:
    print("Secund number is greater than first number")
else:
    print("First number is equal to second number")

#%% Oppgave 3.3: Positivt, negativt eller null

number =round(float(input("Enter a number: ")))
print(f"Integer is: {number}")

remainder = number % 2

if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is zero")

if remainder == 0 and number != 0:
    print("Number is even")
elif remainder != 0 and number != 0:
    print("Number is odd")

#%% Oppgave 3.4: Beregn fraktkostnad

package_weight = int(input("Enter package weight, kg: "))

if package_weight <= 2:
    print("Package costs 79 kroner")
elif package_weight <= 5:
    print("Package costs 129 kroner")
elif package_weight <= 10:
    print("Package costs 199 kroner")
else:
    print("Packages over 10 kg cannot be sent with the service")

#%% Oppgave 3.5: Tilgang til et spill

has_username = True
accepted_rules = True
is_blocked = False

if has_username and accepted_rules and not is_blocked:
    print("Access allowed")
else:
    print("Access denied")

#%% Oppgave 3.6: Gratis levering

order_amount = 650
is_member = True

if is_member or order_amount >= 800:
    print("The customer receives free delivery")
else:
    print("The customer does not receive free delivery")