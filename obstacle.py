import pygame
from random import randint, choice
from physics import PLAYER_START_X, SCREEN_WIDTH, SCREEN_HEIGHT


class Obstacle(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        image_choices = ['obstacle1.png', 'obstacle2.png', 'obstacle3.png', 'obstacle4.png', 'obstacle5.png']
        image_name = './resources/images/{}'.format(choice(image_choices))

        self.image = pygame.image.load(image_name).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = randint(PLAYER_START_X, SCREEN_WIDTH)
        self.rect.y = randint(0, SCREEN_HEIGHT)

        self.xVel = randint(2, 5)

    def draw(self, surface):
        y = self.rect.y + self.rect.h - self.image.get_rect().h
        surface.blit(self.image, self.rect)

    def move(self):
        yShift = randint(-3, 3)
        self.rect.move_ip(-self.xVel, yShift)
        if self.rect.right < 0:
            self.kill()

    def getRect(self):
        return self.rect

    def getSurf(self):
        return self.image





