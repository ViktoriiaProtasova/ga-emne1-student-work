def ask_question(question_text):
    return input(question_text)



def check_answer(answer, correct_answer):
    if answer.lower() == correct_answer.lower():
        return True
    return None


def show_feedback(is_correct):
    if is_correct:
        print("It is correct answer!")
        return 1
    else:
        print("It is incorrect answer!")
    return 0


def run_quiz():
    score = 0

    answer = ask_question("What is the capital of Norway? ")
    score += show_feedback(check_answer(answer, "Oslo"))

    answer = ask_question("How many days are there in a week? ")
    score += show_feedback(check_answer(answer, "7"))

    answer = ask_question("What programming language is used in this quiz? ")
    score += show_feedback(check_answer(answer, "Python"))

    print(f"Total score: {score}")



run_quiz()

