def repeat_message(message, repetitions = 3):
    for i in range(repetitions):
        print(message)

repeat_message("Hello World!")

print("\n---\n")

repeat_message("Hello World!", 5)