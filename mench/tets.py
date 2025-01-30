import pygame
import sys
import random

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

# Corrected main path extending to the edges and forming a plus shape
main_path = [
    (6, j)  for j in range(0,7) ]+ [(i,6) for i in range(5,-1,-1)]+[(0,j) for j in range(7,9)] +[(i,8) for i in range(1,7)]+[(6 , j) for j in range(9,15)] + [(i,14) for i in range(7,9)] + [(8,j) for j in range(13,7,-1)]+[(i,8) for i in range(9,15)]+[(14,j) for j in range(7,5,-1)]+[(i,6) for i in range(13,7,-1)]+[(8,j) for j in range(5,-1,-1)] + [(i,0) for i in range(7,5,-1)]
main_path = main_path[::-1]

# Player base areas
base_areas = {
    "red": [(i, j) for i in range(6) for j in range(6)],
    "blue": [(i, j) for i in range(9, 15) for j in range(6)],
    "green": [(i, j) for i in range(6) for j in range(9, 15)],
    "yellow": [(i, j) for i in range(9, 15) for j in range(9, 15)]
}

# Player pieces
player_pieces = {
    "red": {"r1": (1, 1), "r2": (1, 4), "r3": (4, 4), "r4": (4, 1)},
    "blue": {"b1": (1, 13), "b2": (4, 13), "b3": (1, 10), "b4": (4, 10)},
    "green": {"g1": (13, 1), "g2": (10, 4), "g3": (10, 1), "g4": (13, 4)},
    "yellow": {"y1": (13, 13), "y2": (10, 10), "y3": (13, 10), "y4": (10, 13)}
}

# Dice setup
dice_font = pygame.font.Font(None, 36)
dice_value = 1

# Track selected red piece
red_pieces = list(player_pieces["red"].keys())
selected_piece_index = 0  

# Draw the Ludo board
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)

            # Draw base areas
            if (row, col) in base_areas["red"]:
                pygame.draw.rect(screen, RED, rect)
            elif (row, col) in base_areas["blue"]:
                pygame.draw.rect(screen, BLUE, rect)
            elif (row, col) in base_areas["green"]:
                pygame.draw.rect(screen, GREEN, rect)
            elif (row, col) in base_areas["yellow"]:
                pygame.draw.rect(screen, YELLOW, rect)
            elif (row, col) in main_path:
                pygame.draw.rect(screen, WHITE, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)  
            else:
                pygame.draw.rect(screen, GRAY, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)

# Draw pieces
def draw_pieces():
    for color in player_pieces.keys():
        for piece in player_pieces[color]:
            x, y = player_pieces[color][piece]
            piece_color = RED if color == "red" else BLUE if color == "blue" else GREEN if color == "green" else YELLOW
            
            pygame.draw.circle(screen, piece_color, 
                (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

            # Draw outline around the selected red piece
            if color == "red" and piece == red_pieces[selected_piece_index]:
                pygame.draw.circle(screen, BLACK, 
                    (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2, 2)

# Move a piece
def move_piece(color, dice_roll, piece_name):
    if piece_name in player_pieces[color]:
        piece = player_pieces[color][piece_name]
        if piece in main_path:
            countor = 0
            for repeat in range(dice_roll):
                piece = player_pieces[color][piece_name]
                if piece == (0, 7):
                    rem_dice = dice_roll - countor
                    if rem_dice > 0:
                        move_piece_house(color, rem_dice, piece_name)
                        break
                    elif rem_dice <= 0:
                        break
                current_index = main_path.index(piece)
                new_index = (current_index + 1) % len(main_path)
                player_pieces[color][piece_name] = main_path[new_index]
                countor += 1

        elif piece in [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7)]:
            move_piece_house(color, dice_roll, piece_name)
        else:
            if dice_roll == 6:
                player_pieces[color][piece_name] = (0, 6)

def move_piece_house(color, dice_roll, piece_name):
    for dice in range(dice_roll):
        piece = player_pieces[color][piece_name]
        if piece == (4, 7):
            break
        new_piece = (piece[0] + 1, piece[1])
        player_pieces[color][piece_name] = new_piece

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
                move_piece("red", dice_value, red_pieces[selected_piece_index])
            
            elif event.key == pygame.K_LEFT:  # Select previous piece
                selected_piece_index = (selected_piece_index - 1) % len(red_pieces)
            
            elif event.key == pygame.K_RIGHT:  # Select next piece
                selected_piece_index = (selected_piece_index + 1) % len(red_pieces)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
