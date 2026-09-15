import random

def roll_die(sides = 6):
    for i in range(1, 11):
        print(f"{i} - Roll: {random.randint(1, sides)}")

roll_die()
roll_die(20)