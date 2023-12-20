import pygame

from typing import List, Tuple

from board_frontend import positions  # Only for demo purposes
from config import BOX_RADIUS, RING_COLOR, RING_WIDTH, WIDTH, HEIGHT


def is_within_circle(center_x:int, center_y:int, radius:int, x:int, y:int) -> bool:
    """
    Utility function to check if the click is done within a given circle
    """
    return (x - center_x) ** 2 + (y - center_y) ** 2 < radius ** 2


def display_new_positions(screen, indexes: List[int]):
    """
    Shows on board on which boxes a player can move after rolling the dice
    """
    for idx in indexes:
        pos = positions[idx]
        pygame.draw.circle(screen, RING_COLOR, pos, BOX_RADIUS, RING_WIDTH)


def choose_new_position(screen, indexes: List[int]) -> int:
    """
    Allows the current player to choose its new position 
    by clicking on displayed boxes
    """
    for event in pygame.event.get()
    pos_and_indexes = {positions[idx]: idx for idx in indexes}
    # print(pos_and_indexes)
    for pos in pos_and_indexes:
        pos_x, pos_y = pos
        if is_within_circle()
    

# Example usage in the event loop
for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
        
        mouse_x, mouse_y = event.pos
        if is_within_circle(circle_center_x, circle_center_y, circle_radius, mouse_x, mouse_y):
            print("Circle was clicked!")
