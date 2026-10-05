numbers = [10, 22, 35, 50, 75, 100, 23, 112, 7, 195, 78, 0, 1, -20, -50]

count = 0
for number in numbers:
    if number > 50:
        print(number)
        count += 1
        
print(count)