from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain

objs = list()
for i in range(len(question_data)):
    objs.append(Questions(question_data[i]['question'], question_data[i]['correct_answer']))

quiz_1 = QuizBrain(objs)
print(quiz_1.still_has_question())
while quiz_1.still_has_question():
    quiz_1.next_question()

print(f"You've completed the quiz!")
print(f"Your final score was {quiz_1.score}/{quiz_1.question_number}")

