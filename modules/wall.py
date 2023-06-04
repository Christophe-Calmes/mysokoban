import pygame
import os

class Wall:
    def __init__(self, x, y, width, height, color, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("assets", "wall.png")), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def draw(self):
        self.rect.topleft = (self.x, self.y)
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)
