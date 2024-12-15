""" Object can be moved around with arrow keys. """

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

class Entity:
    def __init__(self, x: int, y: int, image: callable):
        self.x = x
        self.y = y
        self.image = image
    
robot = Entity(0, 0, pygame.image.load("graphics/robot.png"))

def draw_window():
    window.fill((0, 0, 0))
    window.blit(robot.image, (robot.x, robot.y))
    pygame.display.flip()
    clock.tick(60)

def check_events():
    to_up = False
    to_down = False
    to_right = False
    to_left = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    to_up = True
                if event.key == pygame.K_DOWN:
                    to_down = True
                if event.key == pygame.K_RIGHT:
                    to_right = True
                if event.key == pygame.K_LEFT:
                    to_left = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    to_up = False
                if event.key == pygame.K_DOWN:
                    to_down = False
                if event.key == pygame.K_RIGHT:
                    to_right = False
                if event.key == pygame.K_LEFT:
                    to_left = False

            if event.type == pygame.QUIT:
                exit()

        if to_up:
            if robot.y >= 2:
                robot.y -= 2
        if to_down:
            if robot.y <= 480 - 2 - robot.image.get_height():    
                robot.y += 2    
                
        if to_right:
            if robot.x <= 640 - 2 - robot.image.get_width():    
                robot.x += 2
                
        if to_left:
            if robot.x >= 2:    
                robot.x -= 2
        
        draw_window()

def main_loop():
    while True:
        check_events()

main_loop()