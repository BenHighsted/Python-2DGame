# Created by Ben Highsted 2020
# Currently not sure what game I want to create, but it will be a 2D game

import pygame

# Initialises pygame
pygame.init()

# Creates game window
window = pygame.display.set_mode((500, 500))

# Title and Icon
pygame.display.set_caption("Ben's Python Game")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

# Set the background color
window.fill((255, 255, 255))

running = True
while running:

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False

    pygame.display.update()

pygame.quit()
