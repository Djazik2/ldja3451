import pygame
import random

W = 800
H = 600
BG = (0,0,0)
RED = (0,0,360)
blok = 0
start = 1

pygame.init()
pygame.display.set.caption("Текст")
pygame.display.set_mode((W,H))
screen = pygame.display.set_visible(False)
navy =  (5,0,50)
screen.fill(navy)
pygame.mouse.set_visible(False)
front = pygame.font.SysFont('Arial',38,True,False)
front2 = pygame.font.SysFont('Arial',18,False,True)
front_box = pygame.Surface((W - 20,front.get_height))


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
            pygame.quit()
        pygame.display.update()
