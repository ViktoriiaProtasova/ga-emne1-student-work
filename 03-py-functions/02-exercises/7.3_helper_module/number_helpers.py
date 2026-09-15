def is_even(number):
    """Sjekker om tallet er partall og skriver ut resultatet."""
    if number % 2 == 0:
        print("True")
    else:
        print("False")



def find_largest(first_number, second_number):
    """Sammenligner to tall og skriver ut hvilket som er størst."""
    if first_number > second_number:
        print(f"{first_number} is largest")
    elif first_number < second_number:
        print(f"{second_number} is largest")
    else:
        print("Numbers are equal")