from pathlib import Path

data_folder = Path(__file__).parent.parent / "data"
path = data_folder / "message.txt"

print(path)

try:
    with path.open(encoding="utf-8") as file:
        message = file.read()
        print(message)
except FileNotFoundError:
    print(f"Error. File not found: {path} ")



path = data_folder / "number.txt"

print(path)

try:
    with path.open(encoding="utf-8") as file:
        number = int(file.read())
        print(number*2)
except FileNotFoundError:
    print(f"Error. File not found: {path} ")
except ValueError:
    print(f"Error. The file must contain an integer.")



