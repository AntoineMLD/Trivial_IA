import random
from class_question import Question
from utils import THEMES
import networkx as nx


class Player:
    def __init__(self, name):
        self.name = name
        self.score = {theme: False for theme in THEMES}
        self.position = 72
   
    def score_point(self, category: str):
        self.score[category] = True
    

    def check_victory(self):
            return sum(self.score.values()) == 6
        
    
    def lancer_de(self):
        result = random.randint(1, 6)
        return result 


    def give_new_positions(self, G):
        result = self.lancer_de()
        travel_possible = nx.shortest_path_length(G, self.position)
        path_possible = []
        for key,value in travel_possible.items():
            if value == result:
                path_possible.append(key)
        return path_possible
                        