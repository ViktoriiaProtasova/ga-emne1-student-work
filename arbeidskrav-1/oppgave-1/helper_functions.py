def calculate_time():
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




def analyze_text():
    while True:
        text_string = input("Enter a text: ")
        if text_string == "" or text_string.isspace():
            print("Invalid input. Please enter a text")
        else:
            break

    text_string_without_spaces = text_string.count(" ")

    print(f"The number of characters with spaces: {len(text_string)}")
    print(f"The number of characters without spaces: {len(text_string) - text_string_without_spaces}")
    print(f"The text in lowercase: {text_string.lower()}")
    print(f"The text reversed: {text_string[::-1]}")

    if "python" in text_string.lower():
        print(f'The text contains word "python"')
    else:
        print(f'The text does not contain the word "python"')



def analyze_interval():
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
                print(f"Start value must be less than end value, try again")
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

