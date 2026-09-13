# Oppgave 1.4 – Lag en meny

from helper_functions import *

menu_item = 0

while menu_item != 4:
    print("1. Calculate time spent\n"
          "2. Analyze text\n"
          "3. Analyze numerical range\n"
          "4. Exit")
    try:
        menu_item = int(input("Enter menu option: "))
        if menu_item == 4:
            print("Exiting...")
            break
        elif menu_item == 1:
            print("Calculating time...")
            calculate_time()  # Calculate time spent
        elif menu_item == 2:
            print("Analyzing text...")
            analyze_text()  # Analyze text
        elif menu_item == 3:
            print("Analyzing numerical range...")
            analyze_interval()  # Analyze numerical range
        else:
            print("Invalid input. Please enter a valid menu option. Try again.")
    except ValueError:
        print("Invalid input. Please enter a valid menu option. Try again.")