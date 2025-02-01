import pygame
import sys
import random
from boardAndPiece import  draw_board , draw_pieces
from movment import move_piece
from gameSetup import playersColor


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



# Dice setup
dice_font = pygame.font.Font(None, 36)
dice_value = 0


turn = 0 

def changeTurn():
    global turn
    colorTurn = playersColor[turn]
    turn = (turn + 1) % len(playersColor)
    return colorTurn

colorTurn = changeTurn()




# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    # Draw board and pieces
    draw_board()
    draw_pieces()


    # Dice display
    dice_text = dice_font.render(f"Dice: {dice_value}", True, BLACK)
    screen.blit(dice_text, (WIDTH // 2 - dice_text.get_width() // 2, HEIGHT - 40))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Roll the dice
                dice_value = random.randint(1, 6)
                
                move_piece(colorTurn, dice_value , f"{colorTurn[0]}"+f"{2}")
                if dice_value != 6:
                    colorTurn = changeTurn()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
