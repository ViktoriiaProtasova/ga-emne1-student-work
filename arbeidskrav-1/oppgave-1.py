# Oppgave 1.1 – Beregn tidsbruk

number_of_sessions = int(input("Enter number of sessions: "))
minutes_per_session = int(input("Enter minutes per session: "))

if number_of_sessions > 0 and minutes_per_session > 0:
    hours = number_of_sessions * minutes_per_session // 60
    minutes = number_of_sessions * minutes_per_session % 60

    print(f"Number of study sessions: {number_of_sessions}")
    print(f"Minutes per session: {minutes_per_session}")
    print(f"Total time: {hours} hours and {minutes} minutes")
else:
    print(f"Enter the correct value and try again")

#%% Oppgave 1.2 – Analyser tekst

text_string = input("Enter a text: ")


#%% Oppgave 1.3 – Analyser et tallintervall

start_value = float(input("Enter start value: "))
end_value = float(input("Enter end value: "))

start_value = int(start_value)
end_value = int(end_value)

if start_value > end_value:
    print(f"Start value must be greater than end value, try again")
else:
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

#%% Oppgave 1.4 – Lag en meny




