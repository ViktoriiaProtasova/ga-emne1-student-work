#%% Utfordring 6: Maskinen gjetter tallet ditt

attempts = 5
min_number = 1
max_number = 30
is_guessed = False

print(input("Guess the number (1-30): ok?"))

# noinspection DuplicatedCode
while attempts > 0:
    attempts -= 1

    mid_number = min_number + ((max_number - min_number) // 2)

    answer = input(f"Is your number {mid_number}? H (higher), L (lower), C (correct): ").strip().lower()

    if answer == "h":
        min_number = mid_number + 1
    elif answer == "l":
        max_number = mid_number - 1
    elif answer == "c":
        print("I guessed right!")
        is_guessed = True
        break

if not is_guessed:
    print("Game over!")