from collections import deque
from random import randint, shuffle
from typing import Any, List, Tuple

import pygame

from board_coordinates import calculate_all_pos
from class_player import Player
from config import BACKGROUND, BORDER_THICKNESS, BOX_RADIUS, BOX_TYPE_TO_COLOR,\
      RING_COLOR, RING_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE


def initialize_display() -> Tuple[pygame.surface.Surface, pygame.font.Font]:
    """
    Initialize screen and define global settings about font used.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("TrivIA")

    # Filling the screen with background color
    screen.fill(BACKGROUND)
    
    # Font settings
    font_family = 'Verdana'
    font_size = 16

    font = pygame.font.SysFont(font_family, font_size)

    return screen, font


def get_player_names(screen, font) -> List[str]:
    """
    Gather player names via UI
    """
    input_box = pygame.Rect(600, 50, 200, 32)  # Positioned in the right zone
    max_players = 6
    active = False
    text = ''
    player_names = []
    instructions = "Next player name? (End with ENTER, 6 Max)"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return player_names
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if text:
                            if text not in player_names:
                                player_names.append(text)
                                text = ''
                            if len(player_names) >= max_players:
                                return player_names
                        else:
                            return player_names
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        # Clear the input area (600px wide, 100px high)
        pygame.draw.rect(screen, BACKGROUND, (600, 0, 600, 100))
        
        # Render and display instructions
        instruction_surface = font.render(instructions, True, WHITE)
        screen.blit(instruction_surface, (610, 10))  # Slightly offset within the right zone

        # Render and display current input text
        txt_surface = font.render(text, True, (255, 255, 255))
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, (255, 255, 255), input_box, BORDER_THICKNESS)  # Draw the input box

        pygame.display.flip()


def display_board(screen, network, positions: List[Tuple[int, int]]) -> None:
    """
    Do you really not get what this does?
    """
    # Draw all the boxes
    for idx, pos in enumerate(positions):
        # Get the color from the network nodes
        box_color = BOX_TYPE_TO_COLOR[network.nodes[idx]['box_type']]
        pygame.draw.circle(screen, box_color, pos, BOX_RADIUS)


# TODO: THIS IS A TOY VERSION
# Especially, this needs as input the deque of players
def display_scores(screen, font, players) -> None:
    # Define the area for displaying scores
    score_area = pygame.Rect(600, 100, 600, 240)  # Below the top zone

    # Clear the score area
    pygame.draw.rect(screen, BACKGROUND, score_area)

    # Draw the border around the score area
    pygame.draw.rect(screen, WHITE, score_area, BORDER_THICKNESS)

    # Starting Y position for the first line of text
    start_y = 110

    # Display each player's score
    for player_name, score in scores.items():
        score_text = f"{player_name}: {score}"
        text_surface = font.render(score_text, True, WHITE)  # Use the border color for text
        screen.blit(text_surface, (610, start_y))
        start_y += 30  # Increment Y position for next line

    # Update the display for the score area
    pygame.display.update(score_area)


def display_dice_result(screen, font, player: Player, dice_result: int):
    result_area = pygame.Rect(600, 0, 600, 100)

    # Clear the area first
    pygame.draw.rect(screen, BACKGROUND, result_area)

    # Prepare and display the dice result
    result_text = f"{player.name} rolled a {dice_result}"
    text_surface = font.render(result_text, True, (255, 255, 255))  # White text
    screen.blit(text_surface, (610, 10))

    # Update the display to show the dice result
    pygame.display.update(result_area)


def display_new_positions(screen, indexes: List[int], positions: List[Tuple[int, int]]) -> None:
    """
    Shows on board on which boxes a player can move after rolling the dice
    """
    for idx in indexes:
        pos = positions[idx]
        pygame.draw.circle(screen, RING_COLOR, pos, BOX_RADIUS, RING_WIDTH)
    

# TODO CHOOSE NEW POSITION
    

# TODO DISPLAY_NEW_POSITION








def display_question_and_handle_answer(screen, font, background_color, question, answer_options):
    # Define the areas for question and answers
    question_area = pygame.Rect(600, 350, 600, 100)  # Top part of the bottom zone
    answer_area = pygame.Rect(600, 450, 600, 160)   # Bottom part of the bottom zone

    # Clear the areas
    pygame.draw.rect(screen, background_color, question_area)
    pygame.draw.rect(screen, background_color, answer_area)

    # Display the question
    question_text = font.render(question, True, (255, 255, 255))  # White text
    screen.blit(question_text, (610, 360))  # Position the text in the question area

    # Display the answer options
    start_y = 460
    for i, option in enumerate(answer_options, 1):
        answer_text = f"{i}. {option}"
        text_surface = font.render(answer_text, True, (255, 255, 255))  # White text
        screen.blit(text_surface, (610, start_y))
        start_y += 40  # Increment for next option

    pygame.display.update([question_area, answer_area])  # Update both areas

    # Handle answer input
    selected_answer = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                    # Map the key press to the corresponding answer
                    selected_answer = answer_options[int(event.unicode) - 1]
                    return selected_answer



# # Initialize PyGame
# screen, font = initialize_display()
# print(type(screen))
# print(type(font))

# ## INITIALIZE THE GAME
# # Get player names
# player_names = get_player_names(screen, font)
# print("Player Names:", player_names)

# # Initialize turn_order
# shuffle(player_names)
# player_turns = deque(player_names)
# print("TURN ORDER")
# print(player_turns)

# ## TURN LOGIC
# # Roll the dice
# dice_roll = randint(1, 6)
# print(f"{dice_roll = }")

# # Display dice roll
# display_dice_result(screen, font, BACKGROUND, player_names[0], dice_roll)

# pygame.quit()
