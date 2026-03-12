import random

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
    print("=== TRIVIA GAME 1.0 ===")
    print("press q to exit\n")

    while True:
        q_selected = random.choice(list(questions.keys()))
        risposta = input(q_selected + " ")
        if risposta == questions[q_selected]:
            print("correct! +10")
            points_counter += 10
            print(f"you now have {points_counter} points\n")

            if points_counter == 50:
                print("YOU WIN!")
                break
        elif risposta == "q":
            break
        else:
            print("Wrong! Try again!")


if __name__ == "__main__":
    main()
