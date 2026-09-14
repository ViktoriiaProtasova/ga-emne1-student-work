def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

for i in range(1, 11):
    print(f"{i}-{is_even(i)}")


