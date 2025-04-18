"""
Project Title: Pygame Animations
Filename: around-perimeter.py

Description:
    Animation sample where an object moves around the perimeter of the window.
    Requirements: Python and Pygame.
"""

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

robot = pygame.image.load("graphics/robot.png")

x = 0
y = 0
velocity = 1
direction = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    if direction == 1:
        x += velocity
        if x + robot.get_width() == 640:
            direction = 2
    elif direction == 2:
        y += velocity
        if y + robot.get_height() == 480:
            direction = 3
    elif direction == 3:
        x -= velocity
        if x == 0:
            direction = 4
    elif direction == 4:
        y -= velocity
        if y == 0:
            direction = 1

    clock.tick(60)