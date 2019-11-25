import pygame
from pygame.locals import *


WIDTH, HEIGHT = 640, 480


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    pygame.display.set_caption('Atom')
    background_img = pygame.image.load("./resources/images/background.jpg")
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
	# gameover_img = pygame.image.load("./resources/images/gameover.png")
    font = pygame.font.Font('./resources/fonts/BADABB__.TTF', 24)
    clock = pygame.time.Clock()
    running = True
    time0, time_interval = 0, 0
    while running:
        screen.fill(0)
        for x in range(WIDTH // background_img.get_width() + 1):
            for y in range(HEIGHT // background_img.get_height() + 1):
                screen.blit(background_img, (x * 100, y * 100))
            time_passed = clock.tick() / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    pass
        
        time1 = pygame.time.get_ticks() / 1000
        if time1 - time0 > time_interval:
            pass

	# screen.blit(gameover_img, (0, 0))
    pygame.display.flip()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

if __name__ == "__main__":
    main()
