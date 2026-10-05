from pathlib import Path

file_path = Path("..") / "data" / "shopping_list.txt"

handle_list = []

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        handle_list.append(line.strip())

print(handle_list)

with open(file_path, "r", encoding="utf-8") as file:
    print([line.strip() for line in file.readlines()])


with open(file_path, "r", encoding="utf-8") as file:
    print("The shopping list:")
    for number, line in enumerate(file, start=1):
        print(f"{number} {line.strip()}")

