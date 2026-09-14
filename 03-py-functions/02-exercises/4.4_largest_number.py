def find_largest(first_number, second_number):
    if first_number > second_number:
        return first_number
    elif first_number < second_number:
        return second_number
    else:
        return "Numbers are equal"

print(find_largest(5, 6))
print(find_largest(0, 0))