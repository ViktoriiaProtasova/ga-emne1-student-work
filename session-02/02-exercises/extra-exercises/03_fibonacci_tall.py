#%% Utfordring 3: Fibonacci-tall

limit = int(input("Enter limit: "))

a = 0
b = 1

if limit <= 0:
    print("Limit must be greater than 0")
else:
    print(b)

    while True:
        c = a + b
        if c > limit:
            break
        print(c)
        a = b
        b = c