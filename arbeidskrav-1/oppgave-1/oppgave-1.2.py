# Oppgave 1.2 – Analyser tekst

while True:
    text_string = input("Enter a text: ")
    if text_string == "" or text_string.isspace():
        print("Invalid input. Please enter a text")
    else:
        break

text_string_without_spaces = text_string.count(" ")

print(f"The number of characters with spaces: {len(text_string)}")
print(f"The number of characters without spaces: {len(text_string) - text_string_without_spaces}")
print(f"The text in lowercase: {text_string.lower()}")
print(f"The text reversed: {text_string[::-1]}")

if "python" in text_string.lower():
    print(f'The text contains word "python"')
else:
    print(f'The text does not contain the word "python"')
