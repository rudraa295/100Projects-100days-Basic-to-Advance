import question_model as qm
import quiz_brain as qb

points = 0

while True:

    points += 1
    content = qm.question()
    useranswer = input(f"\n{content['text']} (True/False): ").title()

    qb.Question(useranswer , content['answer'], points)