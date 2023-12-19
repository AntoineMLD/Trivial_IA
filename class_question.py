class Question:
    def __init__(self, question_id, theme, question, option1, option2, option3, option4, answer):
        self.question_id = question_id
        self.theme = theme
        self.question = question
        self.options = [option1, option2, option3, option4]
        self.answer = answer

    def afficher_question(self):
        print(f"Thème: {self.theme}")
        print(f"Question: {self.question}")

        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}") 
       

    def verifier_reponse(self, choix):
        
        return self.options[choix - 1] == self.answer