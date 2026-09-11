#%% Kalkulator med meny

menu_item = 0

while menu_item != 5:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    menu_item = int(input("Enter an item: "))

    if menu_item == 5:
        print("Exit")
        break
    elif menu_item < 1 or menu_item > 5:
        continue
    else:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter first number: "))

    if menu_item == 1:
        print(f"Calculation result: {(first_number + second_number):.2f}")
    elif menu_item == 2:
        print(f"Calculation result: {(first_number - second_number):.2f}")
    elif menu_item == 3:
        print(f"Calculation result: {(first_number * second_number):.2f}")
    elif menu_item == 4:
        if second_number == 0.0:
            print("You cannot divide by zero!")
        else:
            print(f"Calculation result: {(first_number / second_number):.2f}")