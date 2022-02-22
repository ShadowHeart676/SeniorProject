import pygame
import winsound
import time

pygame.init()

x = 1300
y = 700

black =(0,0,0)
screen = pygame.display.set_mode((1300,750))
pygame.display.set_caption('MasonKeyboardApplication')
screen.fill(black)
pygame.display.flip()

running = True
while running:

    for event in pygame.event.get():
        t1 = time.time()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                frequency = 270
            if event.key == pygame.K_w:
                frequency = 290
            if event.key == pygame.K_e:
                frequency = 310
            if event.key == pygame.K_r:
                frequency = 330
            if event.key == pygame.K_t:
                frequency = 350
            if event.key == pygame.K_y:
                frequency = 370
            if event.key == pygame.K_u:
                frequency = 390
            if event.key == pygame.K_i:
                frequency = 410
            if event.key == pygame.K_o:
                frequency = 440
            if event.key == pygame.K_p:
                frequency = 460
            t2=time.time()
            winsound.Beep(frequency,int(t2-t1))
        if event.type == pygame.QUIT:
            running = False
        
        pygame.display.update()