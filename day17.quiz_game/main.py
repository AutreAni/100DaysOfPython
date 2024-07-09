from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_item = Question(question['question'], question['correct_answer'])
    question_bank.append(question_item)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quizz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")