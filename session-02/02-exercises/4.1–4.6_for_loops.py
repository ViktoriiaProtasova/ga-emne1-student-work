#%% Oppgave 4.1: Tell oppover
print("loop for the serie 0-9:")
for i in range(10):
    print(i)

print("loop for the serie 5-15:")
for i in range(5, 16):
    print(i)

print("loop for the serie 1-20:")
for i in range(1, 21):
    print(i)

#%% Oppgave 4.2: Partall og oddetall

print("loop for the even numbers from 2 to 20:")
for i in range(2, 21, 2):
    print(i)

print("loop for the odd numbers from 1 to 19:")
for i in range(1, 20, 2):
    print(i)

#%% Oppgave 4.3: Tell nedover

print("loop for numbers from 30 to 10:")
for i in range(30, 9, -1):
    print(i)

print("loop for all odd numbers from 29 to 11:")
for i in range(29, 10, -2):
    print(i)

#%% Oppgave 4.4: Summer tall

total = 0
for i in range(1, 11):
    total += i
    print(i)
    print("running total: ", total)
print("Total: ", total)

#%% Oppgave 4.5: Summer tall med bestemte steg

print("Sum the 3-times table from 3 to 30:")

total_3_30 = 0

for i in range(3, 31, 3):
    total_3_30 += i
    print(i)
    print("running total: ", total_3_30)
print("Total: ", total_3_30)

print("Sum the 5-times table from 5 to 50:")

total_5_50 = 0

for i in range(5, 51, 5):
    total_5_50 += i
    print(i)
    print("running total: ", total_5_50)
print("Total: ", total_5_50)

#%% Oppgave 4.6: Gangetabell

number = int(input("Enter integer (1-10): "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
