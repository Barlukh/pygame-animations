""" Main execution file for the game. """
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

width = robot.get_width()
height = robot.get_height()

def draw_robots():
    x = 60
    y = 100
    for i in range(10):
        for i in range(10):
            window.blit(robot, (x + (i*39), y))
        x += 7
        y += 20

draw_robots()

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()