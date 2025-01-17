# My first game

import pgzrun
from random import randint


WIDTH = 1000
HEIGHT = 1000

rycerz = Actor("prawo")
bandyta = Actor("bandyta_prawo")
# dodaj aktora Coina
coin = Actor("coin")
cola = Actor("cola")

rycerz.pos = (500, 500)
bandyta.pos = (350, 350)
# dodaj pozycję Coina - ma być losowa - uzyj z biblioteki random funkcji randint
coin.pos = (randint(100,900), randint(100,900))
cola.pos = (randint(100,900), randint(100,900))

rycerz_speed = 5
bandyta_speed = 5

rycerz_wygral = False
bandyta_wygral = False

punkty_bandyty = 0

def draw():
    """

    :return:
    """
    if not rycerz_wygral and not bandyta_wygral:
        screen.clear()
        screen.blit("bcg", (0, 0))
        # narysuj coina
        coin.draw()
        cola.draw()
        rycerz.draw()
        bandyta.draw()
        screen.draw.text(f"Bandyta: {punkty_bandyty}", (50, 30), color="blue", fontsize=60, owidth=1.5, ocolor=(255,255,0))

    elif rycerz_wygral:
        screen.clear()
        screen.blit("game_over", (0, 0))

    elif bandyta_wygral:
        screen.clear()
        screen.blit("bandyta_wygral", (0, 0))

def spawn_coin():
    coin.pos = (randint(100, 900), randint(100, 900))

def reset_rycerz():
    global rycerz_speed
    rycerz_speed = 5

def reset_bandyta():
    global bandyta_speed
    bandyta_speed = 5

def update():

    # rycerz łapie bandyte
    global rycerz_wygral
    if rycerz.colliderect(bandyta):
        rycerz_wygral = True
        sounds.game_over.play()
        rycerz.pos = (100, 100)

    # bandyta łapie coina
    global punkty_bandyty, bandyta_wygral
    if bandyta.colliderect(coin):
        coin.pos = (-100, 100)
        sounds.cash.play()
        punkty_bandyty += 1
        if punkty_bandyty == 3:
            sounds.game_over.play()
            rycerz.pos = (-100, -100)
            bandyta_wygral = True
        clock.schedule(spawn_coin, 3)

    global rycerz_speed
    if rycerz.colliderect(cola):
        cola.pos = (-100,100)
        rycerz_speed += 2
        clock.schedule(reset_rycerz, 4)

    global bandyta_speed
    if bandyta.colliderect(cola):
        cola.pos = (-100,100)
        bandyta_speed += 2
        clock.schedule(reset_bandyta, 4)



    # ruchy rycerza
    if keyboard.a:
        rycerz.image = "lewo"
        rycerz.x -= rycerz_speed
    if keyboard.d:
        rycerz.image = "prawo"
        rycerz.x += rycerz_speed
    if keyboard.w:
        rycerz.y -= rycerz_speed
    if keyboard.s:
        rycerz.y += rycerz_speed

    # ruchy bandyty
    if keyboard.up:
        #rycerz.image = "lewo"
        bandyta.y -= bandyta_speed
    if keyboard.down:
        #rycerz.image = "prawo"
        bandyta.y += bandyta_speed
    if keyboard.left:
        bandyta.x -= bandyta_speed
    if keyboard.right:
        bandyta.x += bandyta_speed

    # blokady rycerz
    if rycerz.y < 0:
        rycerz.y = 1000
    if rycerz.x < 0:
        rycerz.x = 1000
    if rycerz.x > 1000:
        rycerz.x = 0
    if rycerz.y > 1000:
        rycerz.y = 0

    if bandyta.y < 0:
        bandyta.y = 1000
    if bandyta.x < 0:
        bandyta.x = 1000
    if bandyta.x > 1000:
        bandyta.x = 0
    if bandyta.y > 1000:
        bandyta.y = 0
        
clock.schedule_interval(spawn_coin, 10)

pgzrun.go()