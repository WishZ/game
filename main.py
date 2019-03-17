import pygame
from pygame.locals import *

pygame.init()
running = True

screen = pygame.display.set_mode((800, 600))
surf = pygame.Surface((50, 50))
surf.fill((255, 255, 255))
rect = surf.get_rect()
screen.blit(surf,(400,300))
pygame.display.flip()
while running:
    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
