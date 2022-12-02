from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# q1 = Question(text, answer)

for q in question_data:
    q_t = q["text"]
    q_a = q["answer"]
    new = Question(q_t,q_a)
    question_bank.append(new)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question(question_bank)

