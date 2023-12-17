import sqlite3
import json

# Load JSON file 
with open('data.json', 'r') as f:
    json_data = json.load(f)

# Connect the BDD
with sqlite3.connect('Trivial_bdd.db') as connection:
    cursor = connection.cursor()
    
    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS categories (
            categorie_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            SQL TEXT, 
            Actualité_IA TEXT, 
            Python TEXT, 
            Git_Github TEXT, 
            Ligne_de_commande_Terminal_Linux TEXT); 
        
        CREATE TABLE IF NOT EXISTS questions (
            question_id INTEGER PRIMARY KEY AUTOINCREMENT, text_question TEXT, 
            categorie_id INTEGER,
            FOREIGN KEY(categorie_id) REFERENCES categories(categorie_id)
        );
        
        CREATE TABLE IF NOT EXISTS answers (
            answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            text_answer TEXT,
            is_correct BOOL,
            question_id INTEGER,
            FOREIGN KEY(question_id) REFERENCES questions(question_id)
        );
        ''')

    for category, questions in json_data.items():
        # Insert category in categories TABLE
        cursor.execute('INSERT INTO categories (SQL, Actualité_IA, Python, Git_Github, Ligne_de_commande_Terminal_Linux) VALUES (?,?,?,?,?)',
                       (category, None, None, None, None))
        categorie_id = cursor.lastrowid # Recover ID of the question Inserted
        
        # Insert each question and this answer in the table
        for question_data in questions:
            # Insert the question in the question table
            cursor.execute('INSERT INTO questions (text_question, categorie_id) VALUES (?, ?)',
                           (question_data['question'], categorie_id))
            question_id = cursor.lastrowid 
            
            # Insert answer in the answer table
            for choice, choice_data in question_data['choices'].items():
                cursor.execute('INSERT INTO answers (text_answer, is_correct, question_id) VALUES (?, ?, ?)',
                               (choice_data['text'], choice_data['is_correct'], question_id))

connection.commit()


