""" Two objects move horizontally across the window at different speeds. """

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

robot = pygame.image.load("graphics/robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

class Robot:
    def __init__(self, x: int, y: int, velocity: int):
        self.image = pygame.image.load("graphics/robot.png")
        self.x = x
        self.y = y
        self.velocity = velocity

robot1 = Robot(0, 50, 1)
robot2 = Robot(0, 140, 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot1.image, (robot1.x, robot1.y))
    window.blit(robot2.image, (robot2.x, robot2.y))
    pygame.display.flip()
    
    robot1.x += robot1.velocity
    if robot1.velocity > 0 and robot1.x+robot_width >= 640:
        robot1.velocity = -robot1.velocity
    if robot1.velocity < 0 and robot1.x <= 0:
        robot1.velocity = -robot1.velocity

    robot2.x += robot2.velocity
    if robot2.velocity > 0 and robot2.x+robot_width >= 640:
        robot2.velocity = -robot2.velocity
    if robot2.velocity < 0 and robot2.x <= 0:
        robot2.velocity = -robot2.velocity

    clock.tick(60)