import pygame

def move():
    pygame.init()

    clock= pygame.time.Clock()

    width, height= 500, 500

    screen= pygame.display.set_mode((width, height))

    pygame.display.set_caption("ball")
    ball_x= width//2
    ball_y= height//2

    ball_radius= 25
    color= (255,0,0)
    
    move_amount= 10

    running = True
    while running:
        clock.tick(10)



        keys= pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            ball_y -=move_amount
        if keys[pygame.K_DOWN]:
            ball_y+=move_amount
        if keys[pygame.K_RIGHT]:
            ball_x+=move_amount
        if keys[pygame.K_LEFT]:
            ball_x-=move_amount
        

        if ball_x<ball_radius:
            ball_x= ball_radius
        if ball_x>width- ball_radius:
            ball_x=width- ball_radius
        if ball_y<ball_radius:
            ball_y= ball_radius
        if ball_y> height-ball_radius:
            ball_y= height-ball_radius
        

        screen.fill((255,255,255))

        pygame.draw.circle(screen, color, (ball_x, ball_y), ball_radius, width=3)

        pygame.display.flip()

    pygame.quit()

move()