#%% Stein, saks, papir
import random

print("Rock, paper, scissors Game:")

round_number = 1
player_score = 0
computer_score = 0

while round_number <= 10:

    print(f"Round {round_number}:")
    print("0. - rock")
    print("1. - scissor")
    print("2. - paper")

    player_number = int(input("Enter your choice: "))
    computer_number = random.randint(0, 2)

    if player_number < 0 or player_number > 2:
        print("Make a correct choice")
        continue

    player_choice = ""
    computer_choice = ""

    if player_number == 0:
       player_choice = "rock"
    elif player_number == 1:
        player_choice = "scissor"
    else:
        player_choice = "paper"

    if computer_number == 0:
       computer_choice = "rock"
    elif computer_number == 1:
        computer_choice = "scissor"
    else:
        computer_choice = "paper"


    print(f"Player choice: {player_choice}")
    print(f"Computer choice: {computer_choice}")

    if player_number == computer_number:
        print("It's a tie!")
    elif player_number == 0 and computer_number == 1:
        print("Player wins!")
        player_score += 1
    elif player_number == 1 and computer_number == 2:
        print("Player wins!")
        player_score += 1
    elif player_number == 2 and computer_number == 0:
        print("Player wins!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    round_number += 1

if player_score == computer_score:
    print("It's a tie!")
elif player_score > computer_score:
    print(f"Player's score: {player_score} - Player wins the Game!")
else:
    print(f"Computer's score: {computer_score} - Computer wins the Game!")