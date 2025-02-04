import pygame
import sys
import os

folder_path = os.path.abspath("game")  # Adjust the path as needed

# Add the folder to sys.path
sys.path.append(folder_path)

# Now you can import the module
from game import game





pygame.init()

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

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))



background = pygame.image.load("assets/background.png")
pointer = pygame.image.load("assets/pointer.png")
pointer =pygame.transform.scale(pointer, (50, 50))
font = pygame.font.Font("assets/Font/PixelifySans-Regular.ttf" ,50)
Y = 300
mohtava = [("PLAY" ,(160 , Y)),("HOW TO PLAY" , (80, Y + 60)),("QUIT" , (163, Y+120))]
pointerPos = [(110, Y+8), (20, Y + 68), (110, Y + 128)]



def mainMenu():
    index = 0 

    while True:
        screen.blit(background, (0, 0))
        screen.blit(pointer, pointerPos[index])
        for object in mohtava:
            text = font.render(object[0], True, BLACK)
            screen.blit(text, object[1])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_UP:
                    index = (index - 1) % 3
                elif event.key == pygame.K_DOWN:
                    index = (index + 1) % 3
                elif event.key == pygame.K_RETURN:
                    match index:
                        case 0 : gameSetupPage() 
                        case 1 : howToPlay()
                        case 2 : pygame.quit() ; exit()
        pygame.display.flip()


def gameSetupPage():
    font = pygame.font.Font("assets/Font/PixelifySans-Regular.ttf" ,30)
    screen = pygame.display.set_mode((400, 200))
    while True:
        screen.fill(BLACK)
        text = font.render("Setup game in terminal", True, WHITE)
        screen.blit(text, (200 // 10  , 200//2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        game()



def howToPlay():
    while True:
        background = pygame.image.load("assets/How.png")
        screen.blit(background, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                mainMenu()
                        



mainMenu()