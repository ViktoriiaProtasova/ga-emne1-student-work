from pathlib import Path

notes_path = Path("..") / "data" / "notes.txt"

with open(notes_path, "w", encoding="utf-8") as file:
    file.write("Remember to buy groceries.\n")

with open(notes_path, "w", encoding="utf-8") as file:
    file.write("Finish Python homework.\n")

# "w" overskriver gammelt innhold.
# Det gamle innholdet blir slettet.

with open(notes_path, "a", encoding="utf-8") as file:
    file.write("Remember to buy groceries.\n")

with open(notes_path, "a", encoding="utf-8") as file:
    file.write("Finish Python homework.\n")

# "a" legger til tekst på slutten.
# Det gamle innholdet blir beholdt.