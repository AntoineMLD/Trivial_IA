from collections import deque
from random import shuffle
from typing import List

from board_network import create_game_network
from board_coordinates import calculate_all_pos
from class_player import Player
from class_gestion_bdd import GestionBDD


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

    return winner, network, positions, bdd, players


