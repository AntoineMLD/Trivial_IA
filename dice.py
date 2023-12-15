"""
This module contains the Dice class, devoted to randomization, including:
- rolling the dice to move on the board,
- eventually randomizing the question's pick into the database.
"""


from random import randint


class Dice:
    """
    Implements a dice object, with number of faces being tuneable.
    """
    def __init__(self, nb_faces; int):
        self.nb_faces = nb_faces

    def roll(self):
        return randint(1, self.nb_faces)
