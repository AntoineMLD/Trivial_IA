import pygame
from collections import deque
import game_functions
from game_functions import init_game, update_game_after_question
from ui_functions import initialize_display, get_player_names



# Initialize PyGame and set it
pygame.init()

screen, font = initialize_display()

# Get players' names
player_names = get_player_names(screen, font)
print("Player Names:", player_names)

# Initialize game components
winner, network, positions, bdd, players = init_game(player_names)

# Draw board
display_board(screen, network, positions)
pygame.display.flip()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # display_board(screen, network, positions)

    # pygame.display.flip()
    print("Done")


winner, network, positions, bdd, players, game_state = game_functions.init_game()


 # Dans run.py
game_status = update_game_after_question()

if game_status == "Victory":
    winner = active_player.name
elif game_status == "Next":
    players.rotate(-1)    

pygame.quit()
