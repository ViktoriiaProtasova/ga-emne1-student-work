#%% Utfordring 2: FizzBuzz

for i in range(1, 31):
    if i % 5 == 0 and i % 3 == 0:
        print(f"{i}: FizzBuzz")
    elif i % 3 == 0:
        print(f"{i}: Fizz")
    elif i % 5 == 0:
        print(f"{i}: Buzz")
    else:
        print(f"{i}: Otherwise")