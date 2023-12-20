import pygame

from brouillon import init_game
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


pygame.quit()
