is_input_valid = False
age = 0

while not is_input_valid:
    try:
        age = int(input("Enter your age: "))
        is_input_valid = True
    except ValueError:
        print("Error. Just integer is valid.")

print(f"Next year {age + 1}")
