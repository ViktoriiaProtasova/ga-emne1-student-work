from pathlib import Path

print(f"Current directory is: {Path.cwd()}")

data_directory = Path("..") / "data"

if data_directory.exists():
    print(data_directory)