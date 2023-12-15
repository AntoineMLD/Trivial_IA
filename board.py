"""
This module is devoted to create the board.
"""

from utils import CircularList
    

# Generate the board
# Names beginning by * indicates you can score on the square
CASES = [
    "*Spe", "Shell", "Again", "IA", "Python", "Again", "Git",
    "*SQL", "Git", "Again", "Shell", "Spe", "Again", "Python",
    "*IA", "Python", "Again", "Git", "SQL", "Again", "Spe",
    "*Shell", "Spe", "Again", "Python", "IA", "Again", "SQL",
    "*Git", "SQL", "Again", "Spe", "Shell", "Again", "IA",
    "*Python", "IA", "Again", "SQL", "Git", "Again", "Shell"
    ]

BOARD = CircularList(CASES)
