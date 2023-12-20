class Question:
    def __init__(self, question_id, theme, question, option1, option2, option3, option4, answer):
        self.question_id = question_id
        self.theme = theme
        self.question = question
        self.options = [option1, option2, option3, option4]
        self.answer = answer

    
    def verifier_reponse(self, reponse):
        
        return self.answer == reponse
    