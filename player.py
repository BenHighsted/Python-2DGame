import pygame

windowSizeX = 500
windowSizeY = 500

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > self.vel:
           self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < windowSizeX - self.width:
           self.x += self.vel
        if keys[pygame.K_UP] and self.y > self.vel:
           self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y < windowSizeY - self.height:
           self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
