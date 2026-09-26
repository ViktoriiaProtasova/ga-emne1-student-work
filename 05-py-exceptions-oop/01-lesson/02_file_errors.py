from pathlib import Path
data_folder = Path(__file__).parent.parent / "data"
path = data_folder / "messae.txt"

print(path)

try:
    with path.open(encoding="utf-8") as file:
        message = file.read()
        print(message)
except FileNotFoundError:
    print(f"Error: f"
          f"ile {path} not found.")
