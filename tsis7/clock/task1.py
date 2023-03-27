import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

clock_image = pygame.image.load('/home/asifjahish/Desktop/pp2-2022-21BD-main/lab 7/clock/clock.jpg')
clock_size= pygame.transform.scale(clock_image,(400,400))

minute_image = pygame.image.load('/home/asifjahish/Desktop/pp2-2022-21BD-main/lab 7/clock/min.png')
minute_size= pygame.transform.scale(minute_image,(100,100))
second_image = pygame.image.load('/home/asifjahish/Desktop/pp2-2022-21BD-main/lab 7/clock/sec.png')
second_size= pygame.transform.scale(second_image,(100,100))

def blitRotate(image, pos, angle,wh,hh):


    box = [pygame.math.Vector2(p) for p in [(0, 0), (wh, 0), (wh, -hh), (0, -hh)]]

    box_rotate = [p.rotate(angle) for p in box]

    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    origin = (pos[0] + min_box[0], pos[1] - max_box[1])

    rotated_image = pygame.transform.rotate(image, angle)
    screen.blit(rotated_image, origin)


w, h = minute_size.get_size()
w2, h2 = minute_size.get_size()

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
    blitRotate(minute_size, pos, -angle +145,w,h)
    blitRotate(second_size, pos, -ang +145,w2,h2)
    angle += 1

    
    
    pygame.draw.circle(screen, (232,34,51), pos, 20, 0)

    pygame.display.flip()
    
pygame.quit()
exit()