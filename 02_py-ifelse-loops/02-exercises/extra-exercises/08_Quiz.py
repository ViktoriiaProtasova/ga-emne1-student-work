#%% Quiz med tre spørsmål

score = 0

print("Quiz: Python Basics")

print("1. It displays text on the screen.")
print("2. It reads input from the user.")
print("3. It stops the program.")

answer = input("Question: What does input() do in Python?")

if answer == "2":
    print("Pass")
    score += 1
else:
    print("Fail")

print("1. x")
print("2. *")
print("3. **")

answer = input("Which symbol is used for multiplication in Python?")

if answer == "2":
    print("Pass")
    score += 1
else:
    print("Fail")

print("1. It repeats a block of code while a condition is true.")
print("2. It creates a new variable.")
print("3. It runs a block of code only once.")

answer = input("What does a while loop do?")

if answer == "1":
    print("Pass")
    score += 1
else:
    print("Fail")

print(f"Total score: {score}")