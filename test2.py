#满天星
import pygame
import random

sc=pygame.display.set_mode((500,600))
star = pygame.image.load("star.png")
for i in range(15):
    sc.blit(star,(random.uniform(0,500),random.uniform(0,600)))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    pygame.display.update()