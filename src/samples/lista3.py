# -*- coding: cp1252 -*-

#--------------------
# IMPORTA
#

### Homem
homem=LegoModel('Homem')
homem.setLocation = vector(-80,0,0) ## Atenção à ordem
homem.Import('MLcad/Homem.ldr')


### Carro
carro=LegoModel('Carro')
carro.Import('MLcad/policecar.ldr')

### Árvore
arvore =LegoModel('Arvore')
arvore.setLocation = vector(-10,0,-50)
arvore.Import('MLcad/tree.ldr')



#---------------
#  
#
FundoRGB = (0,128,255)

#---------------
# Fontes de Luz
#
# FontesLuz[0] fonte por defeito

FontesLuz[0].posicao = ponto(0,1700,0)
FontesLuz[0].corRGB = (1,1,1)
FontesLuz[0].apontada= ponto(0,0,0)

### mais uma fonte de luz

#fonteluz2=FonteLuz()
#fonteluz2.posicao = ponto(100,100,100)
#fonteluz2.corRGB = (255,201,196) #  12  Light Red LDraw
#fonteluz2.apontada= ponto(0,0,0)
#FontesLuz.append(fonteluz2)


#---------------
# Frame 0
#
Frame[0].deAolharPara(ponto(700,0,-1500),ponto(0,0,0))
Frame[0].vectorUP = vector(0,1,0)
Frame[0].Zoom = .5
Frame[0].max_trace_level = 7

### Projecção

#T=Transf()
#T.ProjCabinet()
#Frame[0].projeccao=T

### junta homem na cena
Frame[0].addObj(homem)

### junta carro na cena
Frame[0].addObj(carro)

### junta árvore na cena
Frame[0].addObj(arvore)

actualizaIG(Frame[0],False)





