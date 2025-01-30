import pygame
import sys
import random
from player import player_pieces
from board import main_path , draw_board , draw_pieces
from movment import move_piece , move_piece_house


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
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)

# Board setup
CELL_SIZE = 40
ROWS, COLS = 15, 15




# Dice setup
dice_font = pygame.font.Font(None, 36)
dice_value = 1






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
                move_piece("red", dice_value)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
