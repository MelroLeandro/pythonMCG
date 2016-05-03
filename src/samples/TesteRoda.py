import math
import time

SetPen("red", 10, SOLID)
DrawPointPoint((0,0))

SetPen("red", 1, SOLID)
SetBrush("blue", TRANSPARENT)

DrawPolygon([(30,40),(80,40),(80,80),(30,80)])

def R(teta,L,i):
        I=[]
        for (x,y) in L:
                Rx =x*math.cos(teta)-y*math.sin(teta)+math.sin(i)
                Ry =x*math.sin(teta)+y*math.cos(teta)+math.cos(i)
                I.append((Rx,Ry))
        return I

I=[(30,40),(30,100),(80,40),(0,60),(80,80),(30,80)]
L=[]
for i in range(1,6000):
    #SetPen("black", 1, TRANSPARENT)
    #DrawPolygon(I)
    I=R(math.pi/20,I,i)
    #time.sleep(.1)
    #SetPen("red", 1, SOLID)
    DrawPolygon(I)
    L.append(I)
#DrawPolygonList(L)

