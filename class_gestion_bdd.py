import sqlite3
import random
from class_question import Question

class GestionBDD:
    def __init__(self, nom_base_de_donnees):
        self.connexion = sqlite3.connect(nom_base_de_donnees)
        self.curseur = self.connexion.cursor()

    def obtenir_question(self):
        # Sélectionnez une question aléatoire depuis la base de données
        self.curseur.execute("SELECT * FROM questions ORDER BY RANDOM() LIMIT 1")
        row = self.curseur.fetchone()

        if row:
            question = Question(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            return question
        else:
            return None

    def fermer_connexion(self):
        self.connexion.close()