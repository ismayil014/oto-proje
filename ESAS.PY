import pygame as pg
import sys
import random
pg.init()

class Top :
    def init(self ,pencere_en, pencere_boy)  -> None:
        self.x = random.randrange(0,pencere_en)
        self.y = random.randrange(0,pencere_boy)
        self.renk =random.randrange(5,255),random.randrange(5,255),random.randrange(5,255)
        self.cap = random.randrange(5,100)
        self.x_speed = 1
        self.y_speed = 1
    def hareket_ettir(self , pencere_en , pencere_boy) :
        self.x += self.x_speed
        self.y += self.y_speed
        
        if(self.x > pencere_en or self.x<0) :
            self.x_speed *= -1
        if(self.y > pencere_boy or self.y<0) :
            self.y_speed *= -1

    def cizdir(self , ekran) :
        pg.draw.circle(ekran,self.renk,( self.x , self.y  ),self.cap)



en , boy = 800 , 600
siyah =  0 , 0 , 0 # RGB 0- 255
beyaz = 255 ,255, 255
kirmizi = 255,0,0
gri = 100,100,100

ekran= pg.display.set_mode ( (en,boy) )

a= Top(en,boy)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT :
            sys.exit();
    ekran.fill(gri)
    
    a.çizdir(ekran)
    a.hareket_ettir(pencere_en,pencere_boy)
    
    pg.display.flip()