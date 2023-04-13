import pygame

# Initialize Pygame
pygame.init()

# Set up the canvas
canvas_width = 800
canvas_height = 600
canvas = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption("Paint Program")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Set up variables for shapes
shape_to_draw = ""
start_pos = None
end_pos = None
canvas.fill(white)
# Set up the game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                shape_to_draw = "square"
            elif event.key == pygame.K_r:
                shape_to_draw = "right_triangle"
            elif event.key == pygame.K_e:
                shape_to_draw = "equilateral_triangle"
            elif event.key == pygame.K_h:
                shape_to_draw = "rhombus"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            end_pos = pygame.mouse.get_pos()

    # Clear the canvas
   

    # Draw the selected shape if start and end positions are set
    if start_pos and end_pos:
        if shape_to_draw == "square":
            pygame.draw.rect(canvas, black, (start_pos[0], start_pos[1], end_pos[0]-start_pos[0], end_pos[0]-start_pos[0]), 2)
        elif shape_to_draw == "right_triangle":
            pygame.draw.polygon(canvas, black, [(start_pos[0], start_pos[1]), (end_pos[0], start_pos[1]), (start_pos[0], end_pos[1])], 2)
        elif shape_to_draw == "equilateral_triangle":
            height = (end_pos[0] - start_pos[0]) * 0.86602540378
            pygame.draw.polygon(canvas, black, [(start_pos[0], end_pos[1]), ((start_pos[0]+end_pos[0])/2, start_pos[1]), (end_pos[0], end_pos[1])], 2)
        elif shape_to_draw == "rhombus":
            pygame.draw.polygon(canvas, black, [(start_pos[0]+(end_pos[0]-start_pos[0])/2, start_pos[1]), (end_pos[0], start_pos[1]+(end_pos[1]-start_pos[1])/2), (start_pos[0]+(end_pos[0]-start_pos[0])/2, end_pos[1]), (start_pos[0], start_pos[1]+(end_pos[1]-start_pos[1])/2)], 2)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
