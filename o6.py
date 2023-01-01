import pygame as pg
import sys
import random

def top_oluştur() :
    global en,boy
    cap = random.randrange(10,40)
    x = random .randrange(cap,en-cap)
    y = random.randrange(cap,boy-cap)
    x_speed = random.randrange(1,5)
    y_speed = random.randrange(1,5)
    return [x,y,x_speed,y_speed,cap]


def konum_guncelle(x,y,x_speed,y_speed,y_cap) :
    x += x_speed
    y += y_speed
    if x >= en - y_cap :
        x_speed *= -1
    if x <= 0 + y_cap :
        x_speed *= -1

    if y >= boy - y_cap :
        y_speed *= -1
    if y <=0 + y_cap :
        y_speed *= -1

pg.init()


en,boy = 800 , 600

siyah = 0 , 0, 0 # RGB0- 255
beyaz = 255 , 255 , 255
kırmızı =255 , 0 , 0
gri = 100, 100 , 100
turuncu=252,186,3

ekran = pg.display.set_mode( (en,boy) )

toplar = []

for i in range(10):
    toplar.append(top_oluştur())

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT :
            sys.exit() ;
    ekran.fill(gri)
    
    for i in range(len(toplar)) :
        
        pg.draw.circle(ekran,kırmızı,( toplar[i][0] , toplar[i][1]),toplar[i][4])
        konum_guncelle(toplar[i][0],toplar[i][1],toplar[i][2],toplar[i][3],toplar[i][4])

    pg.display.flip()deryt9pti[;hd
    