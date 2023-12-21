from ui_functions import initialize_display, get_player_names, display_board, display_question_and_handle_answer, display_scores
from game_functions import init_game, check_current_case
import pygame, sys
from config import BACKGROUND, BORDER_THICKNESS, BOX_RADIUS, BOX_TYPE_TO_COLOR, HEIGHT, RING_COLOR, RING_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, WIDTH, RED, INDEX_TO_BOX_TYPE
from class_player import Player
from board_network import create_game_network
from  class_gestion_bdd import GestionBDD

# Initialize PyGame and set it
pygame.init()

G = create_game_network()

screen, board_zone, info_zone, score_zone, question_zone, font = initialize_display()

input_box = pygame.Rect(600, 50, 200, 32)
answer_box = pygame.Rect(600, 420, 80, 80 )
dice_box = pygame.Rect(900, 10, 50, 50)  # Positioned in the right zone
max_players = 1
active = False
text = ''
player_names = []
instructions = "Enter your name"
start_game = False
dice_result = '6'
available_cases = []
positions_chosen = []
BDD = GestionBDD('questions.db')

while True:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            # If the user clicked on the input_box rect.
            if input_box.collidepoint(event.pos):
                active = True
            # When player click on the dice
            elif dice_box.collidepoint(event.pos):
                dice_result = str(player.lancer_de())
                available_cases = player.give_new_positions(G, int(dice_result))
                print(available_cases)
                for i in available_cases:
                    pygame.draw.circle(screen, RED, (positions[i][0], positions[i][1]), BOX_RADIUS+ 3, 3)
            
            # When player click on the case choosen
            else:
                for idx, pos in enumerate(positions):
                    # Vérifier si le clic est à l'intérieur du cercle entouré en rouge
                    if pygame.mouse.get_pos()[0] >= pos[0] - BOX_RADIUS - 3 and pygame.mouse.get_pos()[0] <= pos[0] + BOX_RADIUS + 3:
                        if pygame.mouse.get_pos()[1] >= pos[1] - BOX_RADIUS - 3 and pygame.mouse.get_pos()[1] <= pos[1] + BOX_RADIUS + 3:
                            if idx in available_cases:
                                positions_chosen.append(idx)
                                print(f"Position du {player.name} : {player.position}")
                                print("Case choisie", idx)
                                print("Positions choisies :", positions_chosen)
                                player.position = positions_chosen[-1]
                                print(f"Position du {player.name} : {player.position}")
                                
                               
                            
                            # Effacer tout le plateau
                            screen.fill(BACKGROUND)

                            # Redessiner chaque case avec sa couleur d'origine
                            for idx, pos in enumerate(positions):
                                box_color = BOX_TYPE_TO_COLOR[network.nodes[idx]['box_type']]
                                pygame.draw.circle(screen, box_color, pos, BOX_RADIUS)

                            # Dessiner le cercle du joueur dans sa nouvelle position
                            pygame.draw.circle(screen, RING_COLOR, positions[player.position], BOX_RADIUS + RING_WIDTH, RING_WIDTH)

                            # Mettre à jour l'écran
                            pygame.display.flip()
                            
                            theme, scoring = check_current_case(player)
                            if theme != "Again":
                                question = BDD.obtenir_question(theme)
                                display_question_and_handle_answer(screen, font, question)
                                 
                                if answer_box.collidepoint(event.pos):
                                    active = True                           
                                    if event.type == pygame.KEYDOWN:
                                        if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                                            selected_answer = question.options[int(event.unicode)-1]
                                            print(selected_answer)
                                        
                            # print du theme
                            print("Thème choisi :", theme)
                            print("scoring :", scoring)
                            attrs = question.__dict__

                            for k, v in attrs.items():
                                print(k, ":", v)
                            
                            
                            
                            
                              
                        
            



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
        # drawing board
        for idx, pos in enumerate(positions):
            # Get the color from the network nodes
            box_color = BOX_TYPE_TO_COLOR[network.nodes[idx]['box_type']]
            pygame.draw.circle(screen, box_color, pos, BOX_RADIUS)
            display_scores(screen, font, player)
            

        

    


    # Clear the input area (600px wide, 100px high)
    pygame.draw.rect(screen, BACKGROUND, (600, 0, 600, 100))
    
    # Render and display instructions
    instruction_surface = font.render(instructions, True, WHITE)
    screen.blit(instruction_surface, (610, 10))  # Slightly offset within the right zone

    # Render and display current input text
    txt_surface = font.render(text, True, (255, 255, 255))
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(screen, (255, 255, 255), input_box, BORDER_THICKNESS)  # Draw the input box
    
    
    answer_surface = font.render(text, True, (255, 255, 255))
    screen.blit(answer_surface, (answer_box.x + 5, answer_box.y + 5))
    pygame.draw.rect(screen, (255, 255, 255), answer_box, BORDER_THICKNESS)  # Draw the input box
    
    

    dice_display = font.render(dice_result, True, WHITE)
    screen.blit(dice_display, (920, 25))
    pygame.draw.rect(screen, (255, 255, 255), dice_box, BORDER_THICKNESS)
    
    

    pygame.display.flip()
