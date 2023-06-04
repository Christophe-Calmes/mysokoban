import pygame

class Hole:
    def __init__(self, x, y, radius, screen):
        self.x = x
        self.y = y
        self.radius = radius
        self.screen = screen
        self.color = (0, 0, 0)
        self.width = 25
        self.validated = False
        self.totalBoxes = 0  # Variable pour garder une trace du nombre total de boîtes

    def draw(self):
        if self.validated:
            self.color = (0, 255, 0)
        pygame.draw.circle(self.screen, self.color, (self.x + self.width, self.y + self.width), 25, self.width)

    def boxIsOnHole(self, boxes):
        if self.validated:
            return False, -1
        for i, box in enumerate(boxes, start=1):
            if box.x == self.x and box.y == self.y:
                return True, i
        return False, -1
    
    def validateHole(self):
        self.color = (0, 255, 0)
        self.validated = True
        self.totalBoxes += 1  # Incrémente le nombre total de boîtes validées
        if self.totalBoxes == len(boxes):  # Vérifie si toutes les boîtes ont été validées
            print('You win')
            pygame.quit()  # Arrête le jeu en fermant la fenêtre
