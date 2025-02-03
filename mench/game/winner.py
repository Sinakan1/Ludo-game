from player import player_pieces
import pygame 

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Winner")




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

# font init
font = pygame.font.Font(None, 36)


# check if the player has won   
def winning(color):
    for piece  in player_pieces[color]:
        if player_pieces[color][piece]["play"] == False:
            return False
    else:
        if displayWin(color):
            return True


def displayWin(color):
    while True : 
            screen.fill(BLACK)
            text1 = font.render("Player: ", True, WHITE)
            textColor = font.render(f"{color.upper()}", True, f"{color.upper()}")
            text2 = font.render(" has won the game", True, WHITE)
            textExit = font.render("Press any key to exit", True, WHITE)
            textMenu = font.render("except M , M Is for Menu", True, WHITE)
            screen.blit(text1,(WIDTH//2  - 100, HEIGHT//2) )
            screen.blit(textColor,(WIDTH//2 + 150 - 100, HEIGHT//2) )
            screen.blit(text2,(WIDTH//2 -100 , HEIGHT //2 + 30 ) )
            screen.blit(textExit,(WIDTH//2 - 120 , HEIGHT //2 + 150 ) )
            screen.blit(textMenu,(WIDTH//2 - 120 , HEIGHT //2 + 200 ) )
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event:
                    if event.key == pygame.K_m:
                        return True
                    else:    
                        pygame.quit()
                        exit()
