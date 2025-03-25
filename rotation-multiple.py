"""
Project Title: Pygame Animations
Filename: rotation-multiple.py

Description:
    Animation sample where multiple objects rotate in a circle.
    Requirements: Python and Pygame.
"""

import pygame
import math
 
pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

robot = pygame.image.load("graphics/robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

angle = 0
radius = 150
number = 10
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    window.fill((0, 0, 0))
    for i in range(number):
        x = 640 / 2 + math.cos(angle + 2 * math.pi * i / number) * radius - robot_width / 2
        y = 480 / 2 + math.sin(angle + 2 * math.pi * i / number) * radius - robot_height / 2
        window.blit(robot, (x, y))
    pygame.display.flip()
 
    angle += 0.01
    clock.tick(60)