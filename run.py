import pygame
from collections import deque
import game_functions
from game_functions import init_game
from ui_functions import initialize_display, get_player_names

# Initialize PyGame and set it
pygame.init()
screen, font = initialize_display()
print(type(screen))
print(type(font))

# Get players' names
player_names = get_player_names(screen, font)
print("Player Names:", player_names)

# Initialize game
winner, network, positions, bdd, players = init_game(player_names)
print("Done")



winner, network, positions, bdd, players, game_state =game_functions.init_game()
def get_active_player():
        players = deque(players)
        if game_state == "A":
            return players[0]
        else:
            players.rotate(-1)
            return players
            
  

pygame.quit()
