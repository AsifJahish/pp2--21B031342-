import pygame

# Initialize Pygame
pygame.init()

# Set the window size and title
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Monkey pointing at two things")

# Define some colors
white = (255, 255, 255)
black = (0, 0, 0)
brown = (150, 75, 0)
pink = (255, 192, 203)

# Define a function to draw the monkey's body
def draw_body(x, y, size):
    pygame.draw.circle(screen, brown, (x, y), size)

# Define a function to draw the monkey's head
def draw_head(x, y, size):
    pygame.draw.circle(screen, brown, (x, y), size)
    pygame.draw.circle(screen, white, (x - size // 3, y - size // 3), size // 4)
    pygame.draw.circle(screen, black, (x - size // 3, y - size // 3), size // 8)
    pygame.draw.circle(screen, white, (x + size // 3, y - size // 3), size // 4)
    pygame.draw.circle(screen, black, (x + size // 3, y - size // 3), size // 8)
    pygame.draw.circle(screen, pink, (x, y), size // 3, size // 6)

# Define a function to draw the monkey's arm
def draw_arm(x, y, angle, size):
    pygame.draw.rect(screen, brown, (x, y, size, size // 3))
    pygame.draw.circle(screen, brown, (x + size // 2, y + size // 6), size // 4)
    pygame.draw.line(screen, black, (x + size, y + size // 6), (x + size + size // 3, y - size // 3), size // 8)
    pygame.draw.line(screen, black, (x + size, y + size // 6), (x + size + size // 3, y + size // 3), size // 8)
    rotated_surface = pygame.transform.rotate(screen, angle)
    screen.blit(rotated_surface, (x, y))

# Define a function to draw the monkey's two hands pointing at two things
def draw_hands(x1, y1, x2, y2, size):
    pygame.draw.line(screen, black, (x1, y1), (x1 - size // 2, y1 - size // 2), size // 8)
    pygame.draw.line(screen, black, (x2, y2), (x2 + size // 2, y2 - size // 2), size // 8)

# Draw the monkey with two hands up pointing at two things
draw_body(300, 300, 150)
draw_head(300, 200, 100)
draw_arm(150, 320, -45, 100)
draw_arm(350, 320, 45, 100)
draw_hands(100, 250, 500, 250, 50)

# Update the display
pygame.display.update()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
