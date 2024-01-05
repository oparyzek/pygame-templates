import pygame
import sys
import random
from pygame.locals import *
from pygame import mixer

#there u write a name of your background image file(must be in folder assets)
background = pygame.image.load("assets/background.jpg")


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("comicsans", 30)
    #there u set a pixels for your resolution, this is for Ultra HD(4K)
    window = pygame.display.set_mode((3840, 2160))  

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        window.blit(background, (0, 0))
        pygame.display.update()
        #there u set a FPS, this is 60FPS
        clock.tick(60)