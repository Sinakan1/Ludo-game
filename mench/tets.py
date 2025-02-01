import pygame

pygame.init()

# Screen setup
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text in Center of Circle")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


# Circle setup
circle_x, circle_y = WIDTH // 2, HEIGHT // 2
circle_radius = 150

# Font setup
font = pygame.font.Font(None, circle_radius // 3)  # Default font

# Render text
text = "Hello"
text_surface = font.render(text, True, BLACK)
text_rect = text_surface.get_rect(center=(circle_x, circle_y))

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Draw circle
    pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_radius)

    # Draw text
    screen.blit(text_surface, text_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
