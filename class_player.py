import random
from class_question import Question

class Player:
    def __init__(self):
        self.name = ""
        self.score = 0
        self.position = 0
        self.correct_answers_by_theme = {}  # Dictionnaire pour stocker le score par thème

    def set_name(self):
        self.name = input("Entrez votre nom de joueur : ")
        
        

    
    def lancer_de(self):
        result = random.randint(1, 6)

        direction = input(f"{self.name}, voulez-vous vous déplacer vers la gauche (g) ou vers la droite (d) ? ").lower()
        if direction == 'g':
            self.position -= result
        elif direction == 'd':
            self.position += result
        else:
            print("Choix invalide. Veuillez taper g ou d.")
            

    def poser_question(self, gestion_bdd):
        question = gestion_bdd.obtenir_question()

        if question:
            print(f"\nBienvenue, {self.name}!")
            question.afficher_question()

            choix = int(input("Entrez le numéro de votre réponse (1, 2, 3, 4): "))

            if question.verifier_reponse(choix):
                print("Bonne réponse!")
            
            else:
                print("Mauvaise réponse.")
        else:
            print("Erreur: Aucune question trouvée.")


    

    










