# ... (autre code)

elif event.type == pygame.MOUSEBUTTONDOWN:
    # ... (autre code)

    # When player clicks on the chosen case
    else:
        for idx, pos in enumerate(positions):
            # Check if the click is inside the red circle
            if pygame.mouse.get_pos()[0] >= pos[0] - BOX_RADIUS - 3 and pygame.mouse.get_pos()[0] <= pos[0] + BOX_RADIUS + 3:
                if pygame.mouse.get_pos()[1] >= pos[1] - BOX_RADIUS - 3 and pygame.mouse.get_pos()[1] <= pos[1] + BOX_RADIUS + 3:
                    if idx in available_cases:
                        positions_chosen.append(idx)
                        print(f"Position du {player.name} : {player.position}")
                        print("Case choisie", idx)
                        print("Positions choisies :", positions_chosen)
                        player.position = positions_chosen[-1]
                        print(f"Position du {player.name} : {player.position}")

                        theme, scoring = check_current_case(player)
                        if theme != "Again":
                            question = BDD.obtenir_question(theme)
                            # Handle the question and its options
                            if event.type == pygame.KEYDOWN:
                                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                                    # Map the key press to the corresponding answer
                                    answer_options = question.options
                                    selected_answer = answer_options[int(event.unicode) - 1]

                        # Clear the entire board
                        screen.fill(BACKGROUND)

                        # Redraw each box with its original color
                        for idx, pos in enumerate(positions):
                            box_color = BOX_TYPE_TO_COLOR[network.nodes[idx]['box_type']]
                            pygame.draw.circle(screen, box_color, pos, BOX_RADIUS)

                        # Draw the player's circle in the new position
                        pygame.draw.circle(screen, RING_COLOR, positions[player.position], BOX_RADIUS + RING_WIDTH, RING_WIDTH)

                        # Update the screen
                        pygame.display.flip()

                        # Print the chosen theme and scoring
                        print("Thème choisi :", theme)
                        print("scoring :", scoring)
                        attrs = question.__dict__
                        for k, v in attrs.items():
                            print(k, ":", v)
