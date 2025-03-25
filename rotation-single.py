"""
Project Title: Pygame Animations
Filename: rotation-single.py

Description:
    Animation sample where one object rotates in a circle.
    Requirements: Python and Pygame.
"""

import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

robot = pygame.image.load("graphics/robot.png")

angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x = 320 + math.cos(angle) * 100 - robot.get_width() / 2
    y = 240 + math.sin(angle) * 100 - robot.get_height() / 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    angle += 0.01
    clock.tick(60)