from ui_functions import initialize_display, get_player_names, display_board, display_question_and_handle_answer, display_scores
from game_functions import init_game, check_current_case
import pygame, sys
from config import BACKGROUND, BORDER_THICKNESS, BOX_RADIUS, BOX_TYPE_TO_COLOR, HEIGHT, RING_COLOR, RING_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, WIDTH, RED, THEMES, INDEX_TO_BOX_TYPE, THEME_TO_POINT
from class_player import Player
from board_network import create_game_network
from  class_gestion_bdd import GestionBDD

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
positions_chosen = []

BDD = GestionBDD('questions.db')
# Définir les coordonnées de chaque réponse
response_1 = (495, 541)
response_2 = (541, 541)
response_3 = (495, 577)
response_4 = (541, 577)
# Create text surfaces for the numbers
font_size = 25  # Adjust the font size as needed
font_numbers = pygame.font.SysFont(None, font_size)
text_1 = font_numbers.render(" 1", True, RED)
text_2 = font_numbers.render(" 2", True, RED)
text_3 = font_numbers.render(" 3", True, RED)
text_4 = font_numbers.render(" 4", True, RED)
# Créer des rectangles à partir de ces coordonnées
width = 20  # Choisir la largeur appropriée pour les zones de réponse
height = 20  # Choisir la hauteur appropriée pour les zones de réponse

# Créer les rectangles à partir des coordonnées de clic
rect_response_1 = pygame.Rect(response_1[0], response_1[1], width, height)
rect_response_2 = pygame.Rect(response_2[0], response_2[1], width, height)
rect_response_3 = pygame.Rect(response_3[0], response_3[1], width, height)
rect_response_4 = pygame.Rect(response_4[0], response_4[1], width, height)
selected_answer = None
question_answered = False  # Variable de contrôle



while True:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            selected_answer = None
             # Vérification si l'utilisateur a cliqué sur une réponse
            if rect_response_1.collidepoint(event.pos):
                selected_answer = 1
            elif rect_response_2.collidepoint(event.pos):
                selected_answer = 2
            elif rect_response_3.collidepoint(event.pos):
                selected_answer = 3
            elif rect_response_4.collidepoint(event.pos):
                selected_answer = 4

            # Vérification de la réponse sélectionnée
            if selected_answer is not None and not question_answered:
                # Obtenez la réponse correspondant au chiffre sélectionné depuis la question
                selected_option = question.options[selected_answer - 1]

                # Vérifiez si la réponse sélectionnée correspond à la réponse correcte
                if selected_option == question.answer:
                    # Si la réponse est correcte
                    print("Bonne réponse !")
                    player.score_point(question.theme)  # Marquer un point pour la question
                    question_answered = True
                    # Mettez ici votre logique de scoring pour une bonne réponse

                    # Afficher "Tu as gagné ! Relance le dé" après avoir gagné
                    winning_text = font.render("Tu as gagné ! Relance le dé", True, WHITE)
                    screen.blit(winning_text, (question_zone.x, question_zone.y))  # Afficher le message de victoire
                    pygame.display.flip()  # Mettre à jour l'écran pour afficher le message
                    last_question = question
                    # Masquer la question après avoir affiché le message de victoire
                    display_question_and_handle_answer(screen, font, None, display_question=False, display_winning_text=True)
                    selected_answer = None 
                    question = None
                    
                    pygame.display.flip()  # Mettre à jour l'écran pour afficher le message

                else:
                    display_question_and_handle_answer(screen, font, question)
                        
                                
            
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
                            if theme == "Again":
                                # Affichage du message "Relance le dé"
                                roll_dice_message = font.render("Relance le dé", True, WHITE)
                                screen.blit(roll_dice_message, (question_zone.x, question_zone.y))  # Position à ajuster
                                pygame.display.flip()

                                
                            if theme != "Again":
                                question = BDD.obtenir_question(theme)
                                display_question_and_handle_answer(screen, font, question)
                                last_question = None
                            question_answered = False
                                 
                            
                                        
                            
                            
       
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
        # drawing board
        for idx, pos in enumerate(positions):
            # Get the color from the network nodes
            box_color = BOX_TYPE_TO_COLOR[network.nodes[idx]['box_type']]
            pygame.draw.circle(screen, box_color, pos, BOX_RADIUS)
            display_scores(screen, font, player)
        
        # Displaying scores
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
    
    # Display box of answers
    response_color = (255, 255, 255)  # Couleur blanche pour les contours
    border_thickness = 2  # Épaisseur du contour, à ajuster selon votre choix
    # Dessiner les contours des rectangles
    pygame.draw.rect(screen, response_color, rect_response_1, border_thickness)
    pygame.draw.rect(screen, response_color, rect_response_2, border_thickness)
    pygame.draw.rect(screen, response_color, rect_response_3, border_thickness)
    pygame.draw.rect(screen, response_color, rect_response_4, border_thickness)
    
    # Draw text on the screen
    screen.blit(text_1, response_1)
    screen.blit(text_2, response_2)
    screen.blit(text_3, response_3)
    screen.blit(text_4, response_4)
    
    
    dice_display = font.render(dice_result, True, WHITE)
    screen.blit(dice_display, (920, 25))
    pygame.draw.rect(screen, (255, 255, 255), dice_box, BORDER_THICKNESS)

    
    pygame.display.flip()