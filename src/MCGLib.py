# -*- coding: cp1252 -*-
#
# Matemática para Computação Gráfica 2011-2012
# 30-6-2012
#

#
# Importa módulo com funções elementares
#

import math     # Para o cálculo
import sys, os  # Para carregar ficheiros
import time
import copy
from operator import itemgetter # Para ordenar vértices


LDrawPath="."             # caminho para estrutuas do LDRAW 
Scale=2                # factor de escala entre Lego unit e pythonMCG Unit
                        # Scale = 0.05

global LegoFiles          # Ficheiros do LDRAW
global MeshData           # malhas
global Frame

contador = 1


#//////////////////////////////// COLOR TABLE \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*
#/////
#/////  Values from Official "Ldraw Color Chart"
#/////  Dictionary of  ColorNumber:[Red, Green, Blu, Alpha]
#/////
legocolor={  0: [  51,  51,  51, 255],    #   0  Black LDraw
             1: [   0,  51, 178, 255],    #   1  Blue LDraw
             2: [   0, 127,  51, 255],    #   2  Green LDraw
             3: [   0, 153, 159, 255],    #   3  Dark Cyan LDraw
             4: [ 204,   0,   0, 255],    #   4  Red LDraw
             5: [ 223, 102, 149, 255],    #   5  Magenta LDraw
             6: [ 102,  51,   0, 255],    #   6  Brown LDraw
             7: [ 153, 153, 153, 255],    #   7  Grey LDraw
             8: [ 102, 102,  88, 255],    #   8  Dark Grey LDraw
             9: [   0, 128, 255, 255],    #   9  Light Blue LDraw
            10: [  51, 255, 102, 255],    #  10  Light Green LDraw
            11: [  51, 166, 167, 255],    #  11  Cyan LDraw
            12: [ 255, 201, 196, 255],    #  12  Light Red LDraw
            13: [ 255, 176, 204, 255],    #  13  Pink LDraw
            14: [ 255, 229,   0, 255],    #  14  Yellow LDraw
            15: [ 255, 255, 255, 255],    #  15  White LDraw
            17: [ 102, 240, 153, 255],
            18: [ 204, 142, 104, 255],
            20: [ 224, 204, 240, 255],
            21: [ 196,  40,  27, 255],
            22: [ 153,  51, 153, 255],
            23: [  76,   0, 204, 255],
            24: [ 245, 205,  47, 255],
            25: [  98,  71,  50, 255],
            26: [  27,  42,  52, 255],
            27: [ 229, 255, 168, 255],
            28: [ 250, 163, 157, 255],
            29: [ 161, 196, 139, 255],
            32: [  51,  51,  51, 127],    #  32  Transparent Black LDraw
            33: [   0,  51, 178, 127],    #  33  Transparent Blue LDraw
            34: [   0, 127,  51, 127],    #  34  Transparent Green LDraw
            35: [   0, 153, 159, 127],    #  35  Transparent Dark Cyan LDraw
            36: [ 204,   0,   0, 127],    #  36  Transparent Red LDraw
            37: [ 223, 102, 149, 127],    #  37  Transparent Magenta LDraw
            38: [ 102,  51,   0, 127],    #  38  Transparent Brown LDraw
            39: [ 153, 153, 153, 127],    #  39  Transparent Grey LDraw
            40: [ 102, 102,  88, 127],    #  40  Transparent Dark Grey LDraw
            41: [   0, 128, 255, 127],    #  41  Transparent Light Blue LDraw
            42: [  51, 255, 102, 127],    #  42  Transparent Light Green LDraw
            43: [  51, 166, 167, 127],    #  43  Transparent Cyan LDraw
            44: [ 255, 201, 196, 127],    #  44  Transparent Light Red LDraw
            45: [ 255, 176, 204, 127],    #  45  Transparent Pink LDraw
            46: [ 255, 229,   0, 127],    #  46  Transparent Yellow LDraw
            47: [ 255, 255, 255, 127],    #  47  Transparent White LDraw
            48: [ 132, 182, 141, 255],
            49: [ 248, 241, 132, 255],
            50: [ 236, 232, 222, 255],
           100: [ 238, 196, 182, 255],
           101: [ 218, 134, 121, 255],
           102: [ 110, 153, 201, 255],
           103: [ 199, 193, 183, 255],
           104: [ 107,  50, 123, 255],
           105: [ 226, 155,  63, 255],
           106: [ 218, 133,  64, 255],
           107: [   0, 143, 155, 255],
           108: [ 104,  92,  67, 255],
           110: [  67,  84, 147, 255],
           111: [ 191, 183, 177, 255],
           112: [ 104, 116, 172, 255],
           113: [ 228, 173, 200, 255],
           115: [ 199, 210,  60, 255],
           116: [  85, 165, 175, 255],
           118: [ 183, 215, 213, 255],
           119: [ 164, 189,  70, 255],
           120: [ 217, 228, 167, 255],
           121: [ 231, 172,  88, 255],
           123: [ 211, 111,  76, 255],
           124: [ 146,  57, 120, 255],
           125: [ 234, 184, 145, 255],
           126: [ 165, 165, 203, 255],
           127: [ 220, 188, 129, 255],
           128: [ 174, 122,  89, 255],
           131: [ 156, 163, 168, 255],
           133: [ 213, 115,  61, 255],
           134: [ 216, 221,  86, 255],
           135: [ 116, 134, 156, 255],
           136: [ 135, 124, 144, 255],
           137: [ 224, 152, 100, 255],
           138: [ 149, 138, 115, 255],
           140: [  32,  58,  86, 255],
           141: [  39,  70,  44, 255],
           143: [ 207, 226, 247, 255],
           145: [ 121, 136, 161, 255],
           146: [ 149, 142, 163, 255],
           147: [ 147, 135, 103, 255],
           148: [  87,  88,  87, 255],
           149: [  22,  29,  50, 255],
           150: [ 171, 173, 172, 255],
           151: [ 120, 144, 129, 255],
           153: [ 149, 121, 118, 255],
           154: [ 123,  46,  47, 255],
           157: [ 255, 246, 123, 255],
           158: [ 225, 164, 194, 255],
           168: [ 117, 108,  98, 255],
           176: [ 151, 105,  91, 255],
           178: [ 180, 132,  85, 255],
           179: [ 137, 135, 136, 255],
           180: [ 215, 169,  75, 255],
           190: [ 249, 214,  46, 255],
           191: [ 232, 171,  45, 255],
           192: [ 105,  64,  39, 255],
           193: [ 207,  96,  36, 255],
           194: [ 163, 162, 164, 255],
           195: [  70, 103, 164, 255],
           196: [  35,  71, 139, 255],
           198: [ 142,  66, 133, 255],
           199: [  99,  95,  97, 255],
           200: [ 130, 138,  93, 255],
           208: [ 229, 228, 222, 255],
           209: [ 176, 142,  68, 255],
           210: [ 112, 149, 120, 255],
           211: [ 121, 181, 181, 255],
           212: [ 159, 195, 233, 255],
           213: [ 108, 129, 183, 255],
           216: [ 143,  76,  42, 255],
           217: [ 124,  92,  69, 255],
           218: [ 150, 112, 159, 255],
           219: [ 107,  98, 155, 255],
           220: [ 167, 169, 206, 255],
           221: [ 205,  98, 152, 255],
           222: [ 228, 173, 200, 255],
           223: [ 220, 144, 149, 255],
           224: [ 240, 213, 160, 255],
           225: [ 235, 184, 127, 255],
           226: [ 253, 234, 140, 255],
           232: [ 125, 187, 221, 255],
           268: [  52,  43, 117, 255],
           418: [   0, 191,  89, 255],
           494: [ 204, 204, 204, 255],
           503: [ 230, 227, 218, 255]}
#/////
#/////  Color   16 = Null-colour
#/////        Pieces using null colour code use whatever colour code is
#/////        entered on the command line when rendering with LDraw or,
#/////        if no colour code is specified, they default to a #7 Grey.
#/////  Clear Colours.
#/////        Colors from 32 to 47 are the clear (transparent) version
#/////        of corrispective colors from 0 to 15 (Alpha = 200).
#/////
#//////////////////////////////// COLOR TABLE \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*

matrizId=[[ 1, 0, 0, 0],[ 0, 1, 0, 0],[ 0, 0, 1, 0],[ 0, 0, 0, 1]]

#
# Estrutura para armazenamento de vectores
#
class vector:
    ''' vector(x,y,z) -> Estrutura para armazenamento de vectores '''
    def __init__(self, initx, inity, initz): # Exer 1.1
        ''' construtor de vectores Exer 1.1'''
        self.x = initx  #x do vector
        self.y = inity  #y do vector
        self.z = initz  #z do vector

    def __str__(self):
        ''' v.__str__() <==> str(v) converte vector v para string'''
        return '[%s,%s,%s]' % (self.x, self.y, self.z)

    def __repr__(self):
        ''' v.__repr__() <==> repr(v) resultado de avaliar um vector v'''
        return 'vector(%s,%s,%s)' % (self.x, self.y, self.z)

    def ponto(self): # Exer 1.6
        ''' v.ponto() -> False porque v não é ponto Exer 1.6'''
        return False

    def vector(self): # Exer 1.7
        ''' v.vector() -> True porque é v vector Exer 1.7'''
        return True

    def soma(self,outro): # Exer 1.8
        ''' v.soma(w) <==> v+w soma dos vectores v e w  Exer 1.8'''
        if outro.vector():
            return vector(self.x + outro.x, self.y + outro.y, self.z + outro.z)
        else:
            print 'Parâmetro inválido'

    def __add__(self, outro): # Exer 2.1
        ''' v.__add__(w) <==> v+w soma os vectores v e w Exer 2.1
            v.__add__(P) <==> v+P soma o vector v ao ponto P'''
        if outro.vector():
            return vector(self.x + outro.x, self.y + outro.y, self.z + outro.z)
        else:
            return ponto(self.x + outro.x, self.y + outro.y, self.z + outro.z)

    def __eq__(self, outro): # Exer 2.2
        ''' v.__eq__(w) <==> v==w igualdade de vectores Exer 2.2'''
        return (self.x == outro.x) and (self.y == outro.y) and (self.z == outro.z)

    def __neg__(self): # Exer 2.3
        ''' v.__neg__() <==> -v vector simétrico Exer 2.3'''
        return self.mult(-1)

    def __sub__(self, outro): # Exer 2.4
        ''' v.__sub__(w) <==> v-w diferença de vectores  Exer 2.4'''
        if outro.vector():
            return vector(self.x - outro.x, self.y - outro.y, self.z - outro.z)
        else:
            print 'Parâmetro inválido'

    def normalizar(self): # Exer 2.5
        ''' v.normalizar() <==> 1/||v||*v normliza o vector Exer 2.5'''
        return self.mult(1/self.comprimento())

    def interno(self, outro): # Exer 2.6
        ''' v.interno(w) <==> v.w produto interno Exer 2.6'''
        if outro.vector():
            return self.x*outro.x+self.y*outro.y+self.z*outro.z
        else:
            print 'Parâmetro inválido'


    def mult(self,a): # Exer 1.9
        ''' v.mult(a) <==> a.w produto do vector w pelo escalar a Exer 1.9'''
        return vector(a*self.x, a*self.y, a*self.z)

    def comprimento(self): # Exer 1.10
        ''' v.comprimento() <==> ||v|| norma do vector v Exer 1.10'''
        return math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)

    def paralelo(self,outro): # Exer 1.16
        ''' v.paralelo(w) <==> True se e só se v é paralelo a w Exer 1.16'''
        if outro.vector():
            if outro.x!=0:
                a=float(self.x)/float(outro.x)
            elif outro.y!=0:
                a=float(self.y)/float(outro.y)
            elif outro.z!=0:
                a=float(self.z)/float(outro.z)
            else:
                return True
            return self.x==a*outro.x and self.y==a*outro.y and self.z==a*outro.z
        else:
            print 'Parâmetros inválidos'

    def externo(self, outro): # Exer 3.1
        ''' v.externo(u) <==> vxu produto externo de v por u Exer 1.10'''
        if outro.vector():
            return vector(self.y * outro.z - self.z * outro.y,
                          self.z * outro.x - self.x * outro.z,
                          self.x * outro.y - self.y * outro.x)
        else:
            print 'Parâmetros inválidos'

#
# Estrutura para armazenamento de pontos
#
class ponto:
    ''' ponto(x,y,z)-> Estrutura para armazenamento de pontos '''
    def __init__(self, initx, inity, initz): # Exer 1.2
        ''' construtor de vectores Exer 1.2'''
        self.x = initx # x do ponto
        self.y = inity # y do ponto
        self.z = initz # z do ponto

    def __str__(self):
        ''' P.__str__() <==> str(P) converte ponto P para string'''
        return '(%s,%s,%s)' % (self.x, self.y, self.z)

    def __repr__(self):
        ''' P.__repr__() <==> repr(P) resultado de avaliar um ponto P'''
        return 'ponto(%s,%s,%s)' % (self.x, self.y, self.z)

    def posicao(self): # Exer 1.3
        ''' P.posicao()-> vector posição do ponto P Exer 1.3'''
        return vector(self.x, self.y, self.z)

    def ponto(self): # Exer 1.4
        ''' P.ponto-> True porque P é ponto Exer 1.4'''
        return True

    def vector(self): # Exer 1.5
        ''' P.ponto-> False porque P não é vector Exer 1.5'''
        return False

    def Vector(self,Q): # Exer 1.12
        ''' P.Vector(Q)-> vector PQ Exer 1.5'''
        return vector(Q.x-self.x, Q.y-self.y, Q.z-self.z)

    def __add__(self, outro): # Exer 2.8
        ''' P.__add__(v) <==> P+v soma o ponto P ao vector v Exer 2.8'''
        if outro.vector():
            return ponto(self.x + outro.x, self.y + outro.y, self.z + outro.z)
        else:
            print 'Parâmetro inválido'

    def __eq__(self, outro): # Exer 2.9
        ''' P.__eq__(Q) <==> P==w igualdade de vectores Exer 2.2'''
        return (self.x == outro.x) and (self.y == outro.y) and (self.z == outro.z)

    def __sub__(self, outro): # Exer 2.10
        ''' P.__sub__(Q) <==> P-Q vecto QP Exer 2.10
            P.__sub__(v) <==> P-v soma o vector v ao ponto P'''
        if outro.ponto():
            return vector(self.x - outro.x, self.y - outro.y, self.z - outro.z)
        else:
            return ponto(self.x - outro.x, self.y - outro.y, self.z - outro.z)

    def recta(self,outro): # Exer 2.12
        ''' P.recta(Q) -> a recta que passa por P e Q Exer 2.12
            P.recta(v) -> a recta que passa por P e tem a direcção de v'''
        if outro.ponto():
            return recta(self,outro-self)
        else:
            return recta(self,outro)
        
    def plano(self,outro1,outro2): #3.3
        ''' P.plano(Q,R)-> o plano que passa por P, Q e R
            P.plano(u,v)-> o plano que passa por P, e tem a direcção de u e v '''
        if outro1.ponto() and outro2.ponto():
            return plano(self,(self-outro1).externo(self-outro2))
        elif outro1.vector() and outro2.vector():
            return plano(self,outro1.externo(outro2))
        else:
            print 'Parâmetros inválidos'

    def proj(self,M):
        ''' P.proj(M)-> projecta segundo a matriz M no plano XOY'''
        TM=M.avalia(self)
        return [(TM.x,TM.y),TM.z]

    def transf(self,T):
        ''' P.tranf(T)-> aplica transformacao T ao ponto'''
        return T.avalia(self)
        

#
# Recta
#

class recta: 
    def __init__(self, ponto, vector): #Exer 2.11
        ''' construtor de rectas Exer 2.11'''
        self.ponto = ponto                 # ponto na recta
        self.vector = vector.normalizar()  # vector director

    def __repr__(self): #Exer 2.11
        ''' r.__repr__() <==> repr(r) resultado de avaliar uma recta r'''
        return 'recta(%s,%s)' % (repr(self.ponto), repr(self.vector))

    def tem_ponto(self,P): #Exer 2.13
        ''' r.ponto(P) -> True sse o ponto P está na recta r Exer2.13'''
        return self.vector.paralelo(self.ponto-P)

    def __eq__(self, outro): # Exer 2.14
        ''' r.__eq__(s) <==> r==s se r e s são a mesma recta Exer 2.14'''
        return self.tem_ponto(outro.ponto) and (self.vector==outro.vector or self.vector==-outro.vector)
            

#
# Plano
#

class plano: 
    def __init__(self, ponto, vector): #Exer 3.2
        ''' construtor de planos Exer 2.11'''
        self.ponto = ponto                 # ponto do plano
        self.vector = vector.normalizar()  # vector normal ao plano
        self.animar = False
        self.pigmento = "pigment { rgb <0/255, 160/255, 0/255>] }"

    def __repr__(self): #Exer 3.2
        ''' p.__repr__() <==> repr(r) resultado de avaliar uma plano p'''
        return 'plano(%s,%s)' % (repr(self.ponto), repr(self.vector))

    def tem_ponto(self,P): #Exer 3.5
        ''' p.ponto(P) -> True sse o ponto P está no plano r Exer3.5'''
        return self.vector.interno(P-self.ponto) == 0.0

    def __eq__(self, outro): # Exer 3.6
        ''' p.__eq__(q) <==> p==q se p e q são o mesmo plano Exer 3.6'''
        return self.tem_ponto(outro.ponto) and (self.vector==outro.vector or self.vector==-outro.vector)

    def plano(self):
        return True

    def FaceTriang(self):
        return False

    def FaceQuad(self):
        return False

    def Mesh(self):
        return False


    def Lego(self):
        return False
#
# Matriz 4x4
#
class Transf:
    
    def __init__(self):
        self.matriz=[[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]

    def __str__(self):
        return 'matriz(%s)' % (self.matriz)

    def __repr__(self):
        return 'matriz(%s)' % (self.matriz)

    def avalia(self,P):
        ''' Avalia transformação num ponto'''
        coluna=[P.x,P.y, P.z, 1]
        transf=[0,0,0,0]
        for i in range(4):
            aux=0
            for j in range(4):
                aux = self.matriz[i][j]*coluna[j]+aux
            transf[i]=aux
        if transf[3]!=1:
            return ponto(transf[0]/transf[3],transf[1]/transf[3],transf[2]/transf[3])
        else:
            return ponto(transf[0],transf[1],transf[2])

    def __mul__(self,T):
        ''' Composição de transformações'''
        M=Transf()
        for i in range(4):
            for j in range(4):
                aux=0
                for k in range(4):
                    aux = self.matriz[i][k]*T.matriz[k][j]+aux
                M.matriz[i][j]=aux
        return M
        
    def escalonamento(self,sx,sy,sz):
        self.matriz=[[sx,0,0,0], [0,sy,0,0], [0,0,sz,0], [0,0,0,1]]

    def translacao(self,vector):
        self.matriz=[[1,0,0,vector.x], [0,1,0,vector.y], [0,0,1,vector.z], [0,0,0,1]]

    def rodaX(self,teta):
        ''' Rotação em torno do eixo do X'''
        self.matriz=[[1,0,0,0],
                     [0,math.cos(teta), math.sin(teta),0],
                     [0,-math.sin(teta), math.cos(teta),0],
                     [0,0,0,1]]

    def rodaY(self,teta):
        ''' Rotação em torno do eixo do Y'''
        self.matriz=[[math.cos(teta), 0, math.sin(teta),0],
                     [0,1,0,0], 
                     [-math.sin(teta), 0, math.cos(teta),0],
                     [0,0,0,1]]

    def rodaZ(self,teta):
        ''' Rotação em torno do eixo do Z'''
        self.matriz=[[math.cos(teta),-math.sin(teta),0,0],
                     [math.sin(teta), math.cos(teta),0,0],
                     [0,0,1,0], [0,0,0,1]]

    def ProjOrto(self):
        ''' Projecção ortográfica no plano XOY'''
        self.matriz=[[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]

    def ProjTrime(self):
        ''' Projecção Trimétrica no plano z=0 após uma rotação de 90 graus 
          no eixo x'''
        self.matriz=[[1,0,0,0], [0,0,0,0], [0,-1,1,0], [0,0,0,1]]

    def ProjCavaleira(self):
        '''Projecção cavaleira'''
        L=1
        teta=math.pi/4.0
        self.matriz=[[1,0,L*math.cos(teta),0], [0,1,L*math.sin(teta),0], [0,0,1,0], [0,0,0,1]]

    def ProjCabinet(self):
        '''Projecção cabinet'''
        L=1.0/2.0
        teta=math.atan(2)
        self.matriz=[[1,0,L*math.cos(teta),0], [0,1,L*math.sin(teta),0], [0,0,1,0], [0,0,0,1]]             

    def Persp1fuga(self,pz):
        ''' Prespectiva com um ponto de fuga localizado em Z=r, projectado no
          plano z=0'''
        self.matriz=[[1,0,0,0], [0,1,0,0], [0,0,0,0], [0,0,1.0/pz,1]]

    def Persp2fuga(self,px,py):
        ''' Prespectiva com dois pontos de fuga localizado em X=px e Y=py, projectado no
            plano z=0'''
        self.matriz=[[1,0,0,0], [0,1,0,0], [0,0,1,0], [1.0/px,1.0/py,0,1]]

    def Persp3fuga(self,px,py,pz):
        ''' Prespectiva com três pontos de fuga localizado em X=px e Y=py, projectado no
            plano z=0'''
        self.matriz=[[1,0,0,0], [0,1,0,0], [0,0,1,0], [1.0/px,1.0/py,1.0/pz,1]]

    def vista(self,O,X,Y,Z):
        M=Transf() # matriz de mudança de base
        M.matriz=[[X.x,X.y,X.z,0], [Y.x,Y.y,Y.z,0], [Z.x,Z.y,Z.z,0], [0,0,0,1]]
        T=Transf() # matriz de translação para a origem
        T.matriz=[[1,0,0,-O.x], [0,1,0,-O.y], [0,0,1,-O.z], [0,0,0,1]]
        self.matriz=(M*T).matriz
                
#
# Estrutura para armazenamento de faces triangulares
#
class FaceTriang:
    def __init__(self, ponto1, ponto2, ponto3):
        self.ponto = [ponto1,ponto2,ponto3]

    def __str__(self):
        return 'FaceTriangular(%s)' % (self.ponto)

    def __repr__(self):
        return 'FaceTriangular(%s)' % (self.ponto)

    def FaceTriang(self):
        return True

    def FaceQuad(self):
        return False

    def Mesh(self):
        return False

    def Lego(self):
        return False

#
# Estrutura para armazenamento de faces 
#
class FaceQuad:
    def __init__(self,ponto1, ponto2, ponto3, ponto4):
        self.ponto = [ponto1, ponto2, ponto3, ponto4]

    def __str__(self):
        return 'FaceQuad(%s)' % (self.ponto)

    def __repr__(self):
        return 'FaceQuad(%s)' % (self.ponto)

    def FaceQuad(self):
        return True

    def FaceTriang(self):
        return False

    def Mesh(self):
        return False

    def Lego(self):
        return False

#
# Estrutura para armazenamento dum mesh file
#

class Mesh:
    ''' Classe Malha'''
    def __init__(self):
        self.faces={}     # dic de faces
        self.nos={}       # dic de vértices
        self.nome ='vazio' # Nome do ficheiro
        self.numNos=0     # número de vértices
        self.numFaces=0   # número de faces
        self.ponto = ponto(0,0,0) # loc da malha
        self.escalaX = 1  # Escalas para X,Y e Z
        self.escalaY = 1
        self.escalaZ = 1
        self.cor = 16     # Cor da malha

    def __str__(self):
        return 'mesh(%s,%s,%s)' % (self.nome,self.numNos,self.numFaces)

    def __repr__(self):
        return 'mesh(%s,%s,%s)' % (self.nome,self.numNos,self.numFaces)

    def addNo(self,P):
        ''' Adiciona ponto à lista de vértices''' 
        self.nos[self.numNos]=P
        self.numNos=self.numNos+1
        return self.numNos-1

    def addFace(self,face,color):
        ''' Adiciona face à lista de faces'''
        self.faces[self.numFaces]=(color,face) # face e cor
        self.numFaces=self.numFaces+1
        return self.numFaces-1

    def load(self,filename):
        ''' Carrega malha de ficheiro gmsh'''
        try:
            ifile = open (filename, 'r')
        except:
            print "O ficheiro nao existe.";
            return
        self.nome = filename

        # -- Extract NODES and ELEMENTS from given gmsh file.

        while 1:
            line = ifile.readline()
            if '$MeshFormat' in line:
                line = ifile.readline()
                words = line.split()
                desNum = int (words[2])
            elif '$Nodes' in line:
                line = ifile.readline()
                Nnode = int (line)
                self.numNos=Nnode
                for i in range (1, Nnode+1):
                    line = ifile.readline()
                    words = line.split()
                    self.nos[int(words[0])]=ponto(float(words[1]),float(words[2]),float(words[3]))
            elif '$Elements' in line:
                line = ifile.readline()
                Nel = int(line)
                self.numFaces= Nel
                for i in range (1, Nel+1):
                    # -- If all elements were quads, each line has 8 numbers.
                    #    The first one is a tag, and the last 3 are node numbers.
                    line = ifile.readline()
                    words = line.split()
                    if desNum== 8:
                        self.faces[int(words[0])]=(int(words[5]),int(words[6]),int(words[7]))
                    elif desNum== 5:
                        self.faces[int(words[0])]=(int(words[1]),int(words[2]),int(words[3]),int(words[4]))
                break

        ifile.close()

    def FaceQuad(self):
        return False

    def FaceTriang(self):
        return False

    def Mesh(self):
        return True

    def Lego(self):
        return False
    


#= [CLASS] LegoFile ======================================================
#
class CLFile:
    ''' Carrega ficheiros na árvore de ficheitos das Parts '''
    def __init__(self, filename = None, searchPath = "") :
        self.Lines = []
        self.isPart = False
        self.Name = filename
        
        if filename == None :
           return
        aFile=None
        try:
            aFile = open(filename, "rb")
        except IOError:
            # try in the search path
            filename = searchPath + "/" + self.Name
            try:
                aFile = open(filename, "rb")
            except IOError:
                # try in the MODEL path
                filename = LDrawPath + "/" + "MODELS" + "/" + self.Name
                try:
                    aFile = open(filename, "rb")
                except IOError:
                    self.isPart = True
                    # Search as partes no Ldraw PARTS directory
                    filename = LDrawPath + "/" + "PARTS" + "/" + self.Name
                    try:
                        aFile = open(filename, "rb")
                    except IOError:
                        # Search as partes no Ldraw P directory
                        filename = LDrawPath + "/" + "P" + "/" + self.Name
                        try:
                            aFile = open(filename, "rb")
                        except IOError:
                            print("Nao encontro ficheiro %s!" % (self.Name))
                            self.isPart = False
        self.Name = filename
        if aFile:
            self.Lines = aFile.readlines()
            aFile.close()
    def __str__(self):
         retstr =  " CLASS : LegoFile \n"
         retstr += "   Name     : %s \n" % (self.Name)
         retstr += "   isPart   : %s \n" % (self.isPart)
         return retstr

#=[CLASS] LegoModel =======================================================
#

class LegoModel:
    ''' Cria decritor de Objectos Lego'''
    def __init__(self,nome):
        self.nome=nome
        self.setLocation = vector(0,0,0)
        self.escala = Scale
        self.file = ""
        self.corrTransf=Transf()
        self.corrTransf.matriz=[[ self.escala, 0, 0, 0],
                                [ 0, -self.escala,0, 0],
                                [ 0, 0, -self.escala, 0, 0],
                                [ 0, 0, 0, 1]]
        self.aObj= LegoObject('Model',nome)
        
        
    def Import(self,NomeFicheiro):
        ''' Importa modelo decrito num ficeiro '''
        T = Transf()
        T.translacao(self.setLocation)
        print "-----------------Importa Modelo--------------------"
        print "--- Nome do Modelo: "+self.nome+" Ficheiro: "+ NomeFicheiro
        print "---------------------Inicio------------------------"
        self.file = NomeFicheiro
        EsteFicheiro = LegoFile(NomeFicheiro)
        self.aObj.ImportFile(EsteFicheiro,T*self.corrTransf,{})
        print "-----------------------Fim-------------------------"
        print

    def plano(self):
        return False
    
    def FaceTriang(self):
        return False

    def FaceQuad(self):
        return False

    def Mesh(self):
        return False

    def Lego(self):
        return True

#=[CLASS] LegoObject =====================================================
#
class LegoObject:
    ''' Cria Objecto Lego decrito por um ficheiro ldr ou dat '''
    
    def __init__(self, type, name=""):
        if type != 'Model' and type != 'Part':
            print "Apenas aceita objectos do tipo 'Model' ou 'Part'"
            return null
        self.Type = type
        self.Name = name
        self.cor = 16
        self.animar = False
        self.transf = Transf()
        self.links =[]              # objectos usados no Modelo
        self.Mesh = Mesh()          # associa malha a objecto
        self.Parts=[]
        self.file=""

    def ImportFile(self, lFile, transf, replace, pcolor=16, Invert=False):
        ''' Importa ficheiro com descrição de objecto Lego ou parte'''
        InvertNext = False
        CW = Invert
        for line in lFile.Lines:        #AV   aFile:
            cmdLine = line.split()
            if cmdLine == []:
               pass
            elif cmdLine[0]=='0':  # Remark
               if "BFC" in cmdLine:
                  if " CCW" in line:
                     # Do nothing as sometimes setting CW or CCW is not completely OK
                     # Patched setting 'TwoFaces' mesh
                     pass
                  if " CW" in line:
                     # Do nothing as sometimes setting CW or CCW is not completely OK
                     # Patched setting 'TwoFaces' mesh
                     pass
                  if "INVERTNEXT" in cmdLine:
                      InvertNext = True
               pass
            elif cmdLine[0]=='1':  # Ficheiro de Part
                self.AddPart(cmdLine, transf, replace, pcolor, InvertNext)
                InvertNext = False
                pass
            elif cmdLine[0]=='2':  # Linha
                pass
            elif cmdLine[0]=='3':  # Triangulo
                if self.Type == 'Part':
                    self.AddTriangle(cmdLine, transf ,pcolor, CW)
                else:
                    self.AddTriangle(cmdLine, transf ,16, CW)
            elif cmdLine[0]=='4':  # Quadrilatero
                if self.Type == 'Part':
                    self.AddQuadrilateral(cmdLine, transf, pcolor, CW)
                else:
                    self.AddQuadrilateral(cmdLine, transf, 16, CW)
            elif cmdLine[0]=='5':  # Optional-Line
                InvertNext = False
                pass
            else:
                InvertNext = False
                pass
        

    def AddPart(self, cmd, transf, replace, color=16, Invert=False ):
        ''' Adiciona parte de um objecto Lego '''
        
        if cmd[0] != '1':       # Check if line contains correct command
            return
        if len(cmd) != 15:      # Check for correct number of parameters
            return
        # Get all the command parameters
        newcolor = int(cmd[1])
        if newcolor == 16:
            newcolor = color
        self.cor = newcolor
        partName  = cmd[14].upper()
        self.file = partName
        mtxTranf = Transf()
        mtxTranf.matriz=[[float(cmd[ 5]), float(cmd[ 6]), float(cmd[7]),float(cmd[ 2])],
                        [float(cmd[ 8]), float(cmd[ 9]), float(cmd[10]),float(cmd[ 3])],
                        [float(cmd[ 11]), float(cmd[12]), float(cmd[13]),float(cmd[ 4])],
                        [0, 0, 0,1]]
        LFile = LegoFile(partName)
        if len(replace)==0:
            mtxTranf = transf * mtxTranf
        else:
            try:
                mtxTranf.matriz=replace[LFile.Name].pop()
                mtxTranf = transf * mtxTranf
            except KeyError:
                print "ERRRRROOOO..."
       
        if self.Type == 'Part':
            self.ImportFile(LFile, mtxTranf,{}, newcolor, Invert)
        elif self.Type == 'Model':
            self.Parts.append((LFile.Name,mtxTranf.matriz))
            print "Parte em:"+LFile.Name + " Transf:" + str(mtxTranf.matriz)
            if LFile.isPart:
                newObj = LegoObject('Part', LFile.Name)
                newObj.ImportFile(LFile,mtxTranf,{}, newcolor, Invert)
            else:
                newObj = LegoObject('Model', LFile.Name)
                newObj.ImportFile(LFile,mtxTranf,{},newcolor,Invert)
            newObj.tranf=mtxTranf
            self.links.append(newObj)

    def AddVertex(self, xyzList, T):
        ''' Adiciona vértices na malha '''
        P = ponto(xyzList[0],xyzList[1],xyzList[2])
        Q = P.transf(T)
        L = self.Mesh.nos.values()
        if Q in L:
            for idx in self.Mesh.nos.keys():
                if self.Mesh.nos[idx] == Q:
                    break
        else:
            idx = self.Mesh.addNo(Q)
        return idx

    def AddTriangle(self, cmd, transf, color=16, CW=False):
        ''' Adiciona face com três vértices'''
        if cmd[0] != '3':       # Check if line contains correct command
            return
        if len(cmd) != 11:      # Check for correct number of parameters
            return
        if int(cmd[1]) != 16:
            color = int(cmd[1])
        if CW :
           list = [2,1,0]
        else:
           list = [0,1,2]
        f=[]
        for x in list:
            idx = self.AddVertex([float(cmd[2+(x*3)]), float(cmd[3+(x*3)]),
                             float(cmd[4+(x*3)])], transf)
            f.append(idx)
        self.Mesh.addFace(f,color)

    def AddQuadrilateral(self, cmd, transf, color=16, CW=False):
        ''' Adiciona face com quatro vértices'''
        if cmd[0] != '4':       # Check if line contains correct command
            return
        if len(cmd) != 14:      # Check for correct number of parameters
            return
        if int(cmd[1]) != 16:
            color = int(cmd[1])
        f = []
        if CW :
           list = [3,2,1,0]
        else:
           list = [0,1,2,3]
        for x in list:
            idx = self.AddVertex([float(cmd[2+(x*3)]), float(cmd[3+(x*3)]),
                             float(cmd[4+(x*3)])], transf)
            f.append(idx)
        self.Mesh.addFace(f,color)

#---------------------------------------------------
# Fontes de luz

class FonteLuz:
    ''' Definição de fontes de luz '''
    def __init__(self):
        self.posicao = ponto(0,1700,0)
        self.corRGB = (1,1,1)
        self.apontada= ponto(0,0,1)

        
#---------------------------------------------------
#
#Cena
#

class Cena:
    ''' Descicao da cena 3D '''

    def __init__(self):
        ''' Construtor duma cena '''
        self.objectos = []                  # Objectos que definem a cena 3D
        self.vista2D= []                    # Poligonos que definem a vista 2D
        self.projeccao = Transf()           # incia matriz de projeccao
        self.projeccao.ProjOrto()           # projecta cena na plano XOY
        self.planovista = plano(ponto(0,0,0),vector(0,0,1)) # plano de vista
        self.AolharPara = self.planovista.ponto+self.planovista.vector
        self.vectorUP = vector(0,1,0)       # vector que aponta para Cima
        self.Vista = Transf()               # Definição da vista
        self.Zoom =1                        # factor de zoom
        self.max_trace_level = 5            # Increase by a small amount if transparent areas appear dark.
        

    def deAolharPara(self,ponto1,ponto2):
        ''' determina o plano de vista tendo por base dois pontos'''
        self.planovista = plano(ponto1,ponto2-ponto1)
        self.AolharPara = ponto2

    def lista(self):
        '''lista os objectos da cena'''
        cont = 0
        if not self.objectos:
            print "Lista vazia."
        else:
            print "Lista de objectos na Cena:"
            for obj in self.objectos:
                print "....",cont,"-->",obj
                cont=cont+1

    def remove(self,n):
        '''remove um objecto da cena'''
        del self.objectos[n]

    def addObj(self,object):
        ''' Adiciona um objecto a uma cena'''
    
        # Adiciona Objecto à cena
        self.objectos.append(object)


    def mostraMesh(self,obj):
        ''' Função que descreve a geometria dos objectos Lego para pyMCG'''
        listaPoly=[]
        for face in obj.faces.keys():
            lista=[]
            cor = obj.faces[face][0]
            try:
                Xcor=(hex(legocolor[cor][0])+'x'+hex(legocolor[cor][1])+'x'+hex(legocolor[cor][2])).upper().split('X')
            except KeyError:
                Xcor=["","FF","","B0","","CC"]
            sCor="#"+Xcor[1].zfill(2)+Xcor[3].zfill(2)+Xcor[5].zfill(2)
            numV=len(obj.faces[face][1])
            aux=0
            visivel = True                     # True se face está na frente do plano de vista
            for vert in obj.faces[face][1]:
                try:
                    ImNo=obj.nos[vert].proj(self.Vista)
                    lista.append(ImNo[0])
                    aux = aux + ImNo[1]
                    if ImNo[1]<0:
                        visivel = False
                except KeyError:
                    print "ERRO vértice: "+str(vert)
            if visivel:
                listaPoly.append((sCor,lista,aux/float(numV)))
        return listaPoly

    def strVertMesh(self,obj):
        ''' Formata geometria para objectos no Pov-Ray'''
        global contador
        global legocolor

        nome=obj.Name.replace('./','_').replace('/','_').replace('.','_')
        descVer = '''
#declare tmp%s_%s_=mesh2{
vertex_vectors{
%s
'''%(nome,str(contador),str(obj.Mesh.numNos))
        descFace = ""
        descUnion = '''
object{tmp%s_%s_  hollow}\n
'''%(nome,str(contador))
        descCor=[]
        contCor=0
        for i in range(obj.Mesh.numNos):
                vert=obj.Mesh.nos[i]
                descVer +=",<%s,%s,%s>\n"%(str(vert.x),str(vert.y),str(-vert.z))
        descVer += "}\n"
        contaFaces=0
        for j in obj.Mesh.faces.iterkeys():
                (cor,face)=obj.Mesh.faces[j]
                try:
                    corId = descCor.index(cor)
                except ValueError:
                    descCor.append(cor)
                    corId = descCor.index(cor)
                descFace +=",<%s,%s,%s>, %s\n"%(str(face[0]),str(face[1]),str(face[2]),str(corId))
                if len(face)==4:
                    descFace +=",<%s,%s,%s>, %s\n"%(str(face[2]),str(face[3]),str(face[0]),str(corId))
                    contaFaces += 1
                contaFaces += 1
        descFace += "}\n"
        inicdescFace = '''
face_indices{
%s
'''%(str(contaFaces))

        descText= '''texture_list{
%s\n
'''%len(descCor)
        for cor in descCor:
            try:
                if legocolor[cor][3]== 255:
                    descText+='''
texture {
 pigment { rgb <%s/255, %s/255, %s/255> }
 normal{ lg_normal }
 finish { lg_solid_finish }
}'''%(str(legocolor[cor][0]),str(legocolor[cor][1]),str(legocolor[cor][2]))
                else:
                    descText+='''
texture {
 pigment { rgb <%s/255, %s/255, %s/255>
  #if (lg_quality > 1)
   filter 0.9
  #end
 }
 normal { lg_normal }
 finish { lg_transparent_finish }
}'''%(str(legocolor[cor][0]),str(legocolor[cor][1]),str(legocolor[cor][2]))
            except:
                descText+='''
texture {
 pigment { rgb <255/255, 176/255, 204/255> }
 normal{ lg_normal }
 finish { lg_solid_finish }
}'''
        descText+='''\n}\n'''
        return (descVer+descText+inicdescFace+descFace+"\n}\n",descUnion)
        

    def vertObj(self,obj):
        ''' Função para formatar a geometria do objecto'''
        global contador
        
        Geom= ""
        descUnion= ""
        if obj.Mesh.numNos>0:
            (NGeom,NdescUnion) = self.strVertMesh(obj)
            Geom += NGeom
            descUnion += NdescUnion
        for subObj in obj.links:
            contador += 1
            (NGeom,NdescUnion) = self.vertObj(subObj)
            Geom += NGeom
            descUnion += NdescUnion
        return (Geom,descUnion)

    def render(self,index=6666):
        ''' Função que cria script para o POV-Ray duma cena '''
        global FontesLuz
        global FundoRGB
        
        f = open('POV/tmp_POV_scene_%s.pov'%(str(index)), 'w')
        sceen ='''#include "tmp_POV_geom_1%s.inc" 


#declare LDRAW_RAD_LEVEL = 5;
#declare LDRAW_MTL = 10;
#declare INDEXOFREFRACTION=1.52;
#declare LDRAW_RAD_NORMAL = off;
#declare LDRAW_RAD_MEDIA = off;

#include "rad_def.inc"
global_settings {
  assumed_gamma 1.4
  max_trace_level LDRAW_MTL
  adc_bailout 0.01/2
  radiosity {
    Rad_Settings(LDRAW_RAD_LEVEL, LDRAW_RAD_NORMAL, LDRAW_RAD_MEDIA)
  }
}

sky_sphere {
  pigment {
    %s
    }
  }

 
global_settings {
  //This setting is for alpha transparency to work properly.
  //Increase by a small amount if transparent areas appear dark.
   max_trace_level %s
 
} 

 
//CAMERA PoseRayCAMERA
camera {
        perspective
        location <%s,%s,%s>
        look_at <%s,%s,%s>
        up <%s,%s,%s>
        right x*image_width/image_height
        angle 24.49514 // horizontal FOV angle
        }
'''%(str(index),sky_sphere,str(self.max_trace_level),str(self.planovista.ponto.x),str(self.planovista.ponto.y),str(self.planovista.ponto.z),
     str(self.AolharPara.x),str(self.AolharPara.y),str(self.AolharPara.z),
     str(self.vectorUP.x),str(self.vectorUP.y),str(self.vectorUP.z))
        aux = ""
        for font in FontesLuz:
            aux +='''
//PoseRay default Light attached to the camera
light_source {
              <%s,%s,%s> //light position
              color rgb <%s,%s,%s>*1.6
              parallel
              point_at <%s,%s,%s>
             }
            '''%(str(font.posicao.x),str(font.posicao.y),str(font.posicao.z),
                    str(font.corRGB[0]),str(font.corRGB[1]),str(font.corRGB[2]),
                    str(font.apontada.x),str(font.apontada.y),str(font.apontada.z))
        sceen +=aux
        for objecto in self.objectos:
            if objecto.plano():
                sceen +='''
plane
    {
        <%s,%s,%s>, %s
        pigment { %s }
    }'''%(str(objecto.vector.x),str(objecto.vector.y),str(objecto.vector.z),
          str(objecto.vector.interno(objecto.ponto.posicao())),objecto.pigmento)
        sceen +='''

//Background
background { color rgb<%s/255,%s/255,%s/255>}
 
//Assembled object that is contained in tmp_POV_geom...
object{
      _tmp_
      }
'''%(str(FundoRGB[0]),str(FundoRGB[1]),str(FundoRGB[2]))
        f.write(sceen)
        f.close()

        f = open('POV/tmp_POV_geom_1%s.inc'%(str(index)), 'w')

        sceen ='''#include "lg_color2.inc"
 
//Geometry'''
        Geom=""
        descUnion=""

        for objecto in self.objectos:
            if objecto.Lego():
                obj=objecto.aObj
                (Geom,NdescUnion)=self.vertObj(obj)
                descUnion += NdescUnion
            
            sceen += Geom
        sceen +='''
//Model assembly from the meshes
#declare _tmp_=
union {
'''
        sceen += descUnion
        sceen +='''
}
'''
        f.write(sceen)
        f.close()
        del sceen
        #os.system('"c:\Program File\POV-Ray for Windows v3.6\bin\pvengine.exe" tmp_POV_scene.pov +W320 +H299 +FN +AM1 +A -UA "')



# ===========================================
#
#

            
def LegoObj(cena,obj):
    ''' Cria lista de poligonos que definem malha'''
    lista = cena.mostraMesh(obj.Mesh)
    for subObj in obj.links:
        lista += LegoObj(cena,subObj)
    return lista                        
    
def actualizaIG(cena,Wire=True):
    ''' Actualiza Janela Gráfica'''
    global frame
    
    # matriz de mudança de coordenadas usando um ref ortonormado
     
    w= cena.planovista.vector
    t= cena.vectorUP
    u= t.externo(w).normalizar()
    v= w.externo(u)
    O= cena.planovista.ponto
    V= Transf()
    V.vista(O,u,v,w)

    # Zoom

    Z= Transf()
    Z.escalonamento(cena.Zoom,cena.Zoom,cena.Zoom)

    # matriz de transformação de cena
    M = Transf()
    M = Z*cena.projeccao*V
    cena.Vista=M

    listaPoly=[]
    for object in cena.objectos:
        if object.FaceTriang():
            lista=[]
            aux=0
            for vert in range(2):
                ImNo=object.ponto[vert].proj(M)
                lista.append(ImNo[0])
                aux = aux + ImNo[1]
            listaPoly.append("#FFB0CC",lista,aux/3.0)
        elif object.FaceQuad():
            lista=[]
            aux=0
            for vert in range(3):
                ImNo=object.ponto[vert].proj(M)
                lista.append(ImNo[0])
                aux = aux + ImNo[1]
            listaPoly.append("#FFB0CC",lista,aux/4.0)
        elif object.Mesh():
            sx = object.escalaX
            sy = object.escalaY
            sz = object.escalaZ
            E = Transf()
            E.escalonamento(sx,sy,sz)
            T = Transf()
            T.translacao(object.ponto.posicao())
            for face in object.faces:
                lista=[]
                numV=len(object.faces[face])
                aux=0
                for vert in object.faces[face]:
                    ImNo=object.nos[vert].transf(E).transf(T).proj(M)
                    lista.append(ImNo[0])
                    aux = aux + ImNo[1]
                listaPoly.append("#FFB0CC",lista,aux/float(numV))
        elif object.Lego():
            listaPoly += LegoObj(cena,object.aObj)
    listaPoly.sort(key=itemgetter(2), reverse=False)
    clear()
    cena.vista2D.append(listaPoly)
    if Wire:
        DrawPolygonListC(listaPoly)
    else:
        DrawPolygonListB(listaPoly)


def interpola(xList,yList,idx,npontos):
    ''' Calcula a interpolação de uma lista de pontos'''
    dx = 1.0/(npontos+1)
    lista =[]
    for i in range(npontos):
        x = idx + (i+1)*dx
        y = 0.0
        for j in range(3):
            Lx=1.0
            for k in range(3):
                if k!=j:
                    Lx=Lx*(x-xList[k])/(xList[j]-xList[k])
            y = y + yList[j]*Lx
        lista.append(y)
    return lista

def objsComum(idx):
    ''' Detemina os objectos comuns em três frames seguidas'''
    NomeComum=[] 
    for objA in Frame[idx].objectos:
        if objA.Lego() and objA.animar:
            for objB in Frame[idx+1].objectos:
                if objB.Lego() and objA.animar:
                    if objA.nome == objB.nome:
                        for objC in Frame[idx+2].objectos:
                            if objC.Lego() and objA.animar:
                                if objA.nome == objC.nome:
                                    NomeComum.append((objA,objB,objC))
    return NomeComum

def estaLista(obj,ListObj):
    ''' Verifica se o objecto obj é o primeiro elemento do tuplo da lista'''
    for (obj1,obj2,obj3) in ListObj:
        if obj == obj1:
            return True
    return False

def InterpolaVista(idxFrame,numDiv):
    ''' Usa interpolação para determinar os planos de vista das novas cenas'''

    global Frame
    A=[]
    for num in range(3):
        A.append([[Frame[idxFrame+num].planovista.ponto.x,Frame[idxFrame+num].planovista.ponto.y,Frame[idxFrame+num].planovista.ponto.z],
                [Frame[idxFrame+num].planovista.vector.x,Frame[idxFrame+num].planovista.vector.y,Frame[idxFrame+num].planovista.vector.z]
                ])
    planoV=[]
    for nova in range(numDiv):
        planoV.append([[ 0, 0, 0],[ 0, 0, 0]])
    for i in [0,1]:
        for j in [0,1,2]:
            xLista = [idxFrame,idxFrame+1,idxFrame+2]
            yLista = [A[0][i][j],A[1][i][j],A[2][i][j]]
            yVal = interpola(xLista,yLista,idxFrame,numDiv)
            for nova in range(numDiv):
                planoV[nova][i][j]=yVal[nova]
    return planoV


def DivideFrames(num):
    ''' Cria frames entre os frames existentes na lista Frame'''
    global Frame

    numFrames=len(Frame)
    if numFrames<3:
        print "Numero demasiado pequeno de Frames!"
        return
    Frame.append(Frame[numFrames-1])    # Cria duas cenas fantasma
    Frame.append(Frame[numFrames-1])
    NovoFrame=[]                        # Lista de novas cenas
    for idxFrame in range(numFrames):
        listaComumObj = objsComum(idxFrame)
        transfor ={}  # dicionário de chave frameidx,nome_objecto de transfs
        NovaCena=[]
        NovasVistas=InterpolaVista(idxFrame,num) # Cria vector e ponto dos novos planos de vista
        for nova in range(num):
            cena=Cena()
            cena.Zoom= copy.deepcopy(Frame[idxFrame].Zoom)
            cena.projeccao = copy.deepcopy(Frame[idxFrame].projeccao )
            pontoV =ponto(NovasVistas[nova][0][0],NovasVistas[nova][0][1],NovasVistas[nova][0][2])
            vectorV =vector(NovasVistas[nova][1][0],NovasVistas[nova][1][1],NovasVistas[nova][1][2])
            cena.planovista = plano(pontoV,vectorV) 
            cena.AolharPara = pontoV+vectorV
            cena.vectorUP = copy.deepcopy(Frame[idxFrame].vectorUP)
            #cena.Vista 
            cena.max_trace_level = copy.deepcopy(Frame[idxFrame].max_trace_level) 
            for obj in Frame[idxFrame].objectos:
                if obj.plano():
                    cena.objectos.append(obj)
                elif not estaLista(obj,listaComumObj): 
                    cena.objectos.append(obj)
            NovaCena.append(cena)
        NovoFrame.append(Frame[idxFrame])             
        for objList in listaComumObj:
            A={}   #dicionário da matrizes de transformação dum obj numa key frame
            for objIdx in range(len(objList)):# inicia matriz Ai para a interpolação
                obj = objList[objIdx]
                A[idxFrame+objIdx]={}
                cont=0
                for partIdx in range(len(obj.aObj.Parts)):
                    Part = obj.aObj.Parts[partIdx]
                    nome = Part[0]                      # Nome da parte
                    A[idxFrame+objIdx][(nome,cont)]=Part[1]    # Matriz
                    cont=cont+1
            for nome in A[idxFrame].keys():
                transfor[nome]={}
                for nova in range(num):
                    transfor[nome][nova]=[[ 1, 0, 0, 0],[ 0, 1, 0, 0],[ 0, 0, 1, 0],[ 0, 0, 0, 1]]
                for i in range(3):
                    for j in range(4):
                        xLista = [idxFrame,idxFrame+1,idxFrame+2]
                        yLista = [A[idxFrame][nome][i][j],A[idxFrame+1][nome][i][j],A[idxFrame+2][nome][i][j]]
                        yVal = interpola(xLista,yLista,idxFrame,num)
                        for nova in range(num):
                            transfor[nome][nova][i][j]=yVal[nova]
            for nova in range(num):
                obj=objList[0]
                novoObj=LegoModel(obj.nome)
                novoObj.escala=obj.escala
                novoObj.file=obj.file
                print "----------- Inicio de Novo objecto em Novo Frame -------"
                EsteFicheiro = LegoFile(obj.file)
                transfNova={}
                for (nome,n) in A[idxFrame].keys():
                    try:
                        transfNova[nome].append(transfor[(nome,n)][nova])
                    except KeyError:
                        transfNova[nome]=[transfor[(nome,n)][nova]]
                transf=Transf()
                novoObj.aObj.ImportFile(EsteFicheiro,transf,transfNova)
                print "------------------- Fim ----------"
                NovaCena[nova].addObj(novoObj)
                del novoObj
        for nova in range(num):
            NovoFrame.append(NovaCena[nova])
    Frame=NovoFrame
            
        


#=========================================================================
#
# Carrega as linhas dos ficheiros de descrição de modelos 
#
def LegoFile(filename, searchPath = ""):
    global LegoFiles
    if filename in LegoFiles:
        return LegoFiles[filename]
    aFile = CLFile(filename, searchPath)
    # Caso este seja o ficheiro importado verifica um ficheiro MPD (Multipart File)
    if len(LegoFiles)==0:
       retList = SplitMPD(aFile)
       aFile.Name = retList[0][0]
       aFile.Lines = retList[0][1]
       del retList[0]
       for f in retList:
           bFile = CLFile()
           bFile.Name = f[0]
           bFile.Lines = f[1]
           LegoFiles[bFile.Name] = bFile
    LegoFiles[aFile.Name] = aFile
    return aFile


def SplitMPD(aFile):
    retList=[]
    isMPD = 0
    Start = 0
    Name = aFile.Name.upper()
    for line in aFile.Lines :
        cmdLine = line.split()
        if cmdLine == []:
           pass
        elif cmdLine[0]=='0' and len(cmdLine)>2 and cmdLine[1]=='FILE' : #
           if isMPD == 0 :
               Name  = cmdLine[2]
               Start = aFile.Lines.index(line)
               isMPD = 1
           else :
               Stop = aFile.Lines.index(line)
               retList.append([Name.upper(), aFile.Lines[Start:Stop]])
               Name = cmdLine[2]
               Start = Stop
        elif cmdLine[0]=='0' and len(cmdLine)>1 and cmdLine[1]=='NOFILE' :
           Stop = aFile.Lines.index(line)
           retList.append([Name.upper(), aFile.Lines[Start:Stop]])
           return retList
    retList.append([Name.upper(), aFile.Lines[Start:]])
    return retList

#=========================================================================
#
# Rendering de uma sequência de frames
#
def render(ini=0, fim=-1):
    ''' Faz o rendering do frame de ordem ini até ao frame de ordem fim'''
    global Frame

    if fim==-1 or fim > len(Frame)-1:
        fim=len(Frame)-1
    for idx in range(ini,fim):
        Frame[idx].render(idx)
        
    
#=========================================================================
# MAIN
#

#
# Inicia Frames
#

LegoFiles={}    # dict com os ficheiros nos objectos
cena = Cena()   # inicializa primeira cena 
Frame=[cena]    # Define lista de frames como tendo apenas uma cena
luz=FonteLuz()  # Cria fonte de luz por defeito
FontesLuz=[luz] # Define a lista de fontes de luz
FundoRGB = (0,128,255) #Define uma cor para o fundo no POV-Ray
sky_sphere='''
rgb <0/255,0/255, 1/255>
'''             # Pigmento para céu
clear()         #limpa janela do pyMCG
