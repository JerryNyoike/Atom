import pygame
import time

from graphics import GraphicsEngine
from physics import SCREEN_HEIGHT, SCREEN_WIDTH, TOP_SPEED


class GameEngine():

    def __init__(self):
       
        self.screen = None
        # self.GAME_STATE = MENU_STARTGAME

        
        self.clock = pygame.time.Clock()
        self.gameTime = time.time()
        self.gameRunning = True
        self.currentLevel = 1

    def initializeGame(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            [SCREEN_WIDTH, SCREEN_HEIGHT]
        )
        pygame.display.set_caption('Atom')
        
        self.graphicsEngine = GraphicsEngine(self.screen)

        self.menuStartGame = None
        self.menuAbout = None
        self.menuScene = None
        self.menuGameOver = None
        self.menuGameFinish = None

        self.gameLoop()

    def gameLoop(self):
        while self.gameRunning:
            self.graphicsEngine.renderGame()
            pygame.display.update()

            self.clock.tick(60)

    
    def updatePlayer(self):
        player.doJump()

        player.onGround = False
        if not player.onGround and not player.jumping:
            player.yVel = 4

        if player.xVel > TOP_SPEED:
            player.xVel = TOP_SPEED
        elif player.xVel < -TOP_SPEED:
            player.xVel = -TOP_SPEED

        if player.rect.x <= 0:
            player.rect.x = 0
        elif player.rect.x >= SCREEN_WIDTH - player.rect.w:
            player.rect.x = SCREEN_WIDTH - player.rect.w

        # do collision check once we have obstacles and enemies here
        player.rect.x += player.xVel
        player.rect.y += player.yVel



                
