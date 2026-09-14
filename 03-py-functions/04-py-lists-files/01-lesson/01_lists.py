guests = ["Kermit", "Miss Piggy", "Gonzo"]

print("\n---\n")

mixed_bag = ["Tomas" , 52, True]
print(mixed_bag)



print(guests[0])
print(guests[1])
print(guests[-1])

guests.append("Animal")
guests.remove("Kermit")
print(guests)
print(len(guests))

guests.insert(1, "Gonzo")

print("\n---\n")

for guest in guests:
    print(f"Hello, {guest}!")

print("\n---\n")

scores = [72,88,91,65]
print(len(scores))
print(sum(scores))

average = sum(scores) / len(scores)
print(f"Average: {average:.2f}")

print(max(scores))
print(min(scores))