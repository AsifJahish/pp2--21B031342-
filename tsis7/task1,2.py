import pygame
import time
import math

# initialize Pygame
pygame.init()

# set up the window
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mickey Clock")

# load Mickey Mouse image
mickey = pygame.image.load("/home/asifjahish/vscode/pp2--21B031342-/tsis7/image/mickeyclock.jpeg")
mickey_size= pygame.transform.scale(mickey, (50, 50))
# set the origin of the clock
clock_center_x = window_width // 2
clock_center_y = window_height // 2


clock_radius = 150
clock_center = (200, 200)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)


# define the length of Mickey's hands
minute_hand_length = 100
second_hand_length = 70

# define the colors of the hands
minute_hand_color = (0, 0, 255)
second_hand_color = (255, 0, 0)

# define the angle of the hands
minute_hand_angle = 0
second_hand_angle = 0

# define the function to calculate the angle of the hands
def get_hand_angle(hand_length, current_time, max_time):
    angle = (360 / max_time) * current_time
    angle_rad = math.radians(angle)
    hand_x = hand_length * math.cos(angle_rad)
    hand_y = hand_length * math.sin(angle_rad)
    return angle, hand_x, hand_y

# set up the clock
clock = pygame.time.Clock()

# start the game loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # get the current time
    current_time = time.localtime()
    current_minute = current_time.tm_min
    current_second = current_time.tm_sec

    # calculate the angle and position of the minute hand
    minute_hand_angle, minute_hand_x, minute_hand_y = get_hand_angle(minute_hand_length, current_minute, 60)
    minute_hand_image = pygame.transform.rotate(mickey_size, minute_hand_angle)
    minute_hand_rect = minute_hand_image.get_rect()
    minute_hand_rect.center = (clock_center_x + minute_hand_x, clock_center_y - minute_hand_y)

    # calculate the angle and position of the second hand
    second_hand_angle, second_hand_x, second_hand_y = get_hand_angle(second_hand_length, current_second, 60)
    second_hand_image = pygame.transform.rotate(mickey_size, second_hand_angle)
    second_hand_rect = second_hand_image.get_rect()
    second_hand_rect.center = (clock_center_x + second_hand_x, clock_center_y - second_hand_y)

    # draw the clock hands on the screen
    window.fill((255, 255, 255))
    pygame.draw.circle(window, GRAY, clock_center, clock_radius)
    pygame.draw.circle(window, BLACK, clock_center, clock_radius, 1)
    for i in range(12):
        angle = i * (math.pi/6)
        x = int(math.sin(angle) * (clock_radius - 20)) + clock_center[0]
        y = int(-math.cos(angle) * (clock_radius - 20)) + clock_center[1]
        pygame.draw.circle(window, BLACK, (x, y), 5)

    window.blit(minute_hand_image, minute_hand_rect)
    window.blit(second_hand_image, second_hand_rect)
    pygame.display.update()

    # wait for one second
    clock.tick(60)
