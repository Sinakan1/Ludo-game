import pygame
from player import player_pieces, startCell , endHouse

# Initialize Pygame
pygame.init()

# Corrected main path extending to the edges and forming a plus shape
main_path = [
    (6, j)  for j in range(0,7) ]+ [(i,6) for i in range(5,-1,-1)]+[(0,j) for j in range(7,9)] +[(i,8) for i in range(1,7)]+[(6 , j) for j in range(9,15)] + [(i,14) for i in range(7,9)] + [(8,j) for j in range(13,7,-1)]+[(i,8) for i in range(9,15)]+[(14,j) for j in range(7,5,-1)]+[(i,6) for i in range(13,7,-1)]+[(8,j) for j in range(5,-1,-1)] + [(i,0) for i in range(7,5,-1)]
main_path = main_path[::-1]

# extra_path = [(6,0), (0,7) ,(14,7) , (7,7)]

# main_path.extend(extra_path)



# Player base areas (remove grid lines inside bases)
base_areas = {
    "red": [(i, j) for i in range(6) for j in range(6)],
    "blue": [(i, j) for i in range(9, 15) for j in range(6)],
    "green": [(i, j) for i in range(6) for j in range(9, 15)],
    "yellow": [(i, j) for i in range(9, 15) for j in range(9, 15)],
    "circles": [(63 , 63) , (180,63) , (180,180) , (63,180) , (540,63),(423,63),(540,180),(423,180) ,(63,540),(63,423),(180,540),(180,423), (540,540),(423,423),(540,423),(423,540)]
}

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

# pieces Radius 

circle_radius = CELL_SIZE // 3

# Font setup
font = pygame.font.Font(None, 22)  # Default font

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

            elif (col,row) == startCell["red"] : 
                pygame.draw.rect(screen, DARK_RED , rect)
                pygame.draw.rect(screen, BLACK, rect, 1)  # Keep grid lines inside path

            elif (col,row) == startCell["blue"] : 
                pygame.draw.rect(screen, DARK_BLUE , rect)
                pygame.draw.rect(screen, BLACK, rect, 1)  # Keep grid lines inside path

            elif (col,row) == startCell["yellow"] : 
                pygame.draw.rect(screen, DARK_YELLOW , rect)
                pygame.draw.rect(screen, BLACK, rect, 1)  # Keep grid lines inside path

            elif (col,row) == startCell["green"] : 
                pygame.draw.rect(screen, DARK_GREEN , rect)
                pygame.draw.rect(screen, BLACK, rect, 1)  # Keep grid lines inside path

            # Draw the main path
            elif (row, col) in main_path :
                pygame.draw.rect(screen, WHITE, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)  # Keep grid lines inside path
            else:
                pygame.draw.rect(screen, GRAY, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)  # Keep grid lines for normal cells
            

    for circle in base_areas["circles"]:
        pygame.draw.circle(screen,(255,255,255),circle,25,0)
        

# Draw pieces
def draw_pieces():
    for color in player_pieces.keys():
        i = 1 
        for piece in player_pieces[color]:
            x, y = player_pieces[color][piece]["pos"]
            pygame.draw.circle(
                screen, RED if color == "red" else BLUE if color == "blue" else GREEN if color == "green" else YELLOW,
                pos := (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2),
                circle_radius + 3
            ) 
            text_surface = font.render(f"{i}" , True, WHITE)
            text_rect = text_surface.get_rect(center=pos)
            screen.blit(text_surface,text_rect)
            i += 1 
draw_pieces()