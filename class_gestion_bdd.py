import sqlite3
import random
from class_question import Question


class GestionBDD:
    def __init__(self, nom_base_de_donnees):
        self.connexion = sqlite3.connect(nom_base_de_donnees)
        self.curseur = self.connexion.cursor()
        self.questions_utilisees = set () # Utilise un ensemble pour stocker les ID des questions déjà utilisées

    def obtenir_question(self, theme):
        # Sélection d'une question aléatoire depuis la base de données
        self.curseur.execute("SELECT * FROM questions WHERE theme = ? ORDER BY RANDOM() LIMIT 1", (theme,))
        row = self.curseur.fetchone()

        if row:
            question_id = row[0]
            # Vérifier si la question a déjà été utilisée
            while question_id in self.questions_utilisees:
                self.curseur.execute("SELECT * FROM questions WHERE theme = ? ORDER BY RANDOM() LIMIT 1", (theme,))
                row = self.curseur.fetchone()
                question_id = row[0]

            # Ajouter l'ID de la question à l'ensemble des questions utilisées
            self.questions_utilisees.add(question_id)

            question = Question(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            return question
        else:
            return None

    def fermer_connexion(self):
        self.connexion.close()
        