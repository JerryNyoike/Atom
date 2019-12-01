import pygame
from random import randint, choice
from physics import PLAYER_START_X, SCREEN_WIDTH, SCREEN_HEIGHT, FORWARD_FLY_ACC

IMAGE_CHOICES = [
            'obstacle1.png', 
            'obstacle2.png', 
            'obstacle3.png', 
            'obstacle4.png', 
            'obstacle5.png', 
            'obstacle6.png', 
            'obstacle7.png', 
            'obstacle8.png'
            ]

class Obstacle(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        image_name = './resources/images/{}'.format(choice(IMAGE_CHOICES))

        self.image = pygame.image.load(image_name).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = randint((SCREEN_HEIGHT * 0.75), SCREEN_WIDTH)
        self.rect.y = randint(0, SCREEN_HEIGHT)

        self.xVel = randint(2, 8)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self):
        self.rect.move_ip(-self.xVel, 0)
        if self.rect.right < 0:
            self.kill()





