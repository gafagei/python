#棋盘
import pygame
import  random
pygame.init()
sc=pygame.display.set_mode((500,500))

bg=pygame.image.load("bg.jpg")
#s1="welcome"
#sc.blit(bg,(0,0))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    for i in range(25):
        pygame.draw.line(sc, (255, 255, 255), (0,(i + 1) * 20), (500,(i + 1) * 20), 1)
        pygame.draw.line(sc, (255, 255, 255), ((i+1)*20, 0), ((i+1)*20, 500), 1)
    pygame.display.update()