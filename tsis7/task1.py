import pygame
import time
import os

pygame.init()

# Set the size of the window
window_size = (500, 500)
window = pygame.display.set_mode(window_size)

# Load the image of Mickey Mouse

mickey = pygame.image.load(os.path.join('/home/asifjahish/vscode/pp2--21B031342-/tsis7/image/mickeyclock.jpeg'))
mickey_size= pygame.transform.scale(mickey, (200, 200))

# Set the position of the center of the clock
clock_center = (200, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Get the current time in seconds and minutes
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    # Rotate the images of Mickey's hands
    seconds_hand = pygame.transform.rotate(mickey_size, seconds * 6)
    minutes_hand = pygame.transform.rotate(mickey_size, minutes * 6)

    # Draw the clock hands onto the screen
    window.blit(seconds_hand, (clock_center[0] - seconds_hand.get_rect().width/2, 
                               clock_center[1] - seconds_hand.get_rect().height/2))
    window.blit(minutes_hand, (clock_center[0] - minutes_hand.get_rect().width/2, 
                               clock_center[1] - minutes_hand.get_rect().height/2))

    pygame.display.update()
