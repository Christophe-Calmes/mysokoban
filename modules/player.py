import pygame
from pygame.locals import *
import os

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("assets", "personnage.png")), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.lastMove = (self.x, self.y)

    def draw(self):
        self.rect.topleft = (self.x, self.y)
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)

    def move(self, event):
        if event.type == KEYDOWN:
            self.lastMove = (self.x, self.y)
            if event.key == K_LEFT:
                self.x -= 10
            if event.key == K_RIGHT:
                self.x += 10
            if event.key == K_UP:
                self.y -= 10
            if event.key == K_DOWN:
                self.y += 10

    def moveBack(self):
        self.x = self.lastMove[0]
        self.y = self.lastMove[1]
