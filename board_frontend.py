import math

import pygame

from board import CASES


# GRAPHICAL EFFECTS
BACKGROUND = (29, 62, 71)
WHITE = (255, 255, 255)
BLUE = (68, 202, 219)
ORANGE = (253, 139, 80)
GREEN = (101, 183, 65)
YELLOW = (254, 232, 37)
PINK = (252, 111, 163)
BROWN = (190, 124, 67)
GREY = (236, 225, 205)

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
# Board Screen
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TrivIA Pursuit Board")

# Board Circle
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
    screen.fill(BACKGROUND)  # White background

    # Draw the contour
    # pygame.draw.circle(screen, WHITE, (CENTER_X, CENTER_Y), BOARD_RADIUS, 2)

    # Draw the circular boxes on the contour
    for color, pos in zip(CONTOUR, box_positions):
        pygame.draw.circle(screen, color, pos, 18)

    # Draw the three bridges
    for n_bridge in range(3):
        # Draw the diameters
        begin_pos = box_positions[n_bridge * 7]
        end_pos = box_positions[n_bridge * 7 + 21]
        # pygame.draw.line(screen, WHITE, begin_pos, end_pos, 2)
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
