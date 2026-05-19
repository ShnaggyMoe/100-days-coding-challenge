class User():
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username


user_1 = User('001', 'angela')
print(user_1.id)
print(user_1.name)

user_2 = User('002', 'jack')
print(user_2.id)
print(user_2.name)


class Question():
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer