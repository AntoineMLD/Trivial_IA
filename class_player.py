import random
from class_question import Question
from board_network import *

class Player:
    def __init__(self):
        self.name = ""
        self.score = 0
        self.position = central_node
        self.correct_answers_by_theme = {}  # Dictionnaire pour stocker le score par thème
        

    def set_name(self):
        self.name = input("Entrez votre nom de joueur : ")
        
         
    def lancer_de(self):
        result = random.randint(1, 6)
    
    def give_new_positions(self):
        result = self.lancer_de()
        
        travel_possible = nx.shortest_path_length(G, self.position)
        
        path_possible = []
        
        for key,value in travel_possible.items():
            if value == result:
                path_possible.append(key)
        return path_possible
        
    
    
    
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


    

joueur1 = Player()

joueur1.lancer_de()









