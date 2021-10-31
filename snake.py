# v0 : on repeint l'écran à une période de 1 seconde
# et on a du mal à sortir du programme
# v1 : pareil mais au moins on peut sortir du programme
# avec la touche 'q', ou avec la souris en fermant la fenêtre

import pygame as pg
from random import randint

pg.init()


screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
snake = [
    (10, 15),
    (11, 15),
    (12, 15),
    ] 

a, b, k = 0, 0, 0
fruit = [randint(0, 30), randint(0, 30)]
# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
while running:
    clock.tick(5)

    for i in range(30):
        for j in range(30):
            x=i*20
            y=j*20
            rect = pg.Rect(x, y, 20, 20)
            if (i+j)%2==0:
                color = (200, 200, 200)
            else:
                color = (0, 0, 0)
            pg.draw.rect(screen, color, rect)
    
    
    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        a=b
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False
            elif event.key == pg.K_UP and b!=2:
                snake = snake[1:]
                snake.append((snake[len(snake) - 1][0],snake[len(snake) - 1][1] - 1))
                a=1
                b=1
            elif event.key == pg.K_DOWN and b!=1:
                #direction = (0, 1)
                snake = snake[1:]
                snake.append((snake[len(snake) - 1][0],snake[len(snake) - 1][1] + 1))
                a=2
                b=2
            elif event.key == pg.K_RIGHT and b!=4:
                snake = snake[1:]
                snake.append((snake[len(snake)-1][0] + 1,snake[len(snake) - 1][1]))
                a=3
                b=3
            elif event.key == pg.K_LEFT and b!=3:
                snake = snake[1:]
                snake.append((snake[len(snake)-1][0] - 1,snake[len(snake)- 1][1]))
                a=4
                b=4
    if a ==1:
        snake = snake[1:]
        snake.append((snake[len(snake) - 1][0],snake[len(snake) - 1][1] - 1))
    if a ==2:
        snake = snake[1:]
        snake.append((snake[len(snake) - 1][0],snake[len(snake) - 1][1] + 1))
    if a==3:
        snake = snake[1:]
        snake.append((snake[len(snake)-1][0] + 1,snake[len(snake) - 1][1]))
    if a==4:
        snake = snake[1:]
        snake.append((snake[len(snake)-1][0] - 1,snake[len(snake)- 1][1]))

    if snake[len(snake)-1][0] == fruit[0] and snake[len(snake)-1][1] == fruit[1]:
        fruit[0], fruit[1] = randint(0, 29), randint(0, 29)
        snake.insert(0,(snake[0][0] - 1,snake[0][1]))

    for i in range(len(snake)-2):
        if snake[i][0] >= 29 or snake[i][0] >= 29 or snake[i][0] < 0 or snake[i][0] < 0:
            k+=1
        for j in range(i +1, len(snake)-2):
            if i>j and snake[i]==snake[j] and j!=0:
                k+=1
    if k > 0:
        running = False




    x= 20*fruit[0]
    y= 20*fruit[1]
    rect = pg.Rect(x, y, 20, 20)
    color = (255, 127, 0)
    pg.draw.rect(screen, color, rect)
    #On affiche notre serpent
    for i in range(len(snake)):
        # les coordonnées de rectangle que l'on dessine
        x = 20*snake[i][0] # coordonnée x (colonnes) en pixels
        y = 20*snake[i][1] # coordonnée y (lignes) en pixels
        width = 20 # largeur du rectangle en pixels
        height = 20 # hauteur du rectangle en pixels
        rect = pg.Rect(x, y, width, height)
        # appel à la méthode draw.rect()
        color = (253, 108, 158) # couleur rouge
        pg.draw.rect(screen, color, rect)
    # les coordonnées du corps du serpent
    pg.display.update()




# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()
























