# Created by Ben Highsted 2020
# Currently not sure what game I want to create, but it will be a 2D game

import pygame
from network import Network

# Initialises pygame
pygame.init()

# Creates game window
windowSizeX = 500
windowSizeY = 500

window = pygame.display.set_mode((windowSizeX, windowSizeY))

# Title and Icon
pygame.display.set_caption("Ben's Python Game")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

# Set the background color
window.fill((255, 255, 255))


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

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def redrawWindow(window, player, player2):
    window.fill((255, 255, 255))
    player.draw(window)
    player2.draw(window)
    pygame.display.update()

def main():
    n = Network()
    startPos = read_pos(n.getPos())
    
    p = Player(startPos[0], startPos[1], 40, 60, (255, 0, 0))
    p2 = Player(0, 0, 40, 60, (0, 0, 255))
    clock = pygame.time.Clock()
    
    running = True
    while running:
        clock.tick(60)

        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()
        
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
               pygame.quit()

        p.move()
        redrawWindow(window, p, p2)

main()
