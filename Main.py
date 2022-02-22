import pygame
import time
import random
import numpy as np
from CreateNotes import *


pygame.init()
pygame.mixer.init()
x = 1200
y = 750

black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
blue=(0,0,128)


screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('MasonKeyboardApplication')
screen.fill(black)
pygame.display.flip()


font = pygame.font.Font('freesansbold.ttf',20)


def screen_display():
    w= random.randint(10,700)
    x= random.randint(10,700)
    y = random.randint(10,700)
    z=random.randint(10,700)
    pygame.draw.rect(screen,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),pygame.Rect(w,x,y,z))
    pygame.display.flip()
    time.sleep(.05)
    pygame.draw.rect(screen,black,pygame.Rect(w,x,y,z))
    pygame.display.flip()

background = pygame.image.load("Images\Keyboard Appearance Attempt.png")

running = True

while running:
    screen.blit(background, [0, 0])
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                pygame.mixer.Sound("CodeCreatedSounds/LC.wav").play()
            if event.key == pygame.K_2:
                pygame.mixer.Sound("CodeCreatedSounds/LcS.wav").play()
            if event.key == pygame.K_3:
                pygame.mixer.Sound("CodeCreatedSounds/LD.wav").play()
            if event.key == pygame.K_4:
                pygame.mixer.Sound("CodeCreatedSounds/LdS.wav").play()
            if event.key == pygame.K_5:
                pygame.mixer.Sound("CodeCreatedSounds/LE.wav").play()
            if event.key == pygame.K_6:
                pygame.mixer.Sound("CodeCreatedSounds/LF.wav").play()
            if event.key == pygame.K_7:
                pygame.mixer.Sound("CodeCreatedSounds/LfS.wav").play()
            if event.key == pygame.K_8:
                pygame.mixer.Sound("CodeCreatedSounds/LG.wav").play()
            if event.key == pygame.K_9:
                pygame.mixer.Sound("CodeCreatedSounds/LgS.wav").play()
            if event.key == pygame.K_0:
                pygame.mixer.Sound("CodeCreatedSounds/LA.wav").play()
            if event.key == pygame.K_q:
                pygame.mixer.Sound("CodeCreatedSounds/LaS.wav").play()
            if event.key == pygame.K_w:
                pygame.mixer.Sound("CodeCreatedSounds/LB.wav").play()
            if event.key == pygame.K_e:
                pygame.mixer.Sound("CodeCreatedSounds/C.wav").play()
            if event.key == pygame.K_r:
                pygame.mixer.Sound("CodeCreatedSounds/cS.wav").play()
            if event.key == pygame.K_t:
                pygame.mixer.Sound("CodeCreatedSounds/D.wav").play()
            if event.key == pygame.K_y:
                pygame.mixer.Sound("CodeCreatedSounds/dS.wav").play()
            if event.key == pygame.K_u:
                pygame.mixer.Sound("CodeCreatedSounds/E.wav").play()
            if event.key == pygame.K_i:
                pygame.mixer.Sound("CodeCreatedSounds/F.wav").play()
            if event.key == pygame.K_o:
                pygame.mixer.Sound("CodeCreatedSounds/fS.wav").play()
            if event.key == pygame.K_p:
                pygame.mixer.Sound("CodeCreatedSounds/G.wav").play()
            if event.key == pygame.K_a:
                pygame.mixer.Sound("CodeCreatedSounds/gS.wav").play()
            if event.key == pygame.K_s:
                pygame.mixer.Sound("CodeCreatedSounds/A.wav").play()
            if event.key == pygame.K_d:
                pygame.mixer.Sound("CodeCreatedSounds/aS.wav").play()
            if event.key == pygame.K_f:
                pygame.mixer.Sound("CodeCreatedSounds/B.wav").play()
            if event.key == pygame.K_g:
                pygame.mixer.Sound("CodeCreatedSounds/HC.wav").play()
            if event.key == pygame.K_h:
                pygame.mixer.Sound("CodeCreatedSounds/HcS.wav").play()
            if event.key == pygame.K_j:
                pygame.mixer.Sound("CodeCreatedSounds/HD.wav").play()
            if event.key == pygame.K_k:
                pygame.mixer.Sound("CodeCreatedSounds/HdS.wav").play()
            if event.key == pygame.K_l:
                pygame.mixer.Sound("CodeCreatedSounds/HE.wav").play()
            if event.key == pygame.K_z:
                pygame.mixer.Sound("CodeCreatedSounds/HF.wav").play()
            if event.key == pygame.K_x:
                pygame.mixer.Sound("CodeCreatedSounds/HfS.wav").play()
            if event.key == pygame.K_c:
                pygame.mixer.Sound("CodeCreatedSounds/HG.wav").play()
            if event.key == pygame.K_v:
                pygame.mixer.Sound("CodeCreatedSounds/HgS.wav").play()
            if event.key == pygame.K_b:
                pygame.mixer.Sound("CodeCreatedSounds/HA.wav").play()
            if event.key == pygame.K_n:
                pygame.mixer.Sound("CodeCreatedSounds/HaS.wav").play()
            if event.key == pygame.K_m:
                pygame.mixer.Sound("CodeCreatedSounds/HB.wav").play()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mouseX,mouseY = pos
            if(((mouseX > 68) & (mouseX < 98) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 68) & (mouseX < 112) & (mouseY > 440) & (mouseY < 670))):
                pygame.mixer.Sound("CodeCreatedSounds/LC.wav").play()
            if(((mouseX > 99) & (mouseX < 130) & (mouseY > 170) & (mouseY < 440))):
                pygame.mixer.Sound("CodeCreatedSounds/LcS.wav").play()
            if(((mouseX > 130) & (mouseX < 150) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 120) & (mouseX < 160) & (mouseY > 440) & (mouseY < 670))):
                pygame.mixer.Sound("CodeCreatedSounds/LD.wav").play()
            if(((mouseX > 150) & (mouseX < 180) & (mouseY > 170) & (mouseY < 440))):
                pygame.mixer.Sound("CodeCreatedSounds/LdS.wav").play()
            if(((mouseX > 180) & (mouseX < 210) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 170) & (mouseX < 210) & (mouseY > 440) & (mouseY < 670))):
                pygame.mixer.Sound("CodeCreatedSounds/LE.wav").play()
            if(((mouseX > 220) & (mouseX < 245) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 220) & (mouseX < 260) & (mouseY > 440) & (mouseY < 670))):
                pygame.mixer.Sound("CodeCreatedSounds/LF.wav").play()
            if(((mouseX > 245) & (mouseX < 280) & (mouseY > 170) & (mouseY < 440))):
                pygame.mixer.Sound("CodeCreatedSounds/LfS.wav").play()
            if(((mouseX > 280) & (mouseX < 300) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 270) & (mouseX < 310) & (mouseY > 440) & (mouseY < 670))):
                pygame.mixer.Sound("CodeCreatedSounds/LG.wav").play()
            if(((mouseX > 300) & (mouseX < 328) & (mouseY > 170) & (mouseY < 440))):
                pygame.mixer.Sound("CodeCreatedSounds/LgS.wav").play()
            if(((mouseX > 328) & (mouseX < 348) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 320) & (mouseX < 360) & (mouseY > 440) & (mouseY < 670))):
                pygame.mixer.Sound("CodeCreatedSounds/LA.wav").play()
            if(((mouseX > 348) & (mouseX < 380) & (mouseY > 170) & (mouseY < 440))):
                pygame.mixer.Sound("CodeCreatedSounds/LaS.wav").play()
            if(((mouseX > 380) & (mouseX < 410) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 368) & (mouseX < 410) & (mouseY > 440) & (mouseY < 670))):
                pygame.mixer.Sound("CodeCreatedSounds/LB.wav").play()
            
            if(((mouseX > 68+347) & (mouseX < 98+347) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 68+347) & (mouseX < 112+347) & (mouseY > 440) & (mouseY < 670))):
                pygame.mixer.Sound("CodeCreatedSounds/C.wav").play()
            if(((mouseX > 99+347) & (mouseX < 130+347) & (mouseY > 170) & (mouseY < 440))):
                pygame.mixer.Sound("CodeCreatedSounds/cS.wav").play()
            if(((mouseX > 130+347) & (mouseX < 150+347) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 120+347) & (mouseX < 160+347) & (mouseY > 440) & (mouseY < 670))):
                pygame.mixer.Sound("CodeCreatedSounds/D.wav").play()
            if(((mouseX > 150+347) & (mouseX < 180+347) & (mouseY > 170) & (mouseY < 440))):
                pygame.mixer.Sound("CodeCreatedSounds/dS.wav").play()
            if(((mouseX > 180+347) & (mouseX < 210+347) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 170+347) & (mouseX < 210+347) & (mouseY > 440) & (mouseY < 670))):
                pygame.mixer.Sound("CodeCreatedSounds/E.wav").play()
            if(((mouseX > 220+347) & (mouseX < 245+347) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 220+347) & (mouseX < 260+347) & (mouseY > 440) & (mouseY < 670))):
                pygame.mixer.Sound("CodeCreatedSounds/F.wav").play()
            if(((mouseX > 245+347) & (mouseX < 280+347) & (mouseY > 170) & (mouseY < 440))):
                pygame.mixer.Sound("CodeCreatedSounds/fS.wav").play()
            if(((mouseX > 280+347) & (mouseX < 300+347) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 270+347) & (mouseX < 310+347) & (mouseY > 440) & (mouseY < 670))):
                pygame.mixer.Sound("CodeCreatedSounds/G.wav").play()
            if(((mouseX > 300+347) & (mouseX < 328+347) & (mouseY > 170) & (mouseY < 440))):
                pygame.mixer.Sound("CodeCreatedSounds/gS.wav").play()
            if(((mouseX > 328+347) & (mouseX < 348+347) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 320+347) & (mouseX < 360+347) & (mouseY > 440) & (mouseY < 670))):
                pygame.mixer.Sound("CodeCreatedSounds/A.wav").play()
            if(((mouseX > 348+347) & (mouseX < 380+347) & (mouseY > 170) & (mouseY < 440))):
                pygame.mixer.Sound("CodeCreatedSounds/aS.wav").play()
            if(((mouseX > 380+347) & (mouseX < 410+347) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 368+347) & (mouseX < 410+347) & (mouseY > 440) & (mouseY < 670))):
                pygame.mixer.Sound("CodeCreatedSounds/B.wav").play()

            if(((mouseX > 68+692) & (mouseX < 98+692) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 68+692) & (mouseX < 112+692) & (mouseY > 440) & (mouseY < 670))):
                pygame.mixer.Sound("CodeCreatedSounds/HC.wav").play()
            if(((mouseX > 99+692) & (mouseX < 130+692) & (mouseY > 170) & (mouseY < 440))):
                pygame.mixer.Sound("CodeCreatedSounds/HcS.wav").play()
            if(((mouseX > 130+692) & (mouseX < 150+692) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 120+692) & (mouseX < 160+692) & (mouseY > 440) & (mouseY < 670))):
                pygame.mixer.Sound("CodeCreatedSounds/HD.wav").play()
            if(((mouseX > 150+692) & (mouseX < 180+692) & (mouseY > 170) & (mouseY < 440))):
                pygame.mixer.Sound("CodeCreatedSounds/HdS.wav").play()
            if(((mouseX > 180+692) & (mouseX < 210+692) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 170+692) & (mouseX < 210+692) & (mouseY > 440) & (mouseY < 670))):
                pygame.mixer.Sound("CodeCreatedSounds/HE.wav").play()
            if(((mouseX > 220+692) & (mouseX < 245+692) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 220+692) & (mouseX < 260+692) & (mouseY > 440) & (mouseY < 670))):
                pygame.mixer.Sound("CodeCreatedSounds/HF.wav").play()
            if(((mouseX > 245+692) & (mouseX < 280+692) & (mouseY > 170) & (mouseY < 440))):
                pygame.mixer.Sound("CodeCreatedSounds/HfS.wav").play()
            if(((mouseX > 280+692) & (mouseX < 300+692) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 270+692) & (mouseX < 310+692) & (mouseY > 440) & (mouseY < 670))):
                pygame.mixer.Sound("CodeCreatedSounds/HG.wav").play()
            if(((mouseX > 300+692) & (mouseX < 328+692) & (mouseY > 170) & (mouseY < 440))):
                pygame.mixer.Sound("CodeCreatedSounds/HgS.wav").play()
            if(((mouseX > 328+692) & (mouseX < 348+692) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 320+692) & (mouseX < 360+692) & (mouseY > 440) & (mouseY < 670))):
                pygame.mixer.Sound("CodeCreatedSounds/HA.wav").play()
            if(((mouseX > 348+692) & (mouseX < 380+692) & (mouseY > 170) & (mouseY < 440))):
                pygame.mixer.Sound("CodeCreatedSounds/HaS.wav").play()
            if(((mouseX > 380+692) & (mouseX < 410+692) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 368+692) & (mouseX < 410+692) & (mouseY > 440) & (mouseY < 670))):
                pygame.mixer.Sound("CodeCreatedSounds/HB.wav").play()
        if event.type == pygame.QUIT:
            running = False
        pygame.display.update()

