class Question:

    def __init__(self, text, diff, answer):

        self.text = text
        self.diff = diff
        self.answer = answer

        self.is_asked = False
        self.user_answer = None
        self.points = self.diff * 10

    def get_points(self):

        return self.points

    def is_correct(self):

        return self.user_answer == self.answer

    def build_question(self):

        question_answer = f"\nВопрос: {self.text}\nСложность: {self.diff}/5"
        return question_answer

    def build_positive_feedback(self):

        question_answer = f"Ответ верный, получено {self.points} баллов"

        return question_answer

    def build_negative_feedback(self):

        question_answer = f"Ответ неверный. Верный ответ – {self.answer}"

        return question_answer

    def __repr__(self):
        return f"{self.text} - {self.answer} ({self.diff}/5)"
