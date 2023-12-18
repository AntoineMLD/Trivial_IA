import sqlite3
import json

# Charger le fichier JSON
with open('/home/utilisateur/Documents/dev ia/Trivial_IA/data.json', 'r') as json_file:
    data = json.load(json_file)

# Créer une connexion à la base de données SQLite (cette ligne crée un fichier SQLite dans le répertoire courant)
conn = sqlite3.connect('questions.db')

# Créer un curseur pour exécuter des commandes SQL
cursor = conn.cursor()

# Créer une table pour les questions
cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        theme TEXT,
        question TEXT,
        choice_a TEXT,
        choice_b TEXT,
        choice_c TEXT,
        choice_d TEXT,
        answer TEXT
    )
''')

# Insérer les données dans la table
for theme, questions in data.items():
    for question in questions:
        cursor.execute('''
            INSERT INTO questions (theme, question, choice_a, choice_b, choice_c, choice_d, answer)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            theme,
            question['question'],
            question['Réponse A'],
            question['Réponse B'],
            question['Réponse C'],
            question['Réponse D'],
            question['Answer']
        ))

# Valider les changements dans la base de données
conn.commit()

# Fermer la connexion
conn.close()

