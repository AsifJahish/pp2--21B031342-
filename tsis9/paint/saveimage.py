import pygame
import os

import pygame
import os

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the background color
background_color = (255, 255, 255)

# Set the brush color
brush_color = (0, 0, 0)

# Set the brush size
brush_size = 20

# Set the drawing flag
drawing = False


# Start the main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit the program
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Start drawing
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            # Stop drawing
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing:
            # Draw a line
            pygame.draw.line(screen, brush_color, event.pos, event.rel, brush_size)

    # Fill the background
    screen.fill(background_color)

    # Update the screen
    pygame.display.update()

    # Save the screen as an image when the user presses the 's' key
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        # Get the path to the desktop
        desktop_path = os.path.join(os.path.join(os.environ['HOME']), 'Desktop')
        
        # Set the image path
        image_path = os.path.join("/home/asifjahish/Desktop/Classes 2023/", 'image.png')
        
        # Save the screen as an image
        pygame.image.save(screen, image_path)
        print('Image saved to', image_path)


    # Save the screen as an image when the user presses the 's' key
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        # Get the path to the desktop
        desktop_path = os.path.join(os.path.join(os.environ['HOME']), 'Desktop')
        
        # Set the image path
        image_path = os.path.join("/home/asifjahish/Desktop/Classes 2023/", 'e.png')
        
        # Save the screen as an image
        pygame.image.save(screen, image_path)
        print('Image saved to', image_path)
