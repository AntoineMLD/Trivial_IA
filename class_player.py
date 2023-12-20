import random
from class_question import Question
from board_network import *

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.position = central_node
        self.correct_answers_by_theme = {}  # Dictionnaire pour stocker le score par thème 
         
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
        themes_disponibles = [
            "Recherche d'emploi et recrutement",
            "Ligne de commande Terminal Linux",
            "Git_Github",
            "Python",
            "Actualité IA",
            "SQL"
        ]

    # Afficher les thèmes disponibles
        print("Sélectionnez un thème en entrant le numéro correspondant :")
        for i, theme in enumerate(themes_disponibles, 1):
            print(f"{i}. {theme}")

    # Demander à l'utilisateur de choisir un thème
        choix_theme = int(input("Votre choix : "))

    # Vérifier si le choix est valide
        if 1 <= choix_theme <= len(themes_disponibles):
            theme_selectionne = themes_disponibles[choix_theme - 1]
            question = gestion_bdd.obtenir_question(theme_selectionne)
        
        if question:
            print(f"\nBienvenue, {self.name}!")
            question.afficher_question()

            choix = int(input("Entrez le numéro de votre réponse (1, 2, 3 ou 4): "))

            if question.verifier_reponse(choix):
                print("Bonne réponse!")
            
            else:
                print("Mauvaise réponse.")
        else:
            print("Erreur: Aucune question trouvée.")


    

joueur1 = Player()

joueur1.lancer_de()









