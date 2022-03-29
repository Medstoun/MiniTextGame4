import random

from question import Question
from data import data

def main():

    questions = []

    for i in data:
        new_question = Question(
            i["q"],
            int(i["d"]),
            i["a"]
        )
        questions.append(new_question)

        random.shuffle(questions)

    for question in questions:
        print(question.build_question())

        user_answer = input()

        question.user_answer = user_answer

        if question.is_correct():
            print(question.build_positive_feedback())
        else:
            print(question.build_negative_feedback())


    counter = 0

    points = 0

    for question in questions:
        if question.is_correct():
            counter += 1
            points += question.get_points()

    print("Вот и всё!")
    print(f"Верно отвечено {counter} вопроса из 10")
    print(f"Набрано баллов: {points}")



main()
