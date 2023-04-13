import pygame

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the window
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Simple Paint")

# Set up the pen
pen_color = BLACK
pen_size = 5
pen_position = (0, 0)

# Set up the color buttons
color_buttons = {
    RED: pygame.Rect(10, 10, 50, 50),
    GREEN: pygame.Rect(70, 10, 50, 50),
    BLUE: pygame.Rect(130, 10, 50, 50),
    WHITE: pygame.Rect(190, 10, 50, 50),
    BLACK: pygame.Rect(250, 10, 50, 50)
}

# Set up the eraser button
eraser_button = pygame.Rect(310, 10, 50, 50)

# Set up the game loop
done = False
clock = pygame.time.Clock()
screen.fill(WHITE)
# Main game loop
while not done:
    # Handle events
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse clicked on a color button
            for color, button in color_buttons.items():
                if button.collidepoint(event.pos):
                    pen_color = color
            # Check if the mouse clicked on the eraser button
            if eraser_button.collidepoint(event.pos):
                pen_color = WHITE
            # Get the position of the mouse
            pen_position = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEMOTION:
            # Draw a line from the previous position to the current position
            new_position = pygame.mouse.get_pos()
            pygame.draw.line(screen, pen_color, pen_position, new_position, pen_size)
            pen_position = new_position
        elif event.type == pygame.KEYDOWN:
            # Change the pen size when the up or down arrow keys are pressed
            if event.key == pygame.K_UP:
                pen_size += 1
            elif event.key == pygame.K_DOWN:
                pen_size -= 1
                if pen_size < 1:
                    pen_size = 1
    
    # Draw the color buttons

  
    for color, button in color_buttons.items():
        pygame.draw.rect(screen, color, button)
    
    # Draw a border around the selected color button
    pygame.draw.rect(screen, BLACK, color_buttons[pen_color], 3)
    
    
    # Draw the eraser button
    pygame.draw.rect(screen, BLACK, eraser_button)
    pygame.draw.rect(screen, WHITE, eraser_button.inflate(-6, -6))

    
    # Update the screen
    pygame.display.flip()
    clock.tick(60)

# Clean up
pygame.quit()
