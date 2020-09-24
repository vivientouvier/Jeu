"""This script is a car game, you need to dodge walls and try to make the best score !"""

import random
import math
import time
import sys
import pygame

pygame.init()

fenetre = pygame.display.set_mode((349, 800))

go = pygame.Rect(0, 357, 349, 100)

CONTINUER = True
while CONTINUER:

    CONTINUER_JEU = True
    CONTINUER_ACCEUIL = True
    CONTINUER_PERDU = True

    while CONTINUER_ACCEUIL:
        pygame.time.Clock().tick(30)
        accueil = pygame.image.load("images/accueil.png")
        fenetre.blit(accueil, (0, 0))
        font = pygame.font.Font(None, 60)
        readhighscore = open("highscore.txt", "r")
        highscore = readhighscore.read()
        highscore_display = font.render(highscore, True, (0, 0, 0))
        fenetre.blit(highscore_display, (135, 563))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                CONTINUER = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    CONTINUER = False
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    CONTINUER_ACCEUIL = False
                    fond = pygame.image.load("images/Route.png").convert()
                    fenetre.blit(fond, (0, 0))

                    bandeau = pygame.image.load("images/bandeau.jpg").convert()
                    fenetre.blit(bandeau, (0, 0))


                    voiture = pygame.image.load("images/Voiture.png").convert_alpha()
                    position_voiture = pygame.Rect(122, 640, 100, 157)
                    fenetre.blit(voiture, position_voiture)


                    mur1 = pygame.image.load("images/Mur.png").convert_alpha()
                    x = random.choice([12, 119, 229])
                    position_mur1 = pygame.Rect(x, -100, 104, 56)


                    mur2 = pygame.image.load("images/Mur.png").convert_alpha()
                    x = random.choice([12, 119, 229])
                    position_mur2 = pygame.Rect(x, -500, 104, 56)

                    mur3 = pygame.image.load("images/Mur.png").convert_alpha()
                    x = random.choice([12, 119, 229])
                    position_mur3 = pygame.Rect(x, -900, 104, 56)

                    mur4 = pygame.image.load("images/Mur.png").convert_alpha()
                    x = random.choice([12, 119, 229])
                    position_mur4 = pygame.Rect(x, -900, 104, 56)

                    bg = pygame.image.load('images/route.png')
                    scr = pygame.display.set_mode(bg.get_size())
                    ck = pygame.time.Clock()
                    TK = 0
                    font = pygame.font.Font(None, 25)
                    OFFSET = 0
                    SPEED = 3
                    height = bg.get_height()
                    start = time.time()

            if event.type == pygame.MOUSEBUTTONUP:
                if go.collidepoint(event.pos):
                    CONTINUER_ACCEUIL = False
                    fond = pygame.image.load("images/Route.png").convert()
                    fenetre.blit(fond, (0, 0))

                    bandeau = pygame.image.load("images/bandeau.jpg").convert()
                    fenetre.blit(bandeau, (0, 0))


                    voiture = pygame.image.load("images/Voiture.png").convert_alpha()
                    position_voiture = pygame.Rect(122, 640, 100, 157)
                    fenetre.blit(voiture, position_voiture)


                    mur1 = pygame.image.load("images/Mur.png").convert_alpha()
                    x = random.choice([12, 119, 229])
                    position_mur1 = pygame.Rect(x, -100, 104, 56)


                    mur2 = pygame.image.load("images/Mur.png").convert_alpha()
                    x = random.choice([12, 119, 229])
                    position_mur2 = pygame.Rect(x, -500, 104, 56)

                    mur3 = pygame.image.load("images/Mur.png").convert_alpha()
                    x = random.choice([12, 119, 229])
                    position_mur3 = pygame.Rect(x, -900, 104, 56)

                    mur4 = pygame.image.load("images/Mur.png").convert_alpha()
                    x = random.choice([12, 119, 229])
                    position_mur4 = pygame.Rect(x, -900, 104, 56)

                    bg = pygame.image.load('images/route.png')
                    scr = pygame.display.set_mode(bg.get_size())
                    ck = pygame.time.Clock()
                    TK = 0
                    font = pygame.font.Font(None, 25)
                    OFFSET = 0
                    SPEED = 3
                    height = bg.get_height()
                    start = time.time()

    while CONTINUER_JEU:
        TK += ck.tick()
        counter = math.ceil((time.time() - start)*10)
        score_display = font.render("Score : " + str(counter), True, (255, 255, 255))
        if TK >= 10:
            fenetre = pygame.display.set_mode((349, 800))
            SPEED += 0.005
            OFFSET = (OFFSET+int(SPEED))%height
            scr.blit(bg, (0, OFFSET))
            scr.blit(bg, (0, OFFSET-height))
            position_mur1 = position_mur1.move(0, SPEED)
            position_mur2 = position_mur2.move(0, SPEED)
            position_mur3 = position_mur3.move(0, SPEED)
            position_mur4 = position_mur4.move(0, SPEED)
            if position_mur1.y > 1000:
                x = random.choice([12, 119, 229])
                position_mur1 = pygame.Rect(x, -100, 104, 56)
            if position_mur2.y > 1000:
                x = random.choice([12, 119, 229])
                position_mur2 = pygame.Rect(x, -100, 104, 56)
            if position_mur3.y > 1000:
                x = random.choice([12, 119, 229])
                position_mur3 = pygame.Rect(x, -100, 104, 56)
            if position_mur4.y > 1000:
                x = random.choice([12, 119, 229])
                position_mur4 = pygame.Rect(x, -100, 104, 56)
            fenetre.blit(mur1, position_mur1)
            fenetre.blit(mur2, position_mur2)
            fenetre.blit(mur3, position_mur3)
            fenetre.blit(mur4, position_mur4)
            fenetre.blit(voiture, position_voiture)
            fenetre.blit(bandeau, (0, 0))
            fenetre.blit(score_display, (128, -1))
            TK = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                CONTINUER = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if position_voiture.x < 200:
                        position_voiture = position_voiture.move(108, 0)
                if event.key == pygame.K_LEFT:
                    if position_voiture.x > 100:
                        position_voiture = position_voiture.move(-108, 0)
                if event.key == pygame.K_ESCAPE:
                    CONTINUER = False
                    pygame.quit()
                    sys.exit()

        if (position_voiture.colliderect(position_mur1)
                or position_voiture.colliderect(position_mur2)
                or position_voiture.colliderect(position_mur3)
                or position_voiture.colliderect(position_mur4)):
            if int(counter) > int(highscore):
                with open("highscore.txt", "w") as f:
                    f.write(str(counter))
            pygame.display.update()
            CONTINUER_JEU = False
            if event.type == pygame.QUIT:
                CONTINUER = False
                pygame.quit()
                sys.exit()
        pygame.display.flip()

    while CONTINUER_PERDU:
        perdu = pygame.image.load("images/perdu.png").convert()
        font = pygame.font.Font(None, 40)
        fail = font.render("Ton score est : " + str(counter), True, (255, 255, 255))
        record = font.render("Nouveau record !", True, (255, 255, 255))
        fenetre.blit(perdu, (0, 0))
        fenetre.blit(fail, (60, 200))
        if int(counter) > int(highscore):
            fenetre.blit(record, (65, 250))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    CONTINUER_PERDU = False
                if event.key == pygame.K_ESCAPE:
                    CONTINUER = False
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                CONTINUER = False
                pygame.quit()
                sys.exit()
        pygame.display.flip()
