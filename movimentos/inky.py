
indiceCaminho = 0

def movimentoInky(inkyX, inkyY, blinkX, blinkY, pacmanX, pacmanY, labirinto, passadoinkyX, passadoinkyY, inkyAtual):
    caminho = [0, 0, 0, 0]
    menor = 1000
    #faz o caucluo dos possiveis caminhos do inky
    for i in range(4):
        diferenca = 1000
        if i == 0 and labirinto[inkyY][inkyX - 1] != '#' and (labirinto[inkyY - 1][inkyX] != '_') and (inkyY != passadoinkyY or (inkyX - 1)!= passadoinkyX): #esquerda
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
            
        elif i == 1 and labirinto[inkyY][inkyX + 1] != '#' and (labirinto[inkyY][inkyX + 1] != '_') and (inkyY != passadoinkyY or (inkyX + 1) != passadoinkyX):#  direita
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
        
        elif i == 2 and (labirinto[inkyY - 1][inkyX] != '#') and (labirinto[inkyY - 1][inkyX] != '_') and ((inkyY - 1) != passadoinkyY or inkyX != passadoinkyX):# para cima 
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
        
        elif i == 3 and labirinto[inkyY + 1][inkyX] != '#' and (labirinto[inkyY - 1][inkyX] != '_') and ((inkyY + 1) != passadoinkyY or inkyX != passadoinkyX):#para baixo
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
    
    for i in range(4):
        if caminho[i] == 0:
            caminho[i] = 1000
        
    for i in range(4):
        if caminho[i] < menor:
            menor = caminho[i]
            indiceCaminho = i
    # reliaza a escolha do caminho mais curto
    
    if indiceCaminho == 0:    
        if labirinto[inkyY][inkyX - 1] != '#':
            labirinto[inkyY][inkyX] = inkyAtual
            passadoinkyX = inkyX
            passadoinkyY = inkyY
            inkyX -= 1
            inkyAtual = labirinto[inkyY][inkyX]
        
        if inkyY == 14 and inkyX == 0:
            inkyX = 27
            
    elif indiceCaminho == 1:
        if labirinto[inkyY][inkyX + 1] != '#':
            labirinto[inkyY][inkyX] = inkyAtual
            passadoinkyX = inkyX
            passadoinkyY = inkyY
            inkyX += 1
            inkyAtual = labirinto[inkyY][inkyX]    
        
        if inkyY == 14 and inkyX == 27:
            inkyX = 0
    
    
    elif indiceCaminho == 2:    
        if labirinto[inkyY - 1][inkyX] != '#':
            labirinto[inkyY][inkyX] = inkyAtual
            passadoinkyX = inkyX
            passadoinkyY = inkyY
            inkyY -= 1
            inkyAtual = labirinto[inkyY][inkyX]  
        
    elif indiceCaminho == 3:
        if labirinto[inkyY + 1][inkyX] != '#':
            labirinto[inkyY][inkyX] = inkyAtual
            passadoinkyX = inkyX
            passadoinkyY = inkyY
            inkyY += 1
            inkyAtual = labirinto[inkyY][inkyX]        
    
    return inkyY, inkyX, passadoinkyY, passadoinkyX, inkyAtual