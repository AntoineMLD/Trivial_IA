import math

import pygame

from board import CASES
from board_coordinates import calculate_all_pos
from config import BACKGROUND, BLUE, BROWN, GREEN, GREY, ORANGE, PINK, YELLOW
from config import HEIGHT, WIDTH
from config import THEME_TO_COLOR


# CONTOUR = [THEME_TO_COLOR[case] for case in CASES]
# BRIDGES = [
#     [BROWN, YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE,
#      ORANGE, PINK, GREEN, BLUE, BROWN, YELLOW],
#     [BLUE, PINK, GREEN, YELLOW, ORANGE, BROWN, WHITE,
#       YELLOW, GREEN, BROWN, ORANGE, BLUE, PINK],
#     [ORANGE, GREEN, BROWN, PINK, YELLOW, BLUE, WHITE,
#       PINK, BROWN, BLUE, YELLOW, ORANGE, GREEN]
# ]

# Displaying Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TrivIA Pursuit Board")

# # Board Circle
# BOARD_RADIUS = 250
# CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

# Calculate all boxes positions
positions = calculate_all_pos()

# MAIN RUN
running = True

while running:
    screen.fill(BACKGROUND)  # Official background

    # Draw the contour
    # pygame.draw.circle(screen, WHITE, (CENTER_X, CENTER_Y), BOARD_RADIUS, 2)

    # Draw all the boxes
    for color, pos in zip(CONTOUR, box_positions):
        pygame.draw.circle(screen, color, pos, 18)


    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit()
