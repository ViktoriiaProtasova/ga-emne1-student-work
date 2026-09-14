def read_number():
    return int(input("Enter a number: "))

def describe_sign(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def show_analysis(number, sign, even):
    print(f"Number: {number}\n"
          f"Sign: {sign}\n"
          f"Even: {even}")

def run_number_analyzer():
    number = read_number()
    show_analysis(number, describe_sign(number), is_even(number))

run_number_analyzer()
