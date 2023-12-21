from collections import deque
from random import shuffle
from typing import List
from class_player import Player
from board import BOARD
from config import INDEX_TO_BOX_TYPE
from board_network import create_game_network
from board_coordinates import calculate_all_pos
from class_player import Player
from class_gestion_bdd import GestionBDD
from typing import Tuple


def init_game(player_names: List[str]):
    """
    Set initial game status:
    - winner: Optional[str] = None
    - network: graph object
    - positions: List[Tuple[int, int]]
    - bdd: GestionBDD
    - players: deque d'instances de Joueur
    
    """
    winner = None

    # Set board backend
    network = create_game_network()
    positions = calculate_all_pos()

    # Instanciate BDD
    bdd = GestionBDD("questions.db")

    # Set turn order
    players = [Player(name) for name in player_names]
    shuffle(players)
    players = deque(players)
        
    return (winner, network, positions, bdd, players)


def check_current_case(player: Player) -> Tuple[str, bool]:
    """
    returns a tuple with:
    - next action,
    - scoring or not
    - theme
    """
    scoring = False
    box = INDEX_TO_BOX_TYPE[player.position]
 
    if box == "Again":
        return box, scoring

    if box.startswith("*"):
        scoring = True
        box = box[1:]
    
    return box, scoring


def update_game_after_question(player, theme, correct_answer, scoring) -> str:
    """
    Sets what will be done after answer in questions
    """
    if correct_answer and scoring:
        player.score_point(theme)
        player_wins = player.check_victory()
        if player_wins:
            return "Victory"
        return "Again"
    elif correct_answer:  # and not scoring
        return "Again"
    else:  # Player didn't correctly answer
        return "Next"

# def set_turn_order():
#         players = deque(players)
#         if game_state == "A":
#             return players
#         else:
#             players.rotate(-1)
#             return players
