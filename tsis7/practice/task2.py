import pygame
import os

pygame.init()

pygame.mixer.init()

theMusic = [    "/home/asifjahish/vscode/pp2--21B031342-/tsis7/music/fire.mp3",    "/home/asifjahish/vscode/pp2--21B031342-/tsis7/music/rain .mp3",    "/home/asifjahish/vscode/pp2--21B031342-/tsis7/music/Raindrops.mp3"]

current_music = 0

music = pygame.mixer.music.load(theMusic[current_music])
pygame.mixer.music.play()

# Define keyboard controls
play = pygame.K_SPACE
stop = pygame.K_s
next_track = pygame.K_RIGHT
previous_track = pygame.K_LEFT

# Load a picture for the window
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My music")
mickey = pygame.image.load(os.path.join('/home/asifjahish/vscode/pp2--21B031342-/tsis7/image/mickeyclock.jpeg'))
mickey_size = pygame.transform.scale(mickey, (width, height))

# Main game loop
while True:
    # Check for keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    if keys[play]:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    if keys[stop]:
        pygame.mixer.music.stop()
    if keys[next_track]:
        current_music = (current_music + 1) % len(theMusic)
        music = pygame.mixer.music.load(theMusic[current_music])
        pygame.mixer.music.play()
    if keys[previous_track]:
        current_music = (current_music - 1) % len(theMusic)
        music = pygame.mixer.music.load(theMusic[current_music])
        pygame.mixer.music.play()

    # Draw the image to the screen
    screen.blit(mickey_size, (0, 0))
    pygame.display.update()
