import pygame
import random
import os
from pygame.locals import *
from modules.player import Player
from modules.box import Box
from modules.wall import Wall
from modules.utils import Utils
from modules.hole import Hole

pygame.init()
WIDTH = 1024
HEIGHT = 720
pygame.display.set_caption('Sokoban')

MAPS = [
    ['.', '.', '.', '.', 'W', 'W', 'W', 'W', 'W',
        '.', '.', '.', '.', '.', '.', '.', '.', '.',],
    ['.', '.', '.', '.', 'W', '.', '.', '.', 'W',
        '.', '.', '.', '.', '.', '.', '.', '.', '.',],
    ['.', '.', 'W', 'W', 'W', '.', 'P', '.', 'W',
        'W', '.', '.', '.', '.', '.', '.', '.', '.',],
    ['.', '.', 'W', '.', '.', '.', '.', 'B', '.',
        'W', '.', '.', '.', '.', '.', '.', '.', '.',],
    ['W', 'W', 'W', '.', 'W', '.', 'W', 'W', '.',
        'W', '.', '.', 'W', 'W', 'W', 'W', 'W', 'W',],
    ['W', '.', '.', '.', 'W', '.', 'W', 'W', '.',
        'W', 'W', 'W', 'W', '.', '.', '.', 'H', 'W',],
    ['W', '.', '.', '.', '.', 'B', '.', '.', '.',
        '.', '.', '.', '.', '.', '.', '.', 'H', 'W',],
    ['W', 'W', 'W', 'W', '.', '.', '.', '.', '.',
        'B', '.', '.', '.', '.', '.', '.', 'H', 'W',],
    ['.', '.', '.', 'W', '.', 'B', 'W', 'W', 'W',
        '.', '.', 'W', 'W', '.', '.', '.', 'H', 'W',],
    ['.', '.', '.', 'W', '.', '.', '.', '.', '.',
        '.', '.', 'W', 'W', 'W', 'W', 'W', 'W', 'W',],
    ['.', '.', '.', 'W', 'W', 'W', 'W', 'W', 'W',
        '.', '.', 'W', '.', '.', '.', '.', '.', '.',],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.',
        'W', 'W', '.', '.', '.', '.', '.', '.', '.',],
]

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def generateMaps(MAPS):
    walls, boxes, holes = [], [], []
    for row_index, row in enumerate(MAPS):
        for col_index, char in enumerate(row):
            x = col_index * 50
            y = row_index * 50
            if char == 'W':
                wall = Wall(x, y, 50, 50, 'black', screen)
                walls.append(wall)
            elif char == 'H':
                hole = Hole(x, y, 50, screen)
                holes.append(hole)
            elif char == 'B':
                box = Box(x, y, 50, 50, (0, random.randrange(0, 255), 255), screen)
                boxes.append(box)
            elif char == 'P':
                player = Player(x, y, 50, 50, (255, 0, 0), screen)
    return len(MAPS), len(MAPS[0]), walls, boxes, holes, player

def editorLoop():
    items = ['box.png', 'wall.png', 'hole.png']
    image = items[0]
    items_positions = []

    while True:
        screen.fill((120, 120, 120))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                elif event.key == K_e:
                    return
                elif event.key == K_1:
                    image = items[0]
                elif event.key == K_2:
                    image = items[1]
                elif event.key == K_3:
                    image = items[2]
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if image != 'hole.png':
                    items_positions.append((image, mouse_pos[0] - mouse_pos[0] % 50, mouse_pos[1] - mouse_pos[1] % 50))
                else:
                    items_positions.append((image, mouse_pos[0] - mouse_pos[0] % 50 + 25, mouse_pos[1] - mouse_pos[1] % 50 + 25))

        for item in items_positions:
            item_image = pygame.transform.scale(pygame.image.load(os.path.join("assets", item[0])), (50, 50))
            screen.blit(item_image, (item[1], item[2]))

        mouse_pos = pygame.mouse.get_pos()
        if image != 'hole.png':
            grid_rect = pygame.Rect(mouse_pos[0] - mouse_pos[0] % 50, mouse_pos[1] - mouse_pos[1] % 50, 50, 50)
            pygame.draw.rect(screen, 'black', grid_rect, 1)
            choosen_grid_image = pygame.transform.scale(pygame.image.load(os.path.join("assets", image)), (50, 50))
            screen.blit(choosen_grid_image, (mouse_pos[0] - mouse_pos[0] % 50, mouse_pos[1] - mouse_pos[1] % 50))
        else:
            grid_center = (mouse_pos[0] - mouse_pos[0] % 50 + 25, mouse_pos[1] - mouse_pos[1] % 50 + 25)
            pygame.draw.circle(screen, 'black', grid_center, 25)

        pygame.display.flip()

def gameLoop():
    nbRow, nbCol, walls, boxes, holes, player = generateMaps(MAPS)

    while True:
        screen.fill((120, 120, 120))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            else:
                player.move(event)
                Utils.detectCollideBoxes(boxes, player, event, walls)

        for hole in holes:
            hole.draw()
            isInHole, indexBox = hole.boxIsOnHole(boxes)
            if isInHole:
                boxInHole.append(indexBox)
                boxes.pop(indexBox - 1)
                hole.validateHole()

        for wall in walls:
            wall.draw()

        for box in boxes:
            box.moveIfCollideWithOtherBoxList(boxes, event, player)
            if box.rect.collidelist(walls) != -1:
                player.moveBack()
                box.moveBack()
            box.draw()

        player.draw()
        pygame.display.flip()

while True:
    screen.fill((120, 120, 120))
    font = pygame.font.SysFont('arial', 30)
    text = font.render('Appuyez sur P pour lancer le Sokoban', True, (255, 255, 255))
    text1 = font.render('Appuyez sur d pour lancer l\'designeur de niveau', True, (255, 255, 255))
    text2 = font.render('Appuyez sur Echap pour quitter', True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
    screen.blit(text1, (WIDTH // 2 - 150, HEIGHT // 2))
    screen.blit(text2, (WIDTH // 2 - 150, HEIGHT // 2 + 50))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
            elif event.key == K_d:
                editorLoop()
            elif event.key == K_p:
                gameLoop()

    pygame.display.flip()
