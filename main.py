# Created by Ben Highsted 2020
# Currently not sure what game I want to create, but it will be a 2D game

import pygame

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

# Set up for the basic player size/speed/location
x = 50
y = 50
width = 40
height = 60
vel = 1

# Main Loop
running = True
while running:

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
       x -= vel
    if keys[pygame.K_RIGHT] and x < windowSizeX - width:
       x += vel
    if keys[pygame.K_UP] and y > vel:
       y -= vel
    if keys[pygame.K_DOWN] and y < windowSizeY - height:
       y += vel
       
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))

    pygame.display.update()

pygame.quit()
