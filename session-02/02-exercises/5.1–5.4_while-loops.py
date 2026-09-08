#%% Oppgave 5.1: Tell oppover

number = 1

while number <= 10:
    print(number)
    number += 1
print("Finished")

#%% Oppgave 5.2: Tell nedover

number = 30
while number >= 10:
    print(number)
    number -= 1
print("Finished")

#%% Oppgave 5.3: Kvadrattall

limit = int(input("Enter an upper limit: "))

number = 1
square = number ** 2

while limit >= square:
    print(square)
    number += 1
print("Finished")

#%% Oppgave 5.4: Be om et gyldig tall

integer = 0

while integer <= 0:
    integer = int(input("Enter a positive integer: "))
    if integer <= 0:
        continue
    else:
        print(f"You entered {integer}")
    break




