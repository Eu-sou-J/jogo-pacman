import WConio2 as WConio2
import time
import os

#constroi o labirinto
def prepararLabiritnto(labirinto):
    
# borda labirinto
    for i in range(9):
        labirinto[i][0] = '#'
        labirinto[i][27] = '#'
    for i in range(30, 31):
        for j in range(27, 28):
            labirinto[i][j] = '#'
        
    for i in range(28):
            labirinto[0][i] = '#'
            
    for i in range(19, 31):
        for j in range(1):
            labirinto[i][j] = '#'
                        
# canto superior esquerdo
    for i in range(2, 5, 1):
        for j in range(2, 6, 1):
            labirinto[i][j] = '#'
            
# canto superior esquerdo
    for i in range(6, 8):
        for j in range(2, 6):
            labirinto[i][j] = '#'
            
# canto superior esquerdo
    for i in range(2, 5, 1):
        for j in range(7, 12, 1):
            labirinto[i][j] = '#'

#inferior esquerdo

    for i in range(21, 23):
        for j in range(7, 12):
            labirinto[i][j] = '#'
    
    for i in range(21, 23):
        for j in range(2, 6):
            labirinto[i][j] = '#'
            
    for i in range(23, 26):
        for j in range(4, 6):
            labirinto[i][j] = '#'
    
    for i in range(24, 26):
        for j in range(0, 3):
            labirinto[i][j] = '#'
            
    for i in range(24, 29):
        for j in range(7, 9):
            labirinto[i][j] = '#'
    for i in range(27, 29):
        for j in range(2, 12):
            labirinto[i][j] = '#'
             
    for i in range(26, 29):
        for j in range(13, 15):
            labirinto[i][j] = '#'
            
    for i in range(24, 26):
        for j in range(10, 18):
            labirinto[i][j] = '#'
    
       

#direito central
    for i in range(9, 14):
        for j in range(22, 28):
            labirinto[i][j] = '#'

                 
#esquerdo central
    for i in range(9, 14):
        for j in range(0, 6):
            labirinto[i][j] = '#'
            
    for i in range(15, 20):
        for j in range(0, 6):
            labirinto[i][j] = '#'
            
    for i in range(15, 20):
        for j in range(7, 9):
            labirinto[i][j] = '#'
            
    for i in range(6, 14):
        for j in range(7, 9):
            labirinto[i][j] = '#'
            
    for i in range(9, 11):
        for j in range(9, 12):
            labirinto[i][j] = '#'
                       
#direito central
    for i in range(15, 20):
        for  j in range(22, 28):
            labirinto[i][j] = '#'
            
    for i in range(15, 20):
        for j in range(19, 21):
            labirinto[i][j] = '#'
            
            
# superior central
    for i in range(5):
        labirinto[i][13] = '#'
        labirinto[i][14] = '#'

# superior central
    for i in range(6, 8):
        for j in range(10,18):
            labirinto[i][j] = '#'
            
    for i in range(7, 11):
        labirinto[i][13] = '#'
        labirinto[i][14] = '#'
        
# inferior central
    for i in range(18,20):
        for j in range(10, 18):
            labirinto[i][j]= '#'
            
    for i in range(20, 23):
        for j in range(13, 15):
            labirinto[i][j] = '#'
        
        
# canto superior direito
    for i in range(2, 5):
        for j in range(16, 21):
            labirinto[i][j] = '#'
            
# canto superior direito
    for i in range(2, 5):
        for j in range(22, 26):
            labirinto[i][j] = '#'

# canto superior direito
    for i in range(6,8):
        for j in range(22, 26):
            labirinto[i][j] = '#'
            
 # canto superior direito           
    for i in range (6, 14):    
        for j in range(19, 21):
            labirinto[i][j] = '#'
    for i in range(9, 11):
        for j in range(16,20):
            labirinto[i][j] = '#' 

# inferior direito
    for i in (21, 22):
        for j in range(16, 21):
            labirinto[i][j] = '#'

    for i in range(21, 23):
        for j in range(22, 26):
            labirinto[i][j] = '#'
    
    for i in range(23, 26):
        for j in range(22, 24):
            labirinto[i][j] = '#'
    
    for i in range(24, 26):
        for j in range(25, 28):
            labirinto[i][j]= '#' 

    for i in range(24, 29):
        for j in range(19, 21):
            labirinto[i][j] = '#'
            
    for i in range(27, 29):
        for j in range(16, 26):
            labirinto[i][j] = '#'

# adiciona fundo
    for i in range(30):
        for j in range(28):
            if labirinto[i][j] == 0:
                labirinto[i][j] = '*'
                
#caixa dos fantasmas     
    for i in range(12,17):
        for j in range(10,18):
            labirinto[i][j] = '#'
            
    for i in range(13,16):
        for j in range(11,17):
            labirinto[i][j] = '*'
            
    labirinto[12][13] = '_'
    labirinto[12][14] = '_'
    
    for i in range(30, 31):
        for j in range(28):
            labirinto[i][j] = '#'
    
    for i in range(20, 31):
        for j in range(27, 28):
            labirinto[i][j] = '#'
            
def mostrarLabirinto(labirinto):
    for i in range(31):
        for j in range(28):
            print(labirinto[i][j], end = ' ')
        print()
        
def colocarPastilhas(pastilhas, labirinto):
    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
# evita que que onde não deve ter pastilha não recceba pastilha 
            if(i >= 9 and i <= 19 and j >= 7 and j <= 20) and labirinto[i][j] != '#':
                if labirinto[i][j] == '*':
                    labirinto[i][j] = '*'
                elif labirinto[i][j] == '_':
                    labirinto[i][j] = '_'
# coloca pastilha

            elif labirinto[i][j] == '*' and labirinto[i][j] != '#':
                labirinto[i][j] = 'o'
                pastilhas += 1 
                
    return pastilhas
   
def movientacao(opcao, pacmanY, pacmanX, pacman, pastilhas, labirinto):
    # A movimentacao que pacman fez de acordo com o usuario
    if opcao == 'w' or opcao == 'W':
        if labirinto[pacmanY - 1][pacmanX] == '#':
               labirinto[pacmanY][pacmanX] = pacman
        else:
            if labirinto[pacmanY - 1][pacmanX] == 'o':
                print("\a")
                labirinto[pacmanY][pacmanX] = '*'
                pacmanY -= 1
                pastilhas -= 1
                labirinto[pacmanY][pacmanX] = pacman
            else: 
                labirinto[pacmanY][pacmanX] = '*'
                pacmanY -= 1
                labirinto[pacmanY][pacmanX] = pacman
               
    elif opcao == 'd' or opcao == 'D':
        if labirinto[pacmanY][pacmanX + 1] == '#':
            labirinto[pacmanY][pacmanX] = pacman
        else:
            if labirinto[pacmanY][pacmanX + 1] == 'o':
                print("\a")
                labirinto[pacmanY][pacmanX] = '*'
                pacmanX += 1
                pastilhas -= 1
                labirinto[pacmanY][pacmanX] = pacman
            else:
                labirinto[pacmanY][pacmanX] = '*'
                pacmanX += 1
                labirinto[pacmanY][pacmanX] = pacman
    
    elif opcao == 'a' or opcao == 'A':
        if labirinto[pacmanY][pacmanX - 1] == '#':
            labirinto[pacmanY][pacmanX] = pacman
        else:
            if labirinto[pacmanY][pacmanX - 1] == 'o':
                print("\a")
                labirinto[pacmanY][pacmanX] = '*'
                pacmanX -= 1
                pastilhas -= 1
                labirinto[pacmanY][pacmanX] = pacman
            else:   
                labirinto[pacmanY][pacmanX] = '*'
                pacmanX -= 1
                labirinto[pacmanY][pacmanX] = pacman
    
    elif opcao == 's' or opcao == 'S':
        if labirinto[pacmanY + 1][pacmanX] == '#':
           labirinto[pacmanY][pacmanX] = pacman
        else:
            if labirinto[pacmanY + 1][pacmanX] == 'o':
                print("\a")
                labirinto[pacmanY][pacmanX] = '*'
                pacmanY += 1
                labirinto[pacmanY][pacmanX] = pacman
                pastilhas -=  1
            else:
                labirinto[pacmanY][pacmanX] = '*'
                pacmanY += 1
                labirinto[pacmanY][pacmanX] = pacman
                
    return pacmanY, pacmanX, pastilhas
    
def movimentoBlink(blinkX, blinkY, pacmanX, pacmanY, labirinto):
    caminho = [0, 0, 0, 0]
    indiciCaminho = 0
    diferenca = 0
    menor = 1000
    vivo = True
    
    #faz o caucluo dos possiveis caminhos do blink
    for i in range(4):
        diferenca = 1000
        if i == 0 and labirinto[blinkY][blinkX - 1] != '#':
            deltaX = (blinkX - 1) - pacmanX
            deltaY = blinkY - pacmanY
            
            if deltaY <= 0 and deltaX <= 0:
                diferenca = (deltaX * -1) + (deltaY * -1) 
                
            elif deltaY <= 0:
                diferenca = deltaX + (deltaY * -1)
                
            elif deltaX <= 0:
                diferenca = (deltaX * -1) + deltaY
            else:
                diferenca = deltaX + deltaY
                            
        if i == 1 and labirinto[blinkY][blinkX + 1] != '#':
            deltaX = (blinkX + 1) - pacmanX
            deltaY = blinkY - pacmanY
            
            if deltaY <= 0 and deltaX <= 0:
                diferenca = (deltaX * -1) + (deltaY * -1)
                
            elif deltaY <= 0:
                diferenca = deltaX + (deltaY * -1)
                
            elif deltaX <= 0:
                diferenca = (deltaX * -1) + deltaY
                
            else:
                diferenca = deltaX + deltaY   
                            
        if i == 2 and labirinto[blinkY - 1][blinkX] != '#':
            deltaX = blinkX - pacmanX
            deltaY = (blinkY - 1) - pacmanY
            
            if deltaY <= 0 and deltaX <= 0:
                diferenca = (deltaX * -1) + (deltaY * -1)
                
            elif deltaY <= 0:
                diferenca = deltaX + (deltaY * -1)
                
            elif deltaX <= 0:
                diferenca = (deltaX * -1) + deltaY
            else:
                diferenca = deltaX + deltaY
            
        if i == 3 and labirinto[blinkY + 1][blinkX] != '#':
            deltaX = blinkX - pacmanX
            deltaY = (blinkY + 1)  - pacmanY
            
            if deltaY <= 0 and deltaX <= 0:
                diferenca = (deltaX * -1) + (deltaY * -1)
                
            elif deltaY <= 0:
                diferenca = deltaX + (deltaY * -1)
                
            elif deltaX <= 0:
                diferenca = (deltaX * -1) + deltaY    
                
            else:
                diferenca = deltaX + deltaY

        caminho[i] = diferenca
            
    for i in range(4):
        if caminho[i] < menor:
            menor = caminho[i]
            indiciCaminho = i
            
    # reliaza a escolha do caminho mais curto
    if vidaAtual == True:
        if indiciCaminho == 0:          
            if labirinto[blinkY][blinkX - 1] == '*' and ((blinkY != 17 or blinkY != 21) and ((blinkX - 1) != 10 or (blinkX - 1) != 17)): 
                labirinto[blinkY][blinkX] = '*'
                blinkX -= 1
            
            elif labirinto[blinkY][blinkX - 1] == 'o' and ((blinkY != 17 or blinkY != 21) and ((blinkX - 1) != 10 or (blinkX - 1) != 17)):
                labirinto[blinkY][blinkX] = 'o'
                blinkX -= 1
                
            elif labirinto[blinkY][blinkX - 1] == 'C' and ((blinkY != 17 or blinkY != 21) and ((blinkX - 1) != 10 or (blinkX - 1) != 17)):

                if labirinto[blinkY][blinkX] == 'o':
                    labirinto[blinkY][blinkX] == 'o'
                
                elif labirinto[blinkY][blinkX] == '*': 
                    labirinto[blinkY][blinkX] == '*'  
                                 
                blinkX -= 1
                
        elif indiciCaminho == 1:
            if labirinto[blinkY][blinkX + 1] == '*' and ((blinkY != 17 or blinkY != 21) and ((blinkX + 1) != 10 or (blinkX + 1) != 17)):
                labirinto[blinkY][blinkX] = '*'
                blinkX += 1
                    
            elif labirinto[blinkY][blinkX + 1] == 'o' and ((blinkY != 17 or blinkY != 21) and ((blinkX + 1) != 10 or (blinkX + 1) != 17)):
                labirinto[blinkY][blinkX] = 'o'
                blinkX += 1
                       
            elif labirinto[blinkY][blinkX + 1] == 'o' and ((blinkY != 17 or blinkY != 21) and ((blinkX + 1) != 10 or (blinkX + 1) != 17)):                    
                if labirinto[blinkY][blinkX] == 'o':
                    labirinto[blinkY][blinkX] == 'o'
                
                elif labirinto[blinkY][blinkX] == '*': 
                    labirinto[blinkY][blinkX] == '*'                
                
                blinkX += 1
        
        elif indiciCaminho == 2:
        
            if labirinto[blinkY - 1][blinkX] == '*' and (((blinkY - 1) != 17 or (blinkY - 1 ) != 21) and (blinkX  != 10 or blinkX != 17)):
                labirinto[blinkY][blinkX] = '*'
                blinkY -= 1
            
            elif labirinto[blinkY - 1][blinkX] == 'o' and (((blinkY - 1) != 17 or (blinkY - 1 ) != 21) and (blinkX  != 10 or blinkX != 17)):    
                labirinto[blinkY][blinkX] = 'o'
                blinkY -= 1
                
            elif labirinto[blinkY - 1][blinkX] == 'C' and (((blinkY - 1) != 17 or (blinkY - 1 ) != 21) and (blinkX  != 10 or blinkX != 17)):
                if labirinto[blinkY][blinkX] == 'o':
                    labirinto[blinkY][blinkX] == 'o'
                
                elif labirinto[blinkY][blinkX] == '*': 
                    labirinto[blinkY][blinkX] == '*'            
                    
                blinkY -= 1
        elif indiciCaminho == 3:
        
            if labirinto[blinkY + 1][blinkX] == '*' and (((blinkY + 1) != 17 or (blinkY + 1 ) != 21) and (blinkX  != 10 or blinkX != 17)):                   
                labirinto[blinkY][blinkX] = '*'
                blinkY += 1
            
            elif labirinto[blinkY + 1][blinkX] == 'o' and (((blinkY + 1) != 17 or (blinkY + 1 ) != 21) and (blinkX  != 10 or blinkX != 17)):
                labirinto[blinkY][blinkX] = 'o'
                blinkY += 1
            
            elif labirinto[blinkY + 1][blinkX] == 'C' and (((blinkY + 1) != 17 or (blinkY + 1 ) != 21) and (blinkX  != 10 or blinkX != 17)):
                if labirinto[blinkY][blinkX] == 'o':
                    labirinto[blinkY][blinkX] == 'o'
                
                elif labirinto[blinkY][blinkX] == '*': 
                    labirinto[blinkY][blinkX] == '*'
                
                blinkY += 1
                         
    return blinkY, blinkX  
    
def movimentoPink(pinkX, pinkY, pacmanX, pacmanY, labirinto, vidaAtual):
    caminho = [0, 0, 0, 0]
    menor = 1000
    indiceCaminho = 0
    vivo = True
    for i in range(4):
            #faz o caucluo dos possiveis caminhos do pink
        diferenca = 1000
        if i == 0 and labirinto[pinkY - 1][pinkX] != '#':
            deltaX =  pinkX - pacmanX
            deltaY = (pinkY - 1) - (pacmanY - 5)
            if deltaY < 0 and deltaX < 0:
                diferenca = (deltaY * -1) + (deltaX * -1)
                
            elif deltaY < 0:
                diferenca = (deltaY * -1) + deltaX
            
            elif deltaX < 0:
                diferenca = deltaY + (deltaX * -1)  
                
            else:  
                diferenca = deltaY + deltaX
                        
        if i == 1 and labirinto[pinkY + 1][pinkX] != '#':
            deltaX =  pinkX - pacmanX
            deltaY = (pinkY + 1) - (pacmanY + 5 )
            if deltaY < 0 and deltaX < 0:
                diferenca = (deltaY * -1) + (deltaX * -1)
            
            elif deltaY < 0:
                diferenca = (deltaY * -1) + deltaX
                
            elif deltaX < 0:
                diferenca = deltaY + (deltaX * -1)  
                
            else:  
                diferenca = deltaY + deltaX
                        
        if i == 2 and labirinto[pinkY][pinkX - 1] != '#':
            deltaX = (pinkX - 1) - (pacmanX - 5)
            deltaY = pinkY - pacmanY
            if deltaY < 0 and deltaX < 0:
                diferenca = (deltaY * -1) + (deltaX * -1)
            
            elif deltaY < 0:
                diferenca = (deltaY * -1) + deltaX
                
            elif deltaX < 0:
                diferenca = deltaY + (deltaX * -1)  
                
            else:  
                diferenca = deltaY + deltaX
                            
        if i == 3 and labirinto[pinkY][pinkX + 1] != '#':
            deltaX = (pinkX + 1) - (pacmanX + 5)
            deltaY = pinkY - pacmanY
            if deltaY < 0 and deltaX < 0:
                diferenca = (deltaY * -1) + (deltaX * -1)
                
            elif deltaY < 0:
                diferenca = (deltaY * -1) + deltaX
            
            elif deltaX < 0:
                diferenca = deltaY + (deltaX * -1)  
            
            else:  
                diferenca = deltaY + deltaX
                
        caminho[i] = diferenca
    
    for i in range(4):
        if caminho[i] < menor:
            menor = caminho[i]
            indiceCaminho = i
# reliaza a escolha do caminho mais curto
    if vivo ==  True:
        if vidaAtual == True:
            if indiceCaminho == 0:
                if labirinto[pinkY - 1][pinkX] == '*' and ((pinkY - 1) != 17  and (pinkY - 1) != 21) and (pinkX != 10 and pinkX != 17):
                    if labirinto[pinkY][pinkX] == 'C':
                        labirinto[pinkY][pinkX] = 'A'
                        vidaAtual = False
                    else:
                        labirinto[pinkY][pinkX] = '*'
                        pinkY -= 1
                        
                elif labirinto[pinkY - 1][pinkX] == 'o' and ((pinkY - 1) != 17 and (pinkY - 1) != 21) and (pinkX != 10 and pinkX != 17):
                    if labirinto[pinkY][pinkX] == 'C':
                        labirinto[pinkY][pinkX] = 'A'
                        vidaAtual = False
                    else:
                        labirinto[pinkY][pinkX] = 'o'
                        pinkY -= 1
    
            if indiceCaminho == 1:
                if labirinto[pinkY + 1][pinkX] == '*' and ((pinkY + 1) != 17 and (pinkY + 1) != 21) and (pinkX != 10 and pinkX != 17):
                    if labirinto[pinkY][pinkX] == 'C':
                        labirinto[pinkY][pinkX] = 'A'
                        vidaAtual = False                    
                    
                    else: 
                        labirinto[pinkY][pinkX] = '*'
                        pinkY += 1
            
                elif labirinto[pinkY + 1][pinkX] == 'o' and ((pinkY + 1) != 17 and (pinkY + 1) != 21) and (pinkX != 10 and pinkX != 17):
                    if labirinto[pinkY][pinkX] == 'C':
                        labirinto[pinkY][pinkX] = 'A'
                        vidaAtual = False                    
                    else:
                        labirinto[pinkY][pinkX] = 'o'
                        pinkY += 1
            
            if indiceCaminho == 2:
            
                if labirinto[pinkY][pinkX - 1] == '*' and (pinkY != 17 and pinkY != 21) and ((pinkX - 1) != 10 and (pinkX - 1) != 17):
                    if labirinto[pinkY][pinkX] == 'C':
                        labirinto[pinkY][pinkX] = 'A'
                        vidaAtual = False                    
                    
                    else:
                        labirinto[pinkY][pinkX] = '*'
                        pinkX -= 1
            
                elif labirinto[pinkY][pinkX - 1] == 'o' and (pinkY != 17 and pinkY != 21) and ((pinkX - 1) != 10 and (pinkX - 1) != 17):
                    if labirinto[pinkY][pinkX] == 'C':
                        labirinto[pinkY][pinkX] = 'A'
                        vidaAtual = False                    
                    else:
                        labirinto[pinkY][pinkX] = 'o'
                        pinkX -= 1
        
            if indiceCaminho == 3:
                if labirinto[pinkY][pinkX + 1] == '*' and (pinkY != 17 and pinkY != 21) and ((pinkX + 1) != 10 and (pinkX + 1) != 17):
                    if labirinto[pinkY][pinkX] == 'C':
                        labirinto[pinkY][pinkX] = 'A'
                        vidaAtual = False
                    
                    else:
                        labirinto[pinkY][pinkX] = '*'
                        pinkX += 1
            
                elif labirinto[pinkY][pinkX + 1] == 'o' and (pinkY != 17 and pinkY != 21) and ((pinkX + 1) != 10 and (pinkX + 1) != 17):
                    if labirinto[pinkY][pinkX] == 'C':
                        labirinto[pinkY][pinkX] = 'A'
                        vidaAtual = False                    
                    else:
                        labirinto[pinkY][pinkX] = 'o'
                        pinkX += 1
                        
    return pinkY, pinkX, vidaAtual
            
def movimentoInky(inkyX, inkyY, blinkX, blinkY, pacmanX, pacmanY, labirinto):
    caminho = [0, 0, 0, 0]
    menor = 1000
    indicieCaminho = 0
    #faz o caucluo dos possiveis caminhos do inky
    for i in range(4):
        if i == 0 and labirinto[inkyY - 1][inkyX] != '#':# para cima 
            deltaX = blinkX - pacmanX
            deltaY = blinkY - (pacmanY - 2)
            
            if deltaY < 0 and deltaX < 0:
                diferenca = (deltaY * -1) + (deltaX * -1)
            
            elif deltaY < 0:
                diferenca = (deltaY * -1) + deltaX
            
            elif deltaX < 0: 
                diferenca = deltaY + (deltaX * -1)
            
            else: 
                diferenca = deltaY + deltaX
            
            diferenca *= 2   
            caminho[i] = diferenca
        
        elif i == 1 and labirinto[inkyY + 1][inkyX] != '#':#para baixo
            deltaX = blinkX - pacmanX
            deltaY = blinkY - (pacmanY + 2)
            
            if deltaY < 0 and deltaX < 0:
                diferenca = (deltaY * -1) + (deltaX * -1)
            
            elif deltaY < 0:
                diferenca = (deltaY * -1) + deltaX
            
            elif deltaX < 0:
                diferenca = deltaY + (deltaX * -1)
            
            else:
                diferenca = deltaY + deltaX
            
            diferenca *= 2
            caminho[i] = diferenca
        
        elif i == 2 and labirinto[inkyY][inkyX - 1] != '#': #esquerda
            deltaX = blinkX - (pacmanX - 2)
            deltaY = blinkY - pacmanY
            
            if deltaY < 0 and deltaX < 0:
                diferenca = (deltaY * -1) + (deltaX * -1)
                        
            elif deltaY < 0:
                diferenca = (deltaY * -1) + deltaX
                        
            elif deltaX < 0:
               diferenca = deltaY + (deltaX * -1)
                        
            else:
                diferenca = deltaY + deltaX
                        
            diferenca *= 2
            caminho[i] = diferenca
            
        elif i == 3 and labirinto[inkyY][inkyX + 1] != '#':#  direita
            deltaX = blinkX - (pacmanX + 2)
            deltaY = blinkY - pacmanY
                        
            if deltaY < 0 and deltaX < 0:
                diferenca = (deltaY * -1) + (deltaX * -1)
                                    
            elif deltaY < 0:
                diferenca = (deltaY * -1) + deltaX
                                    
            elif deltaX < 0:
                diferenca = deltaY + (deltaX * -1)
                                    
            else:
                diferenca = deltaY + deltaX
                                    
            diferenca *= 2
            caminho[i] = diferenca
    
    for i in range(4):
        if caminho[i] == 0:
            caminho[i] = 1000
        
    for i in range(4):
        if caminho[i] < menor:
            menor = caminho[i]
            indiceCaminho = i
    # reliaza a escolha do caminho mais curto
    if indiceCaminho == 0:    
        if labirinto[inkyY - 1][inkyX] == '*':
            labirinto[inkyY][inkyX] = '*'
            inkyY -= 1
            
        elif labirinto[inkyY - 1][inkyX] == 'o':
            labirinto[inkyY][inkyX] = 'o'
            inkyY -= 1
        
        elif labirinto[inkyY - 1][inkyX] == '_':
            labirinto[inkyY][inkyX] = '_'
            inkyY -= 1
        
        elif labirinto[inkyY - 1][inkyX] == 'C':
            labirinto[inkyY][inkyX] = 'A'
            inkyY -= 1
        
            
    elif indiceCaminho == 1:
        if labirinto[inkyY + 1][inkyX] == '*':
            labirinto[inkyY][inkyX] = '*'
            inkyY += 1
                    
        elif labirinto[inkyY + 1][inkyX] == 'o':
            labirinto[inkyY][inkyX] = 'o'
            inkyY += 1
        
        elif labirinto[inkyY + 1][inkyX] == '_':
            labirinto[inkyY][inkyX] = '_'
            inkyY += 1
            
    elif indiceCaminho == 2:    
        if labirinto[inkyY][inkyX - 1] == '*':
            labirinto[inkyY][inkyX] = '*'
            inkyX -= 1
        
        elif labirinto[inkyY][inkyX - 1] == 'o':
            labirinto[inkyY][inkyX] = 'o'
            inkyX -= 1
        
        elif labirinto[inkyY][inkyX - 1] == '_':
            labirinto[inkyY][inkyX] = '_'
            inkyX -= 1
        
        elif labirinto[inkyY][inkyX - 1] == 'C':
            labirinto[inkyY][inkyX] = 'A'
            inkyX -= 1
            
    elif indiceCaminho == 3:
        if labirinto[inkyY][inkyX + 1] == '*':
            labirinto[inkyY][inkyX] = '*'
            inkyX += 1
                
        elif labirinto[inkyY][inkyX+ 1] == 'o':
            labirinto[inkyY][inkyX] = 'o'
            inkyX += 1
        
        elif labirinto[inkyY][inkyX+ 1] == '_':
            labirinto[inkyY][inkyX] = '_'
            inkyX += 1
            
        elif labirinto[inkyY][inkyX+ 1] == 'C':
            labirinto[inkyY][inkyX] = 'A'
            inkyX += 1
    
    return inkyY, inkyX
                
os.system("cls")
labirinto = []
pastilhas = 0
vidas = 1
vidaAtual = False
loop = 0

#posiçao dos personagens

#personagens
pacman = 'C'
fantasma = 'A'
opcao = ' '

for i in range(31):
    labirinto.append([])
    for j in range(28):
        labirinto[i].append(0)
                
prepararLabiritnto(labirinto)

pastilhas = colocarPastilhas(pastilhas, labirinto)

vidas = 1

while pastilhas > 0 and vidas >= 0:
    if vidas > 0 and  vidaAtual == False:
        vidaAtual = True
        vidas -= 1
        
        pacmanX = 13
        pacmanY = 23

        blinkX = 13
        blinkY = 11

        pinkX = 12
        pinkY = 14

        inkyX = 14
        inkyY = 14

        labirinto[pacmanY][pacmanX] = pacman
        labirinto[blinkY][blinkX] = fantasma
        labirinto[pinkY][pinkX] = fantasma
        labirinto[inkyY][inkyX] = fantasma
        mostrarLabirinto(labirinto)
        time.sleep(5)        
        loop = 0
    
    else:
        loop = 10
        mostrarLabirinto(labirinto)
        # if(Wc.kbhit()):  #verifica se uma tecla foi apertada
        #     opcao = Wc.getch()  #captura a tecla apertada
        time.sleep(1)

        # print(opcao) 
        opcao = input()
        
        pacmanY, pacmanX, pastilhas = movientacao(opcao, pacmanY, pacmanX, pacman, pastilhas, labirinto)

    # relização dos movimentos
        blinkY, blinkX = movimentoBlink(blinkX, blinkY, pacmanX, pacmanY, labirinto)
    
        if loop >= 10:
            if loop == 10:
                labirinto[pinkY][pinkX] = '*'
                pinkY = 11
                pinkX = 13
            pinkY, pinkX, vidaAtual = movimentoPink(pinkX, pinkY, pacmanX, pacmanY, labirinto, vidaAtual)
    
        if loop >= 15:    
            if loop == 15:
                labirinto[inkyY][inkyX] = '*'
                inkyY = 11
                inkyX = 13
    #        inkyY, inkyX = movimentoInky(inkyX, inkyY, blinkX, blinkY, pacmanX, pacmanY, labirinto)

        labirinto[pacmanY][pacmanX] = pacman
        labirinto[blinkY][blinkX] = fantasma 
        labirinto[pinkY][pinkX] = fantasma
        labirinto[inkyY][inkyX] = fantasma
        
        if (blinkX == pacmanX and blinkY == pacmanY) or (pinkX == pacmanX and pinkY == pacmanY) or (inkyX == pacmanX and inkyY == pacmanY):
            vidaAtual = False
        loop += 1

print("Game-Over")