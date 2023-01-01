import pygame as pg
import sys
pg.init()
clock = pg.time.Clock()

en , boy = 800 , 600
siyah =  0 , 0 , 0 # RGB 0- 255
beyaz = 255 ,255, 255
gri = 125,125,12

ekran = pg.display.set_mode( (en,boy)  )

karolar = []
karo_en = 40
karo_boy = 40
for i in range(en//karo_en * boy//karo_boy) :
    karolar.append((i * karo_en % en, (i * karo_en // en)* karo_boy ))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT :
            sys.exit();
    ekran.fill(gri)
    for cord in karolar:
        pg.draw.rect(ekran,beyaz,(cord[0],cord[1],karo_en,karo_boy), 3)
    pg.display.flip()


clock.tick(30)