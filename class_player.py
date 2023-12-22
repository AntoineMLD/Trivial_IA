import random
from class_question import Question
from config import THEMES, INDEX_TO_BOX_TYPE
import networkx as nx


class Player:
    def __init__(self, name):
        self.name = name
        self.score = {theme: False for theme in THEMES}
        self.position = 72
    
    def __repr__(self):
        id_pos = f"Player {self.name} at position {self.position}\n"
        state = f"Score: {', '}.join({self.score.values()})"
        return id_pos + state
   
    def score_point(self, category: str):
        box_type = INDEX_TO_BOX_TYPE[self.position]
        if box_type.startswith('*'):
            self.score[category] = True
    

    def check_victory(self):
        return sum(self.score.values()) == 6
        
    
    def lancer_de(self):
        result = random.randint(1, 6)
        return result 


    def give_new_positions(self, G, dice_result):
        travel_possible = nx.single_source_shortest_path_length(G,self.position, cutoff=dice_result)
        path_possible = [node for node, distance in travel_possible.items() if distance == dice_result]
        return path_possible

    