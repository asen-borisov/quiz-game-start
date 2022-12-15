from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from UI import QuizInterface

question_bank = []



for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    new = Question(q_text, q_answer)
    question_bank.append(new)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question(question_bank)

print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
