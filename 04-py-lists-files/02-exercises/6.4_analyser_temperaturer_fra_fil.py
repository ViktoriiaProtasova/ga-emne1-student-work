from pathlib import Path

file_path = Path("..") / "data" / "temperatures.txt"

temperatures_list = []

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        temperatures_list.append(float(line))

print(temperatures_list)
print(len(temperatures_list))
print(min(temperatures_list))
print(max(temperatures_list))

print(f"{sum(temperatures_list) / len(temperatures_list):.2f}")