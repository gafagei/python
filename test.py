import pygame
import  random
pygame.init()
sc=pygame.display.set_mode((480,640))
bg=pygame.image.load("bg.jpg")
font = pygame.font.SysFont("",32)
score = 0
x = 0
y = 1
z = []
l = []
for i in range(5):
    l.append(random.randint(65,90))
    z.append(random.randint(0,750))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.blit(bg, (0, 0))
    for i in range(5):
        ra = l[i]
        s1 = chr(ra)
        text = font.render(s1, True, (255, 255, 255))
        sc.blit(text, (x + i * 90, y + z[i]))
        sco = font.render(str(score), True, (255, 255, 255))
        sc.blit(sco, (450,20))
        if event.type == pygame.KEYDOWN:
            if event.key == ra+32:
                z[i] = -y
                score += 1

        if y+z[i] > 640 or y+z[i] == 0:
            z[i] = -y
            l[i] = random.randint(65,90)

        y += 0.2

    pygame.display.update()