import random
import json

N_QUESTION = 5
MAX_POINTS = 3
POINT_STEPS = 1
FILENAME = "questions.json"


with open(FILENAME, "r", encoding="utf-8") as file:
    questions = json.load(file)


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
