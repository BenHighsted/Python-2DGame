# Created by Ben Highsted 2020

import pygame
from network import Network
from player import Player

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

def redrawWindow(window, player, player2):
    window.fill((255, 255, 255))
    player.draw(window)
    player2.draw(window)
    pygame.display.update()

def main():
    n = Network()

    p = n.getP()

    clock = pygame.time.Clock()
    
    running = True
    while running:
        clock.tick(60)
        p2 = n.send(p)
        
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
               pygame.quit()

        p.move()
        redrawWindow(window, p, p2)

main()
