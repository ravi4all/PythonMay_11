import pygame

# Initialize pygame
pygame.init()

red = 255,0,0
black = 0,0,0

screen = pygame.display.set_mode((1000,600))

screen.fill(red)

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()   # quit pygame
            quit()          # quit python

    # pygame.draw.rect(screen,black,[0,0,100,100])
    pygame.draw.circle(screen,black,[100,100],100)

    pygame.display.update()