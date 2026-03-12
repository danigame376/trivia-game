import random

MAX_POINTS = N_QUESTION = 5


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
        if answer == questions[question]:
            print("correct! +10\n")
            points_counter += 1
            print(f"you now have {points_counter} points\n")

            if points_counter == MAX_POINTS:
                print("YOU WIN!")
                print("=== CLOSING GAME ===")
                break
        elif answer == "q":
            break

        elif answer != questions[question]:
            print(f"Wrong! the correct anwer is: {questions[question]}\n")

    if points_counter < MAX_POINTS:
        print(f"You loose!, yuor score is {points_counter}/{MAX_POINTS}")
        print("=== CLOSING GAME ===")


if __name__ == "__main__":
    main()
