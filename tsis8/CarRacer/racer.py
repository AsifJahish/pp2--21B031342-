import pygame
import random

pygame.init()

width, height = 500, 700
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("car racer")


back = pygame.image.load('/home/asifjahish/vscode/pp2--21B031342-/tsis8/CarRacer/AnimatedStreet.png')
back_size = pygame.transform.scale(back, (500, 700))

class ComputerPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        redcar = pygame.image.load('/home/asifjahish/vscode/pp2--21B031342-/tsis8/CarRacer/Enemy.png')
        self.image = redcar
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect.width // 2, width - self.rect.width // 2), 0)

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top >height:
            self.rect.top = 0
            self.rect.center = (random.randint(self.rect.width // 2, width - self.rect.width // 2), 0)

    def draw(self):
        screen.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player = pygame.image.load('/home/asifjahish/vscode/pp2--21B031342-/tsis8/CarRacer/Player.png')
        self.image = player
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height - self.rect.height // 2 - 20)
        self.player_x = width
        self.player_y = 0
        self.player_speed = 3

    def draw(self):
        screen.blit(self.image, (self.player_x, self.player_y))

    def movement(self):
        pressed = pygame.key.get_pressed()
        if self.rect.left > 5 and pressed[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < width - 5 and pressed[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

player = Player()
computerPlayer = ComputerPlayer()

player_group = pygame.sprite.Group(player)
computer_group = pygame.sprite.Group(computerPlayer)
crash_sound = pygame.mixer.Sound('/home/asifjahish/vscode/pp2--21B031342-/tsis8/CarRacer/carcrush.mp3')
sound = pygame.mixer.Sound('/home/asifjahish/vscode/pp2--21B031342-/tsis8/CarRacer/race-car.mp3')


running = True
while running:
    screen.blit(back_size, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    sound.play()

    if pygame.sprite.spritecollideany(player, computer_group):
        crash_sound.play()

        running = False
    player.movement()
    computerPlayer.move()

    player_group.draw(screen)
    computer_group.draw(screen)
    pygame.display.update()
    CLOCK.tick(100)
    pygame.display.flip()

pygame.quit()
