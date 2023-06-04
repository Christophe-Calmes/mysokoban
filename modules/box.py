import pygame
from pygame.locals import *
import os

class Box(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("assets", "box.png")), (self.width, self.height))
        self.rect = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        self.lastMove = (self.x, self.y)

    def draw(self):
        self.rect = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
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

    def moveIfCollideWithOtherBoxList(self, boxes, event, player):
        boxesWithoutHimself = [box for box in boxes if box != self]
        if self.rect.collidelist(boxesWithoutHimself) != -1:
            player.moveBack()
            self.moveBack()
            # for index in self.rect.collidelistall(boxesWithoutHimself):
            #     boxesWithoutHimself[index].move(event)
    
    def moveBack(self):
        self.x = self.lastMove[0]
        self.y = self.lastMove[1]