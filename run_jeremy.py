from ui_functions import initialize_display, get_player_names, display_board
from game_functions import init_game
import pygame, sys
from config import BACKGROUND, BORDER_THICKNESS, BOX_RADIUS, BOX_TYPE_TO_COLOR,\
      HEIGHT, RING_COLOR, RING_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, WIDTH
from class_player import Player
from board_network import create_game_network

# Initialize PyGame and set it
pygame.init()

G = create_game_network()

screen, board_zone, info_zone, score_zone, question_zone, font = initialize_display()

input_box = pygame.Rect(600, 50, 200, 32)
dice_box = pygame.Rect(900, 10, 50, 50)  # Positioned in the right zone
max_players = 1
active = False
text = ''
player_names = []
instructions = "Enter your name"
start_game = False
dice_result = '6'
available_cases = []

while True:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            # If the user clicked on the input_box rect.
            if input_box.collidepoint(event.pos):
                active = True
            elif dice_box.collidepoint(event.pos):
                dice_result = str(player.lancer_de())
                available_cases = player.give_new_positions(G, int(dice_result))
                print(available_cases)



        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    start_game = True
                    if text:
                        if text not in player_names:
                            player_names.append(text)
                            player = Player(text)
                            print(player.name)
                        if len(player_names) >= max_players:
                            player_names = player_names
                    else:
                        player_names = player_names
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
                winner, network, positions, bdd, players, game_state = init_game(player_names)
                
    if start_game : 
        for idx, pos in enumerate(positions):
            # Get the color from the network nodes
            box_color = BOX_TYPE_TO_COLOR[network.nodes[idx]['box_type']]
            pygame.draw.circle(screen, box_color, pos, BOX_RADIUS)

        

    


    # Clear the input area (600px wide, 100px high)
    pygame.draw.rect(screen, BACKGROUND, (600, 0, 600, 100))
    
    # Render and display instructions
    instruction_surface = font.render(instructions, True, WHITE)
    screen.blit(instruction_surface, (610, 10))  # Slightly offset within the right zone

    # Render and display current input text
    txt_surface = font.render(text, True, (255, 255, 255))
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(screen, (255, 255, 255), input_box, BORDER_THICKNESS)  # Draw the input box

    dice_display = font.render(dice_result, True, WHITE)
    screen.blit(dice_display, (920, 25))
    pygame.draw.rect(screen, (255, 255, 255), dice_box, BORDER_THICKNESS)

    pygame.display.flip()
