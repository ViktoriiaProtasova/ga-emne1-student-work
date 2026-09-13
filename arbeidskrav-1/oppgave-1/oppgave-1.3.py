# Oppgave 1.3 – Analyser et tallintervall

while True:
    try:
        start_value = int(input("Enter start value: "))
        break
    except ValueError:
        print("Invalid input. Please enter a positive whole number. Try again.")

while True:
    try:
        end_value = int(input("Enter end value: "))
        if start_value > end_value:
            print(f"Start value must be less than end value. Try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a positive whole number. Try again.")

total = 0

for i in range(start_value, end_value + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(f"{i} - even / divisible by 3")
    elif i % 2 == 0:
        print(f"{i} - even")
    elif i % 3 == 0:
        print(f"{i} - divisible by 3")
    total += i

print(f"Sum of all numbers in the range: {total}")