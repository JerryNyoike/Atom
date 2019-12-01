import pygame
import random
from physics import SCREEN_HEIGHT, SCREEN_WIDTH, TOP_SPEED

from player import Player
from obstacle import Obstacle

atom = Player()

class GraphicsEngine:

    def __init__(self, surface):

        self.screenSurface = surface
        # sprite groups

        self.allSprites = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()

        self.allSprites.add(atom)
        self.getNewObstacles()

        # load everything

        self.loadResources()

    def loadResources(self):

        # sprites

        self.spriteWorld = pygame.image.load('resources/images/background.jpg'
                                             ).convert_alpha()

        self.spriteWorld = pygame.transform.scale(
            self.spriteWorld, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # fonts

        self.scoreFont = pygame.font.Font('resources/fonts/BADABB__.TTF',
                                          16)

    def renderGame(self):
        self.screenSurface.fill((0, 0, 0))
        self.drawBackground()
        self.updateObstacles()
        self.allSprites.draw(self.screenSurface)
        self.drawScore()
        self.drawTime()

    def addObstacle(self, obstacle):
        self.obstacles.add(obstacle)
        self.allSprites.add(obstacle)

    def drawBackground(self):
        for x in range(SCREEN_WIDTH // self.spriteWorld.get_width() + 1):
            for y in range(SCREEN_HEIGHT // self.spriteWorld.get_height() + 1):
                self.screenSurface.blit(
                    self.spriteWorld, (x * 100 - atom.CameraX, y * 100))

    def drawScore(self):
        energyText = self.scoreFont.render(
            'Energy: ' + str(atom.energy), True, (255, 255, 255))
        self.screenSurface.blit(energyText, (10 - atom.CameraX, 10))

    def drawTime(self):
        textSurface = self.scoreFont.render('TIME LEFT: '
                + ' SECS', True,
                (255, 255, 255))
        self.screenSurface.blit(textSurface, (10, 44))

    def getNewObstacles(self):
        for i in range(5):
            self.addObstacle(Obstacle())

    def updatePlayer(self, direction):
        atom.move(direction)

    def updateObstacles(self):
        for obstacle in self.obstacles:
            obstacle.move()




