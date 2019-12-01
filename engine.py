import pygame
import time

from obstacle import Obstacle
from graphics import GraphicsEngine
from physics import SCREEN_HEIGHT, SCREEN_WIDTH

from pygame.locals import (
    K_UP,
    K_w,
    K_DOWN,
    K_s,
    K_LEFT,
    K_d,
    K_RIGHT,
    K_a,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

E_ADDOBSTACLE = pygame.USEREVENT + 1
pygame.time.set_timer(E_ADDOBSTACLE, 250)

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

            for event in pygame.event.get():

                if event.type == QUIT:
                    self.gameRunning = False

                elif event.type == E_ADDOBSTACLE:
                    self.graphicsEngine.addObstacle(Obstacle())

                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.gameRunning = False
            
            pressed_keys = pygame.key.get_pressed()
            for key in pressed_keys:
                if pressed_keys[K_UP] or pressed_keys[K_w]:
                    self.graphicsEngine.updatePlayer()

            pygame.display.update()
            self.clock.tick(60)

                
