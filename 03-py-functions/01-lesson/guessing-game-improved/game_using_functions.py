import random
from game_helpers import *


def play_guessing_game():
    secret_number = random.randint(1, 30)
    result = ""
    attempts = 5

    while attempts > 0:
        guess = read_guess()
        result = check_guess(guess, secret_number)
        show_feedback(result)
        attempts -= 1

        if result == "correct":
            break


    if attempts == 0:
        print("Game Over")

play_guessing_game()

