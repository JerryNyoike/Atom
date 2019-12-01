import pygame
import physics as ph

from physics import PLAYER_START_X, SCREEN_HEIGHT, SCREEN_WIDTH, DIR_LEFT, DIR_RIGHT


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.forward_atom = pygame.image.load("./resources/images/comet.gif")
        self.rotated_atom = pygame.image.load("./resources/images/comet.gif")

        self.CameraX = 1
        # self.CameraY = 0 don't need this right now

        self.image = self.forward_atom

        self.rect = self.image.get_rect()
        self.rect.x = PLAYER_START_X
        self.rect.y = SCREEN_HEIGHT - 400

        self.xVel = 0
        self.yVel = 0

        # initial direction
        self.direction = DIR_RIGHT

        # jumping

        self.jumping = False
        self.onGround = False
        self.origJumpVel = 3.5
        self.jumpVel = self.origJumpVel
        self.gravity = 0.1

        # score
        self.energy = 1000

    def draw(self, surface):
        y = self.rect.y + self.rect.h - self.image.get_rect().h
        surface.blit(self.image, (self.rect.x -self.CameraX, y))

    def reset(self):
        self.rect.x = PLAYER_START_X
        self.rect.y = SCREEN_HEIGHT - 400

        self.xVel = 0
        self.yVel = 0
        self.direction = DIR_RIGHT

        self.energy = 1000

    def move(self, dir):
        """ move will also implement turning
        """

        if self.direction == dir:
            # no turning let's go
            if self.direction == DIR_LEFT:
                self.rect.x -= self.xVel
                # if self.rect.x <= 0:
                #     self.rect.x = 0

            elif self.direction == DIR_RIGHT:
                self.rect.x += self.xVel
                # if self.rect.x >= SCREEN_WIDTH - player.rect.w:
                #     self.rect.y = SCREEN_WIDTH - player.rect.w

        else:
            # we turn
            x = self.rect.x
            y = self.rect.y
            self.direction = dir
            if self.direction == DIR_RIGHT:
                # turn forward
                self.image = self.forward_atom
                self.rect = self.image.get_rect()
                self.rect.x, self.rect.y = x, y

            elif self.direction == DIR_LEFT:
                # turn backward
                self.image = self.rotated_atom
                self.rect = self.image.get_rect()
                self.rect.x, self.rect.y = x, y

        # update camera
        if self.rect.x > SCREEN_WIDTH / 4 * 3:
            self.CameraX += 10

    def doJump(self):
        if self.jumping and not self.onGround:
            self.yVel = -self.jumpVel
            self.jumpVel -= self.gravity

        if self.onGround:
            self.jumping = False
            self.jumpVel = self.origJumpVel
            self.yVel = 0
            self.onGround = True
