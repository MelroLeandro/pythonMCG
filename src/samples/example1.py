import math
global teste
globals()

SetPen("blue", 1, DOT)
DrawLineList([(0,0,10,10),(30,0,50,30),(60,-10,70,0)]) #


SetPen("red", 1, 100)
DrawLinePoint((0,0),(-100,-100))#


SetPen("red", 10, 100)
DrawPointPoint((0,0))#

SetPen("blue", 1, SOLID)
SetBrush("blue", SOLID)
DrawPolygon([(30,40),(80,40),(80,80),(30,80)])#

SetUserScale(0.5)
SetDeviceOrigin(300,300)
SetPen("#00FF00", 1, SOLID)
SetBrush("#0FFF0F", SOLID)
DrawPolygon([(30,40),(80,400),(80,80),(30,80)])#

SetPen("blue", 2, SOLID)
DrawSpline([(30,40),(80,400),(80,80),(30,80)])#
DrawPolygonList([[(30,40),(80,400),(80,80),(30,80)],[(130,40),(180,400),(180,80),(130,80)]])#

DrawArcPoint((30,40),(80,-400),(80,80))#
DrawCirclePoint((-120,-120),70)#
DrawEllipse(0,-50, 50, 100)#
DrawEllipseList([(0,-50, 50, 100),(-10,-60, 50, 100),(-30,-70, 50, 80),(-50,-50, 50, 100)])

#DrawRotatedText("TESTE",0,-100,math.pi/2)
#DrawText("TESTE",0,-100)

L=[]
for i in range(0,11):
	L.append((0,0,100*math.cos(i*math.pi/10),100*math.sin(i*math.pi/10)))
DrawLineList(L)

L=[]
for i in range(0,100):
	for j in range(0,100):
		L.append((i,j))
		
DrawPointList(L)

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
#---------------
from MCGLib import *

f= FaceTriangular(ponto(0,0,0),ponto(30,30,30), ponto(100,0,10))
c= Cena()
c.addObj(f)

#............
DrawPolygonListC([("blue",[(30,40),(80,400),(80,80),(30,80)]),("red",[(130,40),(180,400),(180,80),(130,80)])])#

