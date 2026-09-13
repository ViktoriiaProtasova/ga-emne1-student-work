# Oppgave 1.1 – Beregn tidsbruk

while True:
    try:
        number_of_sessions = int(input("Enter number of sessions: "))
        if number_of_sessions > 0:
            break
        else:
            print("Invalid input. Please enter a positive whole number. Try again.")
    except ValueError:
        print("Invalid input. Please enter a positive whole number. Try again.")

while True:
    try:
        minutes_per_session = int(input("Enter minutes per session: "))
        if minutes_per_session > 0:
            break
        else:
            print("Invalid input. Please enter a positive whole number. Try again.")
    except ValueError:
        print("Invalid input. Please enter a positive whole number. Try again.")

hours = number_of_sessions * minutes_per_session // 60
minutes = number_of_sessions * minutes_per_session % 60

print(f"Number of study sessions: {number_of_sessions}")
print(f"Minutes per session: {minutes_per_session}")
print(f"Total time spent: {hours} hours and {minutes} minutes")



