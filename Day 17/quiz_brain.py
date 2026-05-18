class QuizBrain():
    def __init__(self, question_list):
        self.q_list = question_list
        self.q_number = 0
        self.score = 0


    def still_has_question(self):
        return self.q_number < len(self.q_list)


    def next_question(self):
        current_question = self.q_list[self.q_number]
        user_answer = input(current_question.text)
        self.q_number += 1
        if current_question.answer == user_answer:
            self.score += 1
            print(f"Correct answer. Good job! Your score is {self.score}")
            return True
        else:
            print(f"Incorrect! The correct answer was {current_question.answer}. Your score is {self.score}")