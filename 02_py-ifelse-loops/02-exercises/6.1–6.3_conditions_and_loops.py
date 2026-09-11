#%% Oppgave 6.1: Tallundersøkelse

for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i}: Even")
    else:
        print(f"{i}: Odd")

#%% Oppgave 6.2: PIN-kode med begrenset antall forsøk

secret_pin = 2468
attempts_left = 3
is_authenticated = False

while attempts_left > 0:

    if not is_authenticated:
        pin_code = int(input("Enter pin code: "))

        if pin_code == secret_pin:
            is_authenticated = True
            print("Access granted")
            break
        else:
            attempts_left -= 1
            print(f"You have {attempts_left} attempts left")
    else:
        print("Access granted")
        break

if not is_authenticated:
    print("Access denied")

#%% Oppgave 6.3: Finn tall som oppfyller flere krav

counter = 0

for i in range(1, 101):

    if i % 3 == 0 and 20 < i < 80:
        counter += 1
        print(f"{i}")

print(f"Total: {counter}")