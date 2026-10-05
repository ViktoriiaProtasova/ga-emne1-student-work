temperatures = [-11, 2, -2, 4, 7, -1, 0]

for temp in temperatures:
    if temp < -10:
        print(f"{temp} degrees - Cold day!")
    else:
        print(f"{temp} degrees")

print(f"max = {max(temperatures)} degrees")
print(f"min = {min(temperatures)} degrees")
print(f"average = {(sum(temperatures) / len(temperatures)):.2f} degrees")

