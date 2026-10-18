import WConio2 as WConio2
# import random
import time
import os
import movimentos

from mapa import pastilhas
from mapa import labirinto

def mostrarVidas(vidas, pontos):
    while vidas >= 0:
        if vidas > 0:
            print('C', end = ' ')
        vidas -= 1    
    print('pontos:', pontos)
        
os.system("cls")
labirinto = []
tictac = 0
vidas = 1
vidaAtual = False
loop = 0
pontos = 0
poder = False
temporizador = 0

#personagens
pacman = 'C'
blink = 'B'
pink = 'P'
inky = 'I'
opcao = ' '
# esta criando o labirinto
for i in range(31):
    labirinto.append([])
    for j in range(28):
        labirinto[i].append(0)
                
# prepararLabiritnto(labirinto)
# labirinto((labirinto))

pastilhas.colocartictac(tictac, labirinto)

vidas = 3

while tictac > 0 and vidas >= 0:
    if vidas >= 0 and  vidaAtual == False:
        poder = False
        temporizador = 0
        vidaAtual = True
        vidas -= 1
        
        pacmanX = 13
        pacmanY = 23

        blinkX = 13
        blinkY = 11
        
        passadoBlinkX = blinkX
        passadoBlinkY = blinkY
        blinkAtual = ' '
        blinkVivo = True
        
        pinkX = 12
        pinkY = 14
        
        passadoPinkX = pinkX
        passadoPinkY = pinkY
        pinkAtual = ' '
        pinkVivo = True
        
        inkyX = 14
        inkyY = 14

        passadoinkyX = inkyX
        passadoinkyY = inkyY
        inkyAtual = ' '
        inkyVivo = True
        
        labirinto[pacmanY][pacmanX] = pacman
        labirinto[blinkY][blinkX] = blink
        labirinto[pinkY][pinkX] = pink
        labirinto[inkyY][inkyX] = inky
        labirinto.mostrarLabirinto(labirinto)
        mostrarVidas(vidas, pontos)
        
        time.sleep(5)        
        loop = 0
    
    else:
        if temporizador == 50:
            poder = False
            temporizador = 0
            blink = 'B'
            pink = 'P'
            inky = 'I'
            blinkVivo = True
            pinkVivo = True
            inkyVivo = True
 
        labirinto.mostrarLabirinto(labirinto)
        mostrarVidas(vidas, pontos)
        
        time.sleep(0.2)
        if(WConio2.kbhit()):  #verifica se uma tecla foi apertada
            codigo, opcao = WConio2.getch()  #captura a tecla apertada

        print(opcao) 
        
        pacmanY, pacmanX, tictac, pontos, poder= movimentos.moviPacman(opcao, pacmanY, pacmanX, pacman, tictac, labirinto, pontos, poder)

    # relização dos movimentos
        blinkY, blinkX, passadoBlinkY, passadoBlinkX, blinkAtual  = movimentos.blink(passadoBlinkX, passadoBlinkY, blinkX, blinkY, pacmanX, pacmanY, labirinto, poder, blinkAtual)
    
        if loop >= 10:
            if loop == 10:
                labirinto[pinkY][pinkX] = ' '
                pinkY = 11
                pinkX = 13
            pinkY, pinkX, passadoPinkY, passadoPinkX, pinkAtual = movimentos.pink(pinkX, pinkY, pacmanX, pacmanY, labirinto, passadoPinkX, passadoPinkY, opcao, pinkAtual, poder)
    
        if loop >= 15:    
            if loop == 15:
                labirinto[inkyY][inkyX] = ' '
                inkyY = 11
                inkyX = 13
            inkyY, inkyX, passadoinkyY, passadoinkyX, inkyAtual = movimentos.inky(inkyX, inkyY, blinkX, blinkY, pacmanX, pacmanY, labirinto, passadoinkyX, passadoinkyY,inkyAtual)

        labirinto[pacmanY][pacmanX] = pacman
        labirinto[blinkY][blinkX] = blink 
        labirinto[pinkY][pinkX] = pink
        labirinto[inkyY][inkyX] = inky
        
        if poder == False:
            if (blinkX == pacmanX and blinkY == pacmanY) and blinkVivo == True:
                vidaAtual = False
                
            elif(pinkX == pacmanX and pinkY == pacmanY) and pinkVivo == True:
                vidaAtual = False
            
            elif(inkyX == pacmanX and inkyY == pacmanY) and inkyVivo == True:
                vidaAtual = False
        
        if poder == True:
            if blinkX == pacmanX and blinkY == pacmanY:
                blinkVivo = False
                blink = ':' 
            
            if pinkX == pacmanX and pinkY == pacmanY:
                pinkVivo = False
                pink = ':' 
            
            elif inkyX == pacmanX and inkyY == pacmanY:
                inkyVivo = False
                inky = ':' 
            
        if poder == True:
            temporizador += 1
            blink = '4'
            pink = '4'
            inky = '4'
        loop += 1
        print(temporizador)
print("Game-Over")