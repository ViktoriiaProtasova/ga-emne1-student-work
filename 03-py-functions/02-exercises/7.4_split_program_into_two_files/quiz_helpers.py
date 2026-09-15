def ask_question(question_text):
    """Viser et spørsmål og returnerer brukerens svar."""
    return input(question_text)


def check_answer(answer, correct_answer):
    """Sjekker svaret og returnerer True hvis svaret er riktig, ellers False."""
    if answer.lower() == correct_answer.lower():
        return True
    return False


def show_feedback(is_correct):
    """Viser om svaret er riktig og returnerer 1 eller 0."""
    if is_correct:
        print("It is correct answer!")
        return 1
    else:
        print("It is incorrect answer!")
    return 0


def run_quiz():
    """Kjører quizen, teller poeng og viser sluttsummen."""
    score = 0

    answer = ask_question("What is the capital of Norway? ")
    score += show_feedback(check_answer(answer, "Oslo"))

    answer = ask_question("How many days are there in a week? ")
    score += show_feedback(check_answer(answer, "7"))

    answer = ask_question("What programming language is used in this quiz? ")
    score += show_feedback(check_answer(answer, "Python"))

    print(f"Total score: {score}")