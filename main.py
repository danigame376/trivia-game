import random
import sys
import json
from pathlib import Path

N_QUESTIONS = 5
MAX_POINTS = 3
POINT_STEPS = 1
FILENAME = "questions.json"


class TriviaGame:
    def __init__(
        self, filename: str, point_steps: int, max_points: int, n_questions: int
    ) -> None:
        self.filepath = Path(filename)
        self.questions = self._load_questions()
        self.points = 0
        self.point_steps = point_steps
        self.max_points = max_points
        self.n_questions = n_questions

    def _load_questions(self) -> dict[str, str]:
        if not self.filepath.exists():
            print(f"Non trovo il file {self.filepath}")
            print("=== CLOSING GAME... ===")
            sys.exit(1)
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"il file {self.filepath} non è un jason valido")
            print("=== CLOSING GAME... ===")
            sys.exit(1)

    def _get_answer(self, i: int, question: str) -> str:
        return input(f"Question {i}: {question} ").lower().strip()

    def _check_user_answer(self, answer: str, question: str) -> bool:
        if answer == "q":
            return True

        if answer == self.questions[question].lower():
            self.points += self.point_steps
            print(f"Correct! you have {self.points}/{self.max_points} points")
        else:
            print(f"Wrong, you still have {self.points}/{self.max_points} points")
        return False

    def run(self) -> None:
        print("=== TRIVIA GAME 1.0 ===")
        print("Press q to exit")

        n_questions = min(self.n_questions, len(self.questions))
        qs_selected = random.sample(list(self.questions.keys()), n_questions)

        for i, question in enumerate(qs_selected, start=1):
            user_answer = self._get_answer(i, question)
            user_wants_to_quit = self._check_user_answer(user_answer, question)
            if user_wants_to_quit:
                print("=== CLOSING GAME... ===")
                return
            if self.points == self.max_points:
                print("YOU WIN!")
                print("=== CLOSING GAME... ===")
                return
        print("You lose!")
        print("=== CLOSING GAME... ===")
        return


def main() -> None:
    game = TriviaGame(FILENAME, POINT_STEPS, MAX_POINTS, N_QUESTIONS)
    game.run()


if __name__ == "__main__":
    main()
