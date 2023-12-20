import pygame

from game_functions import init_game
from ui_functions import initialize_display, get_player_names, display_board

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

pygame.quit()
