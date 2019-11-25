import pygame
import physics

from physics import PLAYER_START_X, SCREEN_HEIGHT


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("./resources/images/comet.gif")
        
        self.rotated_atom = pygame.image.load("./resources/images/comet.gif")
        self.rect = self.rotated_atom.get_rect()
        self.rect.x = PLAYER_START_X
        self.rect.y = SCREEN_HEIGHT - 400

        self.xVel = 0
        self.yVel = 0

        self.energy = 1000

        # jumping

        self.jumping = False
        self.onGround = False
        self.origJumpVel = 3.5
        self.jumpVel = self.origJumpVel
        self.gravity = 0.1

        # score
        self.collectedResources = 0

    def draw(self, surface):
        y = self.rect.y + self.rect.h - self.image.get_rect().h
        surface.blit(self.image, (self.rect.x, y))

    def reset(self):
        self.rect.x = PLAYER_START_X
        self.rect.y = SCREEN_HEIGHT - 400

        self.xVel = 0
        self.yVel = 0
        self.direction = DIR_RIGHT

        self.collectedResources = 0

    def doJump(self):
        if self.jumping and not self.onGround:
            self.yVel = -self.jumpVel
            self.jumpVel -= self.gravity

        if self.onGround:
            self.jumping = False
            self.jumpVel = self.origJumpVel
            self.yVel = 0
            self.onGround = True



			