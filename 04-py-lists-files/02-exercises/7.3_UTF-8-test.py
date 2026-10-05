from pathlib import Path

utf8_test_path = Path("..") / "data" / "utf8_test.txt"

with open(utf8_test_path, "w", encoding="utf-8") as file:
    file.write("Blåbær, grøt, pølse, ærlig og Østfold\n")

with open(utf8_test_path, "r", encoding="utf-8") as file:
    print(file.read())