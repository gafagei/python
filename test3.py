#满天雪花
import pygame
import  random
sc=pygame.display.set_mode((1000,750))
snow=pygame.image.load("snow.png")
bg=pygame.image.load("bg.jpg")
x = 0
y = -128

#z = [random.uniform(0,500),random.uniform(0,500),random.uniform(0,500),random.uniform(0,500),random.uniform(0,500),
     #random.uniform(0,500),random.uniform(0,500),random.uniform(0,500),random.uniform(0,500),random.uniform(0,500)]
z = []
for i in range(10):
    z.append(random.uniform(0,750))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.blit(bg,(0, 0))
    for i in range(10):
        sc.blit(snow,(x+i*90,y+z[i]))
        y += 0.5
        if y+z[i] > 768:
            z[i] = -y-128

    pygame.display.update()