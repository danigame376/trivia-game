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

    q_selected = list(questions.keys())
    random.shuffle(q_selected)
    for question in q_selected:
        if question == q_selected[-1]:
            print("\nYou loose!")
            print("=== CLOSING GAME ===")
            break
        risposta = input(question + " ")
        if risposta == questions[question]:
            print("correct! +10")
            points_counter += 10
            print(f"you now have {points_counter} points\n")

            if points_counter == 50:
                print("YOU WIN!")
                print("=== CLOSING GAME ===")
                break
        elif risposta == "q":
            break
        else:
            print("Wrong! Try again!")
        
        



if __name__ == "__main__":
    main()
