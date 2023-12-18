import math

import pygame

from board import CASES


# GRAPHICAL EFFECTS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (33, 156, 144)
ORANGE = (255, 152, 0)
GREEN = (101, 183, 65)
YELLOW = (244, 232, 105)
PINK = (255, 105, 105)
BROWN = (167, 49, 33)
GREY = (218, 212, 181)

COLOR_MAP = {
    "*Spe": BROWN,
    "Spe": BROWN,
    "*SQL": BLUE,
    "SQL": BLUE,
    "*IA": ORANGE,
    "IA": ORANGE,
    "*Shell": YELLOW,
    "Shell": YELLOW,
    "*Git": PINK,
    "Git": PINK,
    "*Python": GREEN,
    "Python": GREEN,
    "Again": GREY
}
CONTOUR = [COLOR_MAP[case] for case in CASES]
BRIDGES = [
    [BROWN, YELLOW, PINK, ORANGE, BLUE, GREEN, WHITE,
     ORANGE, PINK, GREEN, BLUE, BROWN, YELLOW],
    [BLUE, PINK, GREEN, YELLOW, ORANGE, BROWN, WHITE,
      YELLOW, GREEN, BROWN, ORANGE, BLUE, PINK],
    [ORANGE, GREEN, BROWN, PINK, YELLOW, BLUE, WHITE,
      PINK, BROWN, BLUE, YELLOW, ORANGE, GREEN]
]

# DIMENSIONS
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TrivIA Pursuit Board")

BOARD_RADIUS = 250
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

# Function to calculate positions on the circle
def calculate_positions(num_points):
    positions = []
    angle = 0
    rotation = 2 * math.pi / num_points

    for _ in range(num_points):
        x = CENTER_X + int(BOARD_RADIUS * math.cos(angle))
        y = CENTER_Y + int(BOARD_RADIUS * math.sin(angle))
        positions.append((x, y))
        angle += rotation

    return positions

# For the particular case of our board
box_positions = calculate_positions(42)


# MAIN RUN
running = True
while running:
    screen.fill(BLACK)  # White background

    # Draw the contour
    pygame.draw.circle(screen, WHITE, (CENTER_X, CENTER_Y), BOARD_RADIUS, 2)

    # Draw the circular boxes on the contour
    for color, pos in zip(CONTOUR, box_positions):
        pygame.draw.circle(screen, color, pos, 18)

    # Draw the three bridges
    for n_bridge in range(3):
        # Draw the diameters
        begin_pos = box_positions[n_bridge * 7]
        end_pos = box_positions[n_bridge * 7 + 21]
        pygame.draw.line(screen, WHITE, begin_pos, end_pos, 2)
        # Draw the boxes on the diameters
        for n_box in range(1, 12):
            fraction = n_box / 12
            box_x = begin_pos[0] + fraction * (end_pos[0] - begin_pos[0])
            box_y = begin_pos[1] + fraction * (end_pos[1] - begin_pos[1])
            pygame.draw.circle(
                screen,
                BRIDGES[n_bridge][n_box],
                (int(box_x), int(box_y)),
                18)

    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit()
