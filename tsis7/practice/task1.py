

import pygame
import datetime

pygame.init()

width, height= 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("monkey clock")
clock = pygame.time.Clock()


clock_image= pygame.image.load("/home/asifjahish/vscode/pp2--21B031342-/tsis7/clock/clock.jpg")
clock_size= pygame.transform.scale(clock_image, (width, height))

minute = pygame.image.load('/home/asifjahish/vscode/pp2--21B031342-/tsis7/clock/min.png')
minute_size= pygame.transform.scale(minute,(120,120))
second = pygame.image.load('/home/asifjahish/vscode/pp2--21B031342-/tsis7/clock/min.png')
second_size= pygame.transform.scale(second,(120,120))

def blitRotate(image, pos, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    rect = rotated_image.get_rect(center=pos)
    screen.blit(rotated_image, rect)

    """
    The first line creates a list of four 2D 
    vectors using Pygame's Vector2 class,
      representing the corners of a rectangular box. 
      The values for these 
    vectors are taken from a tuple 
    containing four pairs of x-y coordinates.
    
    """

    
angle = 0
done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                 done = True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
    angle = datetime.datetime.now().second/60 * 360
    ang = datetime.datetime.now().minute/60 * 360

    pos = (screen.get_width()/2, screen.get_height()/2)
    
    
    screen.blit(clock_size,(0,0))
    blitRotate(minute_size, pos, -angle +145)
    blitRotate(second_size, pos, -ang +145)
    angle += 1

    
    
    pygame.draw.circle(screen, (232,34,51), pos, 20, 0)

    pygame.display.flip()
    
pygame.quit()
exit()
