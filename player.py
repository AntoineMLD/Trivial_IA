class Player:
    def __init__(self):
        self.name = ""
        self.score = 0
        self.position = 0
        self.correct_answers_by_theme = {}  # Dictionnaire pour stocker le score par thème

    def set_name(self):
        self.name = input("Entrez votre nom de joueur : ")

    def deplacement(self, steps):
        self.position += steps

    def lancer_de(self):
        result = random.randint(1,7)
        self.deplacement(result)

        direction = input(f"{self.name}, voulez-vous vous déplacer vers la gauche (g) ou vers la droite (d) ? ").lower()
        if direction == 'g':
            self.position -= 1
        elif direction == 'd':
            self.position += 1
        else:
            print("Choix invalide. Veuillez tapez g ou d.")


    def reponse(self, question, bonne_reponse, theme):
        print(f"{self.name}, voici une question ({theme}) : {question}")

        options = ["1.réponse1 ", "2.réponse2 ", "3.réponse3 "]

        print("Options :")
        for option in options:
            print(option)

        while True:
            choix = input("Votre réponse (1, 2, ou 3) : ")
            if choix == '1':
                print(f"Bonne réponse {self.name}.")
                # Mise à jour des bonnes réponses par thème dans le dico 
                if theme not in self.correct_answers_by_theme:
                    self.correct_answers_by_theme[theme] = 1
                else:
                    self.correct_answers_by_theme[theme] += 1
                return True
            elif choix in ('2', '3'):
                print(f"Mauvaise réponse. {self.name} n'a pas gagné.")
                return False
            else:
                print("Choix invalide. Veuillez choisir parmi les options proposées.")

            # Mis à jour du score total
                self.total_score += 1

    

    










