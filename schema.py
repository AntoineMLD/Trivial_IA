from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# Create an item engine to connect from the bdd
engine = create_engine('sqlite://Trivial_bdd.db')

# Base class to define the model
Base = declarative_base()

# Need to create table categories with id and name of categories, a table questions with id, categorie_id and question_text then a table answer with id, question_id, response_text and is_correct (Bool)

# Create class categories
class Categories(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name_categorie = Column(String)
    questions = relationship("Questions", back_populates="category")

# Create class Questions
class Questions(Base):
    __tablename__ = 'questions'
    
    id = Column(Integer, primary_key=True)
    categorie_id = Column(Integer, ForeignKey('categories.id'))
    question_text = Column(String)
    category = relationship("Categories", back_populates="questions")
    answer = relationship("answer", back_populates="question")

# Create class answer
class Answer(Base):
    __tablename__ = 'answer'
    
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    answer_text = Column(String)
    question = relationship("Questions", back_populates="answer")


# Create table on the dbb
Base.metadata.create_all(engine)

# Create DBB's session
Session = sessionmaker(bind=engine)
session = Session()

# Add category in the category table
sql = Categories(id=1, name_categorie = 'SQL')
python = Categories(id=2, name_categorie = 'Python')
lci = Categories(id=3, name_categorie = 'Ligne de commande')
ia = Categories(id=3, name_categorie = 'Actualités IA')
git = Categories(id=3, name_categorie = 'Git/Github')

session.add_all([sql, python, lci, ia, git])


# Add questions in the Questions table

sql_question_1 = Questions(id=1, categorie_id = 1, question_text = 'Que veut dire SGBDR ? ')
sql_question_2 = Questions(id=2, categorie_id = 1, question_text = 'Qui est le créateur originel de MySQL ?')
sql_question_3 = Questions(id=3, categorie_id = 1, question_text = 'Quel est l’ordre des requête SQL ?')
sql_question_4 = Questions(id=4, categorie_id = 1, question_text = 'Quels sont les systèmes de gestion de base de data relationnelle les plus populaires ?')
sql_question_5 = Questions(id=4, categorie_id = 1, question_text = 'Quels sont les systèmes de gestion de base de data relationnelle les plus populaires ?')



# Add answer in the Answer table
sql_answer_1 = Answer(id=1, question_id = 1, answer_text = {'a' : 'Système de Gestion de Base de Données Réseau', 'b' : 'Sécurité Globale des Bases de Données Relationnelles', 'c' : 'Système de Gestion de Base de Donnée Relationnelle'})
sql_answer_2 = Answer(id=2, question_id=1, answer_trext = {'a' : 'John McCarthy', 'b' : 'Michael Widenius', 'c' : 'Linus Torvalds'})
sql_answer_3 = Answer(id=3, question_id=1, answer_trext = {'a' : 'Select, From, Where, Order by, Having', 'b' : 'From, Select, Where, Order by, Having', 'c' : 'Select, Order by, Where, From, Having'})
sql_answer_4 = Answer(id=4, question_id=1, answer_trext = {'a' : 'Oracle Database, MySQL, Microsoft SQL Server, PostgreSQL, SQLite', 'b' : 'MongoDB, Cassandra, Redis"', 'c' : 'Excel, PowerPoint, Word', 'd' : 'Visual Studio, Eclipse, Ruby'})
