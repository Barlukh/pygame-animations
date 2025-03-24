"""
Project Title: Pygame Animations
Filename: movement-mouse.py

Description:
    Animation sample where an object follows a mouse cursor.
    Requirements: Python and Pygame.
"""

__author__ = "Boris Gazur"
__date__ = "March 24, 2025"

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

robot = pygame.image.load("graphics/robot.png")

robot_x = 0
robot_y = 0
target_x = 0
target_y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            target_x = event.pos[0] - robot.get_width() / 2
            target_y = event.pos[1] - robot.get_height() / 2

        if event.type == pygame.QUIT:
            exit(0)

    if robot_x > target_x:
        robot_x -= 1
    if robot_x < target_x:
        robot_x += 1
    if robot_y > target_y:
        robot_y -= 1
    if robot_y < target_y:
        robot_y += 1

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)