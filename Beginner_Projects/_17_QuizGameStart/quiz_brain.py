class Question:
    def __init__(self, useranswer, answer , points):
        self.useranswer = useranswer
        self.answer = answer

        if useranswer == answer:
            pass
        else:
            print(f"The answer was not correct ... Your points are {points-1}")
            exit()