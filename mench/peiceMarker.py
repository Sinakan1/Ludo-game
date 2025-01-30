import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hover & Arrow Key Selection")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define objects (rectangles)
objects = [
    pygame.Rect(100, 100, 100, 100),
    pygame.Rect(300, 100, 100, 100),
    pygame.Rect(500, 100, 100, 100)
]

# Initial selected object index (-1 means nothing selected)
selected_index = 0  
mouse_selected = False  # Track if mouse moved over an object

# Function to draw the outline circle around the selected object
def draw_outline(surface, rect, color, radius):
    pygame.draw.circle(surface, color, rect.center, radius, 2)

# Main loop
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()  # Get current mouse position
    mouse_selected = False  # Reset flag

    # Detect hover and update selection
    for i, obj in enumerate(objects):
        if obj.collidepoint(mouse_pos):  
            selected_index = i
            mouse_selected = True
            break  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Handle arrow key input only if the mouse isn't selecting an object
            if event.key == pygame.K_LEFT:
                selected_index = (selected_index - 1) % len(objects)
                mouse_selected = False  # Prevent overriding selection
            elif event.key == pygame.K_RIGHT:
                selected_index = (selected_index + 1) % len(objects)
                mouse_selected = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the objects
    for obj in objects:
        pygame.draw.rect(screen, BLACK, obj)

    # Draw the outline around the selected object
    if selected_index != -1:
        draw_outline(screen, objects[selected_index], RED, 60)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
