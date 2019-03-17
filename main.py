import pygame

from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()


pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True

player = Player()

screen.blit(player.surf, player.rect)

pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
