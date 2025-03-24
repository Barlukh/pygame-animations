"""
Project Title: Pygame Animations
Filename: bounce-perimeter.py

Description:
    Animation sample where an object bounces around the window.
    Requirements: Python and Pygame.
"""

__author__ = "Boris Gazur"
__date__ = "March 24, 2025"

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

ball = pygame.image.load("graphics/ball.png")

x = 0
y = 0
x_velocity = 1
y_velocity = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()
    
    x += x_velocity
    y += y_velocity
    if x_velocity > 0 and x+ball.get_width() >= 640:
        x_velocity = -x_velocity
    if y_velocity > 0 and y+ball.get_height() >= 480:
        y_velocity = -y_velocity
    if x_velocity < 0 and x <= 0:
        x_velocity = -x_velocity
    if y_velocity < 0 and y <= 0:
        y_velocity = -y_velocity

    clock.tick(60)