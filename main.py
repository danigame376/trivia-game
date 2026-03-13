import random

N_QUESTION = 5
MAX_POINTS = 3
POINT_STEPS = 1


questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "boolean",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3",
}


def print_header():
    print("\n=== TRIVIA GAME 1.0 ===")
    print("press q to exit\n")


def get_answer(i, question):
    return input(f"Question {i + 1}: {question} ").lower().strip()


def check_answer(user_answer, question, points_counter):
    if user_answer == "q":
        print("=== CLOSING GAME ===")
        return None

    if user_answer == questions[question].lower():
        print(f"correct! +{POINT_STEPS}")
        print(f"you now have {points_counter + POINT_STEPS}/{MAX_POINTS} points\n")
        return POINT_STEPS

    else:
        print(f"Wrong! the correct answer is: {questions[question]}")
        print(f"you still have {points_counter}/{MAX_POINTS} points\n")
        return 0


def check_vicotry(points_counter):
    if points_counter == MAX_POINTS:
        return 1


def print_win():
    print("YOU WIN!")
    print("=== CLOSING GAME ===")


def print_lose(points_counter):
    print(f"You lose!, your score is {points_counter}/{MAX_POINTS}")
    print("=== CLOSING GAME ===")


def main():

    print_header()
    points_counter = 0
    qs_selected = random.sample(list(questions.keys()), N_QUESTION)

    for i, question in enumerate(qs_selected):
        user_answer = get_answer(i, question)
        result = check_answer(user_answer, question, points_counter)

        if result is None:
            return

        points_counter += result

        if check_vicotry(points_counter):
            print_win()
            return

    print_lose(points_counter)


if __name__ == "__main__":
    main()
