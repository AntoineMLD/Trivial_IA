import math

import pygame

from board_coordinates import calculate_all_pos
from board_network import create_game_network
from config import BACKGROUND, HEIGHT, WIDTH, BOX_RADIUS, BOX_TYPE_TO_COLOR


# Displaying Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TrivIA Pursuit Board")

# Calculate all boxes positions and create the game's network
positions = calculate_all_pos()
network = create_game_network()

# MAIN RUN
running = True

while running:
    screen.fill(BACKGROUND)  # Official background
    
    # Draw all the boxes
    for idx, pos in enumerate(positions):
        # Get the color from the network nodes
        box_color = BOX_TYPE_TO_COLOR[network.nodes[idx]['box_type']]
        pygame.draw.circle(screen, box_color, pos, BOX_RADIUS)

    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit()
