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

# extra_path = [(7,0), (0,7) ,(14,7) , (7,7)]

# main_path.extend(extra_path)

print(main_path)


# Player base areas (remove grid lines inside bases)
base_areas = {
    "red": [(i, j) for i in range(6) for j in range(6)],
    "blue": [(i, j) for i in range(6) for j in range(9, 15)],
    "green": [(i, j) for i in range(9, 15) for j in range(6)],
    "yellow": [(i, j) for i in range(9, 15) for j in range(9, 15)],
}

# Player pieces
player_pieces = {
    "red": [(1, 6)],
    "blue": [(8, 1)],
    "green": [(6, 13)],
    "yellow": [(13, 8)]
}

# Dice setup
dice_font = pygame.font.Font(None, 36)
dice_value = 1

# Draw the Ludo board
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)

            # Draw base areas for players without grid lines
            if (row, col) in base_areas["red"]:
                pygame.draw.rect(screen, RED, rect)
            elif (row, col) in base_areas["blue"]:
                pygame.draw.rect(screen, BLUE, rect)
            elif (row, col) in base_areas["green"]:
                pygame.draw.rect(screen, GREEN, rect)
            elif (row, col) in base_areas["yellow"]:
                pygame.draw.rect(screen, YELLOW, rect)
            # Draw the main path
            elif (row, col) in main_path:
                pygame.draw.rect(screen, WHITE, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)  # Keep grid lines inside path
            else:
                pygame.draw.rect(screen, GRAY, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)  # Keep grid lines for normal cells

# Draw pieces
def draw_pieces():
    for color, pieces in player_pieces.items():
        for piece in pieces:
            x, y = piece
            pygame.draw.circle(
                screen, RED if color == "red" else BLUE if color == "blue" else GREEN if color == "green" else YELLOW,
                (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2),
                CELL_SIZE // 3
            )

# Move a piece
def move_piece(color, dice_roll):
    if player_pieces[color]:
        piece = player_pieces[color][0]  # Get the first piece of the player
        if piece in main_path:  # Check if the piece is on the main path
            countor = 0
            for repeat in range(dice_roll):
                piece = player_pieces[color][0]
                if piece == (0,7) :
                    rem_dice = dice_roll - countor
                    if rem_dice > 0:
                        break
                    elif rem_dice <= 0 :
                        break                     
                current_index = main_path.index(piece)  # Find current position in the main path
                new_index = (current_index + 1) % len(main_path)  # Calculate new position
                print(new_index)
                player_pieces[color][0] = main_path[new_index]  # Update the piece position
                countor += 1
        else:
            # If the piece is not on the main path, move it to the starting position
            player_pieces[color][0] = main_path[0]


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
