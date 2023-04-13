import pygame

def move_ball_game():
    # initialize Pygame
    pygame.init()

    # set up the window
    clock = pygame.time.Clock()
    screen_width = 640
    screen_height = 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Move the Ball")

    # set up the ball
    ball_radius = 50
    ball_color = (255, 0, 0)
    ball_x = screen_width // 2
    ball_y = screen_height // 2

    move_amount= 20

    # main game loop
    running = True
    while running:
        # handle events
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # get pressed keys
        keys = pygame.key.get_pressed()

        # move the ball
        if keys[pygame.K_UP]:
            ball_y -= move_amount
        if keys[pygame.K_DOWN]:
            ball_y += move_amount
        if keys[pygame.K_LEFT]:
            ball_x -= move_amount
        if keys[pygame.K_RIGHT]:
            ball_x += move_amount

        # check if the ball is out of bounds
        if ball_x < ball_radius:
            ball_x = ball_radius
        if ball_x > screen_width - ball_radius:
            ball_x = screen_width - ball_radius
        if ball_y < ball_radius:
            ball_y = ball_radius
        if ball_y > screen_height - ball_radius:
            ball_y = screen_height - ball_radius

        # draw the screen
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
        pygame.display.flip()

    # quit Pygame
    pygame.quit()


move_ball_game()


"""
In Pygame, the Clock object is used 
to control the frame rate of a game or
 application. It allows you to set a maximum 
 frame rate, and then measures the time elapsed
   between each frame.




   In this code, event is a variable 
   that is used to iterate 
   through a list of all the
     events that have occurred 
     since the last time the event queue
       was checked. The events are obtained
         using the pygame.event.get() method, 
         which returns a list of pygame.
         event.Event objects.

"""