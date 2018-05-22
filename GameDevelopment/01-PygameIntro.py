import pygame

# Initialize pygame
pygame.init()

red = 255,0,0

screen = pygame.display.set_mode((1000,700))

screen.fill(red)

while True:
    pygame.display.update()