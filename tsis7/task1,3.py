

import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the window
window_size = (400, 400)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Clock")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Set up the clock's variables
clock_radius = 150
clock_center = (200, 200)

# Start the main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear the screen
    window.fill(WHITE)

    # Draw the clock face
    pygame.draw.circle(window, GRAY, clock_center, clock_radius)
    pygame.draw.circle(window, BLACK, clock_center, clock_radius, 1)

    # Draw the hour markers
    for i in range(12):
        angle = i * (math.pi/6)
        x = int(math.sin(angle) * (clock_radius - 20)) + clock_center[0]
        y = int(-math.cos(angle) * (clock_radius - 20)) + clock_center[1]
        pygame.draw.circle(window, BLACK, (x, y), 5)

    # Draw the hands
    current_time = pygame.time.get_ticks() / 1000
    hours = current_time / 3600 % 12
    minutes = current_time / 60 % 60
    seconds = current_time % 60

    hour_angle = (hours * math.pi/6) + (minutes * math.pi/360)
    minute_angle = (minutes * math.pi/30)
    second_angle = (seconds * math.pi/30)

    hour_hand_length = 50
    minute_hand_length = 75
    second_hand_length = 100

    hour_x = int(math.sin(hour_angle) * hour_hand_length) + clock_center[0]
    hour_y = int(-math.cos(hour_angle) * hour_hand_length) + clock_center[1]
    minute_x = int(math.sin(minute_angle) * minute_hand_length) + clock_center[0]
    minute_y = int(-math.cos(minute_angle) * minute_hand_length) + clock_center[1]
    second_x = int(math.sin(second_angle) * second_hand_length) + clock_center[0]
    second_y = int(-math.cos(second_angle) * second_hand_length) + clock_center[1]

    pygame.draw.line(window, BLACK, clock_center, (hour_x, hour_y), 6)
    pygame.draw.line(window, BLACK, clock_center, (minute_x, minute_y), 4)
    pygame.draw.line(window, BLACK, clock_center, (second_x, second_y), 2)

    # Update the screen
    pygame.display.update()
