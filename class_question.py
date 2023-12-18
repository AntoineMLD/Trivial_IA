class Question:
    def __init__(self, question_id, question, option1, option2, option3, option4, answer):
        self.question_id = question_id
        self.question = question
        self.options = [option1, option2, option3, option4, answer]
        self.answer = answer

    def afficher_question(self):
        print(self.question)
        for i, option in enumerate(self.options, start=0):
            print(f"{i}. {option}") 
       

    def verifier_reponse(self, choix):
        
        return self.options[choix - 1] == self.answer or self.options[-1] == self.answer