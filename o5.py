[17:45, 11.11.2022] Arif Bolum: mport pygame as pg
import sys

def hiz_hesap(ivme,zaman):
    """
    v=a*t
    
    """
    return ivme*zaman


pg.init()

en, boy=800,400

siyah=0,0,0 #RGB 0-255

beyaz=255,255,255
turuncu=252,186,3
clock=pg.time.Clock()


ekran=pg.display.set_mode( (en, boy))
cap=20
x ,y =en //2 , cap
y_hiz=0
# clock.tick(10) olduğu için saniyede 10 kare gösteriliyor bu nedenle 100 milisanıyede 1 aralık güncelleme var

dt=0.033
#  time değişkeni
t=0
#  yerçekimi ivmesi
g=4.86

while True:
         [17:45, 11.11.2022] Arif Bolum: for event in pg.event.get():
           if event.type==pg.QUIT:
            sys.exit();
    ekran.fill(turuncu)
      pg.draw.circle(ekran,beyaz,(x,y),20)
    if(g<0):
        t-=dt
    else:
        t+=dt

    y_hiz=hiz_hesap(g,t)

    
    if (y +y_hiz< boy-cap):
        y+=y_hiz
    else:
        g*=-1
        t /=2

    
    

    pg.display.flip() 
    clock.tick(30)