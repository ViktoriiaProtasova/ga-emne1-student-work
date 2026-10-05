scores = list((1,2,3,4,5,6))

print(scores)

count = len(scores)
total = sum(scores)
lowest = min(scores)
highest = max(scores)
average = total / count

print(count, total, lowest, highest, f"{average:.2f}")