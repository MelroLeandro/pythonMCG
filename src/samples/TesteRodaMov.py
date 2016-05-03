import math

SetPen("red", 10, SOLID)
DrawPointPoint((0,0))

SetPen("red", 1, SOLID)
SetBrush("blue", SOLID)

DrawPolygon([(30,40),(80,40),(80,80),(30,80)])

def R(teta,L):
        I=[]
        for (x,y) in L:
                Rx =x*math.cos(teta)-y*math.sin(teta)
                Ry =x*math.sin(teta)+y*math.cos(teta)
                I.append((Rx,Ry))
        return I

DrawPolygon(R(math.pi/3,[(30,40),(80,40),(80,80),(30,80)]))

SetBrush("blue", TRANSPARENT)
DrawCirclePoint((0,0),math.sqrt(30**2+40**2))
DrawCirclePoint((0,0),math.sqrt(80**2+80**2))
