#%%
secret_number = 5
attempts_left = 5

while attempts_left > 0:
    attempts_left -= 1
    number = int(input("Guess the number: "))
    if number > secret_number:
       print("Too high")
    elif number < secret_number:
       print("Too low")
    else:
        print("You guessed right!")
        break
if attempts_left == 0:
    print("Game over!")

#%% Ekstra øvingsoppgave

attempts_left = 5
min_number = 1
max_number = 30
is_guessed = False

print("Guess the number (1-30)")

while attempts_left > 0:
    attempts_left -= 1

    mid_number = min_number + ((max_number - min_number) // 2)

    answer = input(f"Is your number {mid_number} H (higher), L (lower), C (correct): ").strip().lower()

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





