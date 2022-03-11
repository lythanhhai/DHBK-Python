from Data import question_data

class Question_model():
    def __init__(self, text="", answer=""):
        self.text = text
        self.answer = answer

class Question_bank():
    def __init__(self, list_question= []):
        self.list_question = []
        for question in question_data:
            self.list_question.append(Question_model(question_data['text'], question_data['answer']))

# new_q = Question_model()
# new_q_b = Question_bank()