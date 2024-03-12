class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question, options):
        print(question)
        for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option}")

    def validate_answer(self, user_input, correct_answer):
        return user_input.lower() == correct_answer.lower()

    def run_quiz(self):
        for question, options, correct_answer in self.questions:
            self.display_question(question, options)
            user_answer = input("Enter your choice: ")
            if self.validate_answer(user_answer, correct_answer):
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect. The correct answer is:", correct_answer)
            print()

    def display_final_score(self):
        print("Quiz completed!")
        print("Your final score is:", self.score)


if __name__ == "__main__":
    questions = [
        ("What is the capital of France?", ["Paris", "London", "Berlin"], "Paris"),
        ("What is 2 + 2?", ["3", "4", "5"], "4"),
        ("Which planet is known as the Red Planet?", ["Mars", "Venus", "Mercury"], "Mars")
    ]

    quiz = Quiz(questions)
    quiz.run_quiz()
    quiz.display_final_score()
