import random
import data as d

def question():
    ques = random.choice(d.question_data)
    d.question_data.remove(ques)
    return ques















