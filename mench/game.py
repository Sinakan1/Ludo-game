turn = 0 
def game ():
    import pygame
    import sys
    import random
    from boardAndPiece import  draw_board , draw_pieces,main_path
    from movment import move_piece
    from gameSetup import playersColor
    from player import player_pieces
    from winner import winning

    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    WIDTH, HEIGHT = 900, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ludo Game")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    FAKERED = (200, 0, 0)
    RED = (255, 0, 0)
    DARK_RED = (159, 96, 96)
    BLUE = (0, 0, 255)
    DARK_BLUE = (102, 102, 153)
    GREEN = (0, 255, 0)
    DARK_GREEN = (83, 172, 83)
    YELLOW = (236, 182, 19)
    DARK_YELLOW = (198, 163, 57)
    GRAY = (200, 200, 200)

    # Board setup
    CELL_SIZE = 40
    ROWS, COLS = 15, 15

    # Dice setup
    dice_font = pygame.font.Font(None, 36)
    dice_value = 0



    def changeTurn():
        # check if the player has won
        global turn
        colorTurn = playersColor[turn]

        turn = (turn + 1) % len(playersColor)
        return colorTurn
        
        
    colorTurn = changeTurn()


    # index
    i = 0
    # Main game loop
    clock = pygame.time.Clock()
    running = True
    moved = True #check is turn is over or not 
    while running:
        screen.fill(WHITE)

        # Draw board and pieces
        draw_board()
        draw_pieces()
        colorTokens = list(player_pieces[colorTurn].keys())
        selected_pieces = colorTokens[i]
        selected_pieces_pos = player_pieces[colorTurn][selected_pieces]["pos"]
        selected_pieces_played = player_pieces[colorTurn][selected_pieces]["play"]
        x,y = selected_pieces_pos
        circle = pygame.draw.circle(screen , (0,0,0) ,(x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2),18,3 )

        # Dice display
        dice_text = dice_font.render(f"Dice: {dice_value}", True, BLACK)
        screen.blit(dice_text, (WIDTH // 2 - dice_text.get_width() // 2, HEIGHT - 40))
        
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE and moved:  # Roll the dice
                    dice_value = random.randint(1, 6)
                    dice_text = dice_font.render(f"Dice: {dice_value}", True, WHITE)
                    screen.blit(dice_text, (WIDTH // 2 - dice_text.get_width() // 2, HEIGHT - 40))
                    moved = False

                elif event.key == pygame.K_RETURN and not moved:
                    moved = move_piece(colorTurn, dice_value , selected_pieces)
                    print(moved)
                    if moved:
                        if dice_value != 6:
                            dice_value = ""
                            winning(colorTurn)
                            colorTurn = changeTurn()
                        
                        else:
                            dice_value = ""
                            pass
                    else :
                        pass

                elif event.key == pygame.K_BACKSPACE :
                    colorTurn = changeTurn()
                    dice_value = ""
                    moved = True
                        
                elif event.key == pygame.K_LEFT:
                    colorTokens = list(player_pieces[colorTurn].keys())
                    if i == 0 : i = 3 
                    else : i -= 1

                elif event.key == pygame.K_RIGHT:
                    colorTokens = list(player_pieces[colorTurn].keys())
                    if i == 3 : i = 0 
                    else : i += 1
                    

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()
