class Question:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class Quiz:

    def __init__(self):
        self.questions = []

    def add_question(self, question, answer):
        new_question = Question(question, answer)
        self.questions.append(new_question)

    def remove_question_at(self, index):
        del self.questions[index]

    def get_question_at(self, index):
        return self.questions[index].question

    def check_answer_at(self, index, user_answer):
        actual_answer = self.questions[index].answer
        if user_answer.lower() == actual_answer.lower():
            return True
        else:
            return False

    def get_num_questions(self):
        return len(self.questions)


def test_backend():
    test_quiz = Quiz()
    test_quiz.add_question("Test Q", "Test A")
    print(f"Test Q count: {test_quiz.get_num_questions()}")


if __name__ == "__main__":
    test_backend()