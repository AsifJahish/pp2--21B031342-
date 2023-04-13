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

# Set up the rectangle drawing state
drawing_rectangle = False
rectangle_start_position = None
rectangle_end_position = None
rectangle_color = BLACK

# Set up the circle drawing state
drawing_circle = False
circle_start_position = None
circle_end_position = None
circle_color = BLACK

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
            # Check if the mouse clicked on the top rectangle
            if event.pos[1] < 60:
                # Check if the mouse clicked on the color chooser rectangle
                if rectangle_start_position is not None and pygame.Rect(rectangle_start_position, (50, 50)).collidepoint(event.pos):
                    rectangle_color = pen_color
                else:
                    drawing_rectangle = True
                    rectangle_start_position = event.pos
            # Check if the mouse clicked on the top circle
            elif event.pos[1] < 120:
                # Check if the mouse clicked on the color chooser rectangle
                if circle_start_position is not None and pygame.Rect(circle_start_position, (50, 50)).collidepoint(event.pos):
                    circle_color = pen_color
                else:
                    drawing_circle = True
                    circle_start_position = event.pos
        elif event.type == pygame.MOUSEMOTION:
            if drawing_rectangle:
                # Erase the old rectangle
                if rectangle_end_position is not None:
                    pygame.draw.rect(screen, WHITE, (rectangle_start_position, rectangle_end_position))
                # Draw the new rectangle
                rectangle_end_position = event.pos
                pygame.draw.rect(screen, pen_color, (rectangle_start_position, rectangle_end_position), pen_size)
                # Draw the color chooser rectangle
                pygame.draw.rect(screen, rectangle_color, (rectangle_start_position, (50, 50)))
        elif drawing_circle:
                # Erase the old circle
            if circle_end_position is not None:
                pygame.draw.circle(screen, WHITE, circle_start_position, int(pygame.math.distance.circle(circle_start_position, circle_end_position)))
              # Draw the new circle
                circle_end_position = event.pos
                pygame.draw.circle(screen, pen_color, circle_start_position, int(pygame.math.distance.circle(circle_start_position, circle_end_position)), pen_size)
                    # Draw the color chooser rectangle
                pygame.draw.rect(screen, circle_color, (circle_start_position[0] - 25, circle_start_position[1] - 25, 50, 50))

        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing_rectangle:
                drawing_rectangle = False
            # Draw the final rectangle
                pygame.draw.rect(screen, pen_color, (rectangle_start_position, rectangle_end_position), pen_size, width=4)
            # Draw the color chooser rectangle
                pygame.draw.rect(screen, rectangle_color, (rectangle_start_position, (50, 50)))
            # Reset the rectangle drawing state
                rectangle_start_position = None
                rectangle_end_position = None
        elif drawing_circle:
            drawing_circle = False
            # Draw the final circle
            pygame.draw.circle(screen, pen_color, circle_start_position, int(pygame.math.distance.circle(circle_start_position, circle_end_position)), pen_size)
            # Draw the color chooser rectangle
            pygame.draw.rect(screen, circle_color, (circle_start_position[0] - 25, circle_start_position[1] - 25, 50, 50))
            # Reset the circle drawing state
            circle_start_position = None
            circle_end_position = None

# Draw the color buttons
for color, button in color_buttons.items():
    pygame.draw.rect(screen, color, button)
# Draw the eraser button
pygame.draw.rect(screen, WHITE, eraser_button)
pygame.draw.rect(screen, BLACK, eraser_button, 1)
# Draw the top rectangle
pygame.draw.rect(screen, WHITE, (0, 0, size[0], 60))
pygame.draw.rect(screen, BLACK, (0, 0, size[0], 60), 1)
# Draw the color chooser rectangle on the top rectangle
if rectangle_start_position is not None:
    pygame.draw.rect(screen, rectangle_color, (rectangle_start_position, (50, 50)))
# Draw the circle chooser rectangle on the top rectangle
if circle_start_position is not None:
    pygame.draw.rect(screen, circle_color, (circle_start_position[0] - 25, circle_start_position[1] - 25, 50, 50))
# Update the screen
pygame.display.flip()
# Limit the frame rate
clock.tick(60)
