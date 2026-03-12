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


def main():
    points_counter = 0
    print("\n=== TRIVIA GAME 1.0 ===")
    print("press q to exit\n")

    q_selected = random.sample(list(questions.keys()), N_QUESTION)
    for i, question in enumerate(q_selected):
        answer = input(f"Question {i + 1}: {question} ").lower().strip()

        if answer == "q":
            print("=== CLOSING GAME ===")
            return

        if answer == questions[question].lower():
            print(f"correct! +{POINT_STEPS}")
            points_counter += POINT_STEPS
            print(f"you now have {points_counter}/{MAX_POINTS} points\n")

            if points_counter == MAX_POINTS:
                print("YOU WIN!")
                print("=== CLOSING GAME ===")
                return
        else:
            print(f"Wrong! the correct anwer is: {questions[question]}")
            print(f"you now have {points_counter}/{MAX_POINTS} points\n")

    print(f"You lose!, yuor score is {points_counter}/{MAX_POINTS}")
    print("=== CLOSING GAME ===")


if __name__ == "__main__":
    main()
