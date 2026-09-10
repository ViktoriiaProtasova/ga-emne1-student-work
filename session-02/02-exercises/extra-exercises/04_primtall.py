#%% Utfordring 4: Primtall

number = int(input("Enter a positive integer: "))

is_prime = True

if number == 1:
    is_prime = False
else:
    for i in range(2, number):

        if number % i == 0:
            is_prime = False

if is_prime:
    print(f"The number {number} is a prime number")
else:
    print(f"The number {number} is not a prime number")