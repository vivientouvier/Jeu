import pygame, sys, random, math, time
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((349, 800))

go = pygame.Rect( 0, 357, 349, 101)

mur = pygame.image.load("Mur.png").convert_alpha()
x= random.randint(1,3)
if x==1:
    x=12
if x==2:
    x=119
if x==3:
    x==229
position_mur = pygame.Rect(x, -100, 104, 56)

mur2 = pygame.image.load("Mur.png").convert_alpha()
x= random.randint(1,3)
if x==1:
    x=12
if x==2:
    x=119
if x==3:
    x=229
position_mur2 = pygame.Rect(x, -500, 104, 56)

mur3 = pygame.image.load("Mur.png").convert_alpha()
x= random.randint(1,3)
if x==1:
    x=12
if x==2:
    x=119
if x==3:
    x==229
position_mur3 = pygame.Rect(x, -100, 104, 56)

mur4 = pygame.image.load("Mur.png").convert_alpha()
x= random.randint(1,3)
if x==1:
    x=12
if x==2:
    x=119
if x==3:
    x=229
position_mur4 = pygame.Rect(x, -500, 104, 56)

pygame.display.flip()

continuer = True
while continuer :

    continuer_jeu = True
    continuer_accueil = True
    continuer_perdu = True

    while continuer_accueil :
        pygame.time.Clock().tick(30)
        accueil = pygame.image.load("accueil.png")
        fenetre.blit(accueil, (0,0))
        font=pygame.font.Font(None, 60)
        readhighscore = open("highscore.txt", "r")
        highscore = readhighscore.read()
        highscore_display = font.render(highscore, True, (0,0,0))
        fenetre.blit(highscore_display, (135,563))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                continuer = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    continuer = False
                if event.key == K_SPACE:
                    continuer_accueil = False
                    continuer_perdu = False
                    continuer_jeu = True
                    fond = pygame.image.load("Route.png").convert()
                    fenetre.blit(fond, (0,0))

                    bandeau = pygame.image.load("bandeau.jpg").convert()
                    fenetre.blit(bandeau, (0,0))

                    voiture = pygame.image.load("Voiture.png").convert_alpha()
                    position_voiture = pygame.Rect(122, 640, 100, 157)
                    fenetre.blit(voiture, position_voiture)

                    mur = pygame.image.load("Mur.png").convert_alpha()
                    x= random.randint(1,3)
                    if x==1:
                        x=12
                    if x==2:
                        x=119
                    if x==3:
                        x=229
                    position_mur = pygame.Rect(x, -100, 104, 56)

                    mur2 = pygame.image.load("Mur.png").convert_alpha()
                    x= random.randint(1,3)
                    if x==1:
                        x=12
                    if x==2:
                        x=119
                    if x==3:
                        x=229
                    position_mur2 = pygame.Rect(x, -500, 104, 56)

                    mur3 = pygame.image.load("Mur.png").convert_alpha()
                    x= random.randint(1,3)
                    if x==1:
                        x=12
                    if x==2:
                        x=119
                    if x==3:
                        x=229
                    position_mur3 = pygame.Rect(x, -900, 104, 56)

                    mur4 = pygame.image.load("Mur.png").convert_alpha()
                    x= random.randint(1,3)
                    if x==1:
                        x=12
                    if x==2:
                        x=119
                    if x==3:
                        x=229
                    position_mur4 = pygame.Rect(x, -900, 104, 56)

                    bg  = pygame.image.load('route.png')
                    scr = pygame.display.set_mode(bg.get_size())
                    ck  = pygame.time.Clock()
                    tk  = 0
                    counter=0
                    font=pygame.font.Font(None, 25)
                    offset = 0
                    speed  = 3
                    height = bg.get_height()
                    start = time.time()

            if event.type == MOUSEBUTTONUP:
                if go.collidepoint(event.pos):
                    continuer_accueil = False
                    continuer_perdu = False
                    continuer_jeu = True
                    fond = pygame.image.load("Route.png").convert()
                    fenetre.blit(fond, (0,0))

                    bandeau = pygame.image.load("bandeau.jpg").convert()
                    fenetre.blit(bandeau, (0,0))

                    voiture = pygame.image.load("Voiture.png").convert_alpha()
                    position_voiture = pygame.Rect(122, 640, 100, 157)
                    fenetre.blit(voiture, position_voiture)

                    mur = pygame.image.load("Mur.png").convert_alpha()
                    x= random.randint(1,3)
                    if x==1:
                        x=12
                    if x==2:
                        x=119
                    if x==3:
                        x=229
                    position_mur = pygame.Rect(x, -100, 104, 56)

                    mur2 = pygame.image.load("Mur.png").convert_alpha()
                    x= random.randint(1,3)
                    if x==1:
                        x=12
                    if x==2:
                        x=119
                    if x==3:
                        x=229
                    position_mur2 = pygame.Rect(x, -500, 104, 56)

                    mur3 = pygame.image.load("Mur.png").convert_alpha()
                    x= random.randint(1,3)
                    if x==1:
                        x=12
                    if x==2:
                        x=119
                    if x==3:
                        x=229
                    position_mur3 = pygame.Rect(x, -900, 104, 56)

                    mur4 = pygame.image.load("Mur.png").convert_alpha()
                    x= random.randint(1,3)
                    if x==1:
                        x=12
                    if x==2:
                        x=119
                    if x==3:
                        x=229
                    position_mur4 = pygame.Rect(x, -900, 104, 56)

                    bg  = pygame.image.load('route.png')
                    scr = pygame.display.set_mode(bg.get_size())
                    ck  = pygame.time.Clock()
                    tk  = 0
                    counter=0
                    font=pygame.font.Font(None, 25)
                    offset = 0
                    speed  = 3
                    height = bg.get_height()
                    start = time.time()

    while continuer_jeu :
        tk += ck.tick()
        counter = time.time() - start
        counter2 = math.ceil(counter*10)
        score_display = font.render("Score : " + str(counter2), True, (255,255,255))
        if tk >= 10:
            fenetre = pygame.display.set_mode((349, 800))
            speed += 0.005
            offset = (offset+int(speed))%height
            scr.blit(bg,(0,offset))
            scr.blit(bg,(0,offset-height))
            position_mur = position_mur.move(0,speed)
            position_mur2 = position_mur2.move(0,speed)
            position_mur3 = position_mur3.move(0,speed)
            position_mur4 = position_mur4.move(0,speed)
            if position_mur.y > 1000 :
                x= random.randint(1,3)
                if x==1:
                    x=12
                if x==2:
                    x=119
                if x==3:
                    x=229
                position_mur = pygame.Rect(x, -100, 104, 56)
            if position_mur2.y > 1000 :
                x= random.randint(1,3)
                if x==1:
                    x=12
                if x==2:
                    x=119
                if x==3:
                    x=229
                position_mur2 = pygame.Rect(x, -100, 104, 56)
            if position_mur3.y > 1000 :
                x= random.randint(1,3)
                if x==1:
                    x=12
                if x==2:
                    x=119
                if x==3:
                    x=229
                position_mur3 = pygame.Rect(x, -100, 104, 56)
            if position_mur4.y > 1000 :
                x= random.randint(1,3)
                if x==1:
                    x=12
                if x==2:
                    x=119
                if x==3:
                    x=229
                position_mur4 = pygame.Rect(x, -100, 104, 56)
            fenetre.blit(mur, position_mur)
            fenetre.blit(mur2, position_mur2)
            fenetre.blit(mur3, position_mur3)
            fenetre.blit(mur4, position_mur4)
            fenetre.blit(voiture, position_voiture)
            fenetre.blit(bandeau, (0,0))
            fenetre.blit(score_display, (128, -1))
            tk = 0
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                continuer = False
            if event.type ==  KEYDOWN :
                if event.key == K_RIGHT:
                    if position_voiture.x<200:
                        position_voiture = position_voiture.move(108,0)
                if event.key == K_LEFT:
                    if position_voiture.x>100:
                        position_voiture = position_voiture.move(-108,0)
                if event.key == K_ESCAPE:
                    pygame.quit()
                    continuer = False

        if position_voiture.colliderect(position_mur) :
            if int(counter2) > int(highscore):
                with open("highscore.txt", "w") as f:
                    f.write(str(counter2))
            pygame.display.update()
            continuer_jeu = False
            continuer_accueil = False
            continuer_perdu = True
            if event.type==QUIT:
                pygame.quit()
                continuer = False
        if position_voiture.colliderect(position_mur2) :
            if int(counter2) > int(highscore):
                with open("highscore.txt", "w") as f:
                    f.write(str(counter2))
            pygame.display.update()
            continuer_jeu = False
            continuer_accueil = False
            continuer_perdu = True
            if event.type==QUIT:
                pygame.quit()
                continuer = False
        if position_voiture.colliderect(position_mur3) :
            if int(counter2) > int(highscore):
                with open("highscore.txt", "w") as f:
                    f.write(str(counter2))
            pygame.display.update()
            continuer_jeu = False
            continuer_accueil = False
            continuer_perdu = True
            if event.type==QUIT:
                pygame.quit()
                continuer = False
        if position_voiture.colliderect(position_mur4) :
            if int(counter2) > int(highscore):
                with open("highscore.txt", "w") as f:
                    f.write(str(counter2))
            pygame.display.update()
            continuer_jeu = False
            continuer_accueil = False
            continuer_perdu = True
            if event.type==QUIT:
                pygame.quit()
                continuer = False
        pygame.display.flip()

    while continuer_perdu :
        perdu = pygame.image.load("perdu.png").convert()
        font=pygame.font.Font(None, 40)
        fail = font.render("Ton score est : " + str(counter2), True, (255,255,255))
        record = font.render("Nouveau record !", True, (255,255,255))
        fenetre.blit(perdu, (0,0))
        fenetre.blit(fail, (60, 200))
        if int(counter2) > int(highscore):
            fenetre.blit(record, (65, 250))
        for event in pygame.event.get():
            if event.type == KEYDOWN :
                if event.key == K_q :
                    continuer_perdu = False
                    continuer_jeu = True
            if event.type == KEYDOWN:
                if event.key== K_ESCAPE:
                    pygame.quit()
                    continuer = False
            if event.type==QUIT:
                pygame.quit()
                continuer = False
        pygame.display.flip()

pygame.display.flip()

if event.type==QUIT:
    pygame.quit()