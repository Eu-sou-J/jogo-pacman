import random

vivo = True
vidaAtual = 0

def movimentoPink(pinkX, pinkY, pacmanX, pacmanY, labirinto, passadoPinkX, passadoPinkY, opcao, pinkAtual, poder):
    caminho = [0, 0, 0, 0]
    menor = 1000
    indiceCaminho = 0
    posicaoX = 0
    posicaoY = 0
    if poder == True:
        posicaoX = random.randint(1, 26)
        posicaoY = random.randint(1, 29)
        for i in range(4):    
            if i == 0 and (labirinto[pinkY][pinkX - 1] != '#') and (labirinto[pinkY][pinkX - 1] != '_') and ((pinkX - 1) != passadoPinkX or pinkY != passadoPinkY):
                deltaX = (pinkX - 1) - posicaoX
                deltaY = pinkY - posicaoY
                if deltaY < 0 and deltaX < 0:
                    diferenca = (deltaY * -1) + (deltaX * -1)
            
                elif deltaY < 0:
                    diferenca = (deltaY * -1) + deltaX
            
                elif deltaX < 0:
                    diferenca = deltaY + (deltaX * -1)  
                
                else:  
                    diferenca = deltaY + deltaX
                            
            elif i == 1 and (labirinto[pinkY][pinkX + 1] != '#') and (labirinto[pinkY][pinkX + 1] != '_') and ((pinkX + 1) != passadoPinkX or pinkY != passadoPinkY):
                deltaX = (pinkX + 1) - posicaoX
                deltaY = pinkY - posicaoY
                if deltaY < 0 and deltaX < 0:
                    diferenca = (deltaY * -1) + (deltaX * -1)
                
                elif deltaY < 0:
                    diferenca = (deltaY * -1) + deltaX

                elif deltaX < 0:
                    diferenca = deltaY + (deltaX * -1)  

                else:  
                    diferenca = deltaY + deltaX                
        
            elif i == 2 and (labirinto[pinkY - 1][pinkX] != '#') and (labirinto[pinkY -1][pinkX] != '_') and (pinkX != passadoPinkX or (pinkY - 1) != passadoPinkY):
                deltaX =  pinkX - posicaoX
                deltaY = (pinkY - 1) - posicaoY
                if deltaY < 0 and deltaX < 0:
                    diferenca = (deltaY * -1) + (deltaX * -1)
                
                elif deltaY < 0:
                    diferenca = (deltaY * -1) + deltaX

                elif deltaX < 0:
                    diferenca = deltaY + (deltaX * -1)  

                else:  
                    diferenca = deltaY + deltaX
                        
            elif i == 3 and (labirinto[pinkY + 1][pinkX] != '#') and (labirinto[pinkY + 1][pinkX] != '_') and (pinkX != passadoPinkX or (pinkY + 1) != passadoPinkY):
                deltaX =  pinkX - posicaoX
                deltaY = (pinkY + 1) - posicaoY
                if deltaY < 0 and deltaX < 0:
                    diferenca = (deltaY * -1) + (deltaX * -1)
            
                elif deltaY < 0:
                    diferenca = (deltaY * -1) + deltaX
                
                elif deltaX < 0:
                    diferenca = deltaY + (deltaX * -1)  
                
                else:  
                    diferenca = deltaY + deltaX
        
            caminho[i] = diferenca

    elif poder == False:    
        if opcao == 'A' or opcao == 'a':
            for i in range(4):
                #faz o caucluo dos possiveis caminhos do pink
                diferenca = 1000
                if i == 0 and (labirinto[pinkY][pinkX - 1] != '#') and (labirinto[pinkY][pinkX - 1] != '_') and ((pinkX - 1) != passadoPinkX or pinkY != passadoPinkY):
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
                            
                elif i == 1 and (labirinto[pinkY][pinkX + 1] != '#') and (labirinto[pinkY][pinkX + 1] != '_') and ((pinkX + 1) != passadoPinkX or pinkY != passadoPinkY):
                    deltaX = (pinkX + 1) - (pacmanX - 5)
                    deltaY = pinkY - pacmanY
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
                
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX

                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  

                    else:  
                        diferenca = deltaY + deltaX                
        
                elif i == 2 and (labirinto[pinkY - 1][pinkX] != '#') and (labirinto[pinkY -1][pinkX] != '_') and (pinkX != passadoPinkX or (pinkY - 1) != passadoPinkY):
                    deltaX =  pinkX - (pacmanX - 5)
                    deltaY = (pinkY - 1) - pacmanY
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
                
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX

                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  

                    else:  
                        diferenca = deltaY + deltaX
                        
                elif i == 3 and (labirinto[pinkY + 1][pinkX] != '#') and (labirinto[pinkY + 1][pinkX] != '_') and (pinkX != passadoPinkX or (pinkY + 1) != passadoPinkY):
                    deltaX =  pinkX - (pacmanX - 5)
                    deltaY = (pinkY + 1) - pacmanY
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
            
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX
                
                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  
                
                    else:  
                        diferenca = deltaY + deltaX
        
                caminho[i] = diferenca
                
        elif opcao == 'd' or opcao == 'D':
            for i in range(4):
                #faz o caucluo dos possiveis caminhos do pink
                diferenca = 1000
                if i == 0 and (labirinto[pinkY][pinkX - 1] != '#') and (labirinto[pinkY][pinkX - 1] != '_') and ((pinkX - 1) != passadoPinkX or pinkY != passadoPinkY):
                    deltaX = (pinkX - 1) - (pacmanX + 5)
                    deltaY = pinkY - pacmanY
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
            
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX
                
                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  
                
                    else:  
                        diferenca = deltaY + deltaX
                            
                elif i == 1 and (labirinto[pinkY][pinkX + 1] != '#') and (labirinto[pinkY][pinkX + 1] != '_') and ((pinkX + 1) != passadoPinkX or pinkY != passadoPinkY):
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
        
                elif i == 2 and (labirinto[pinkY - 1][pinkX] != '#') and (labirinto[pinkY -1][pinkX] != '_') and (pinkX != passadoPinkX or (pinkY - 1) != passadoPinkY):
                    deltaX =  pinkX - (pacmanX + 5)
                    deltaY = (pinkY - 1) - pacmanY
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
                
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX

                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  

                    else:  
                        diferenca = deltaY + deltaX
                        
                elif i == 3 and (labirinto[pinkY + 1][pinkX] != '#') and (labirinto[pinkY + 1][pinkX] != '_') and (pinkX != passadoPinkX or (pinkY + 1) != passadoPinkY):
                    deltaX =  pinkX - (pacmanX + 5)
                    deltaY = (pinkY + 1) - pacmanY
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
            
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX
                
                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  
                
                    else:  
                        diferenca = deltaY + deltaX
        
                caminho[i] = diferenca
        elif opcao == 'W' or opcao == 'w':
            for i in range(4):
                #faz o caucluo dos possiveis caminhos do pink
                diferenca = 1000
                if i == 0 and (labirinto[pinkY][pinkX - 1] != '#') and (labirinto[pinkY][pinkX - 1] != '_') and ((pinkX - 1) != passadoPinkX or pinkY != passadoPinkY):
                    deltaX = (pinkX - 1) - pacmanX
                    deltaY = pinkY - (pacmanY - 5)
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
            
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX
                
                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  
                
                    else:  
                        diferenca = deltaY + deltaX
                            
                elif i == 1 and (labirinto[pinkY][pinkX + 1] != '#') and (labirinto[pinkY][pinkX + 1] != '_') and ((pinkX + 1) != passadoPinkX or pinkY != passadoPinkY):
                    deltaX = (pinkX + 1) - pacmanX
                    deltaY = pinkY - (pacmanY - 5)
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
                
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX

                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  

                    else:  
                        diferenca = deltaY + deltaX                
        
                elif i == 2 and (labirinto[pinkY - 1][pinkX] != '#') and (labirinto[pinkY -1][pinkX] != '_') and (pinkX != passadoPinkX or (pinkY - 1) != passadoPinkY):
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
                        
                elif i == 3 and (labirinto[pinkY + 1][pinkX] != '#') and (labirinto[pinkY + 1][pinkX] != '_') and (pinkX != passadoPinkX or (pinkY + 1) != passadoPinkY):
                    deltaX =  pinkX - pacmanX
                    deltaY = (pinkY + 1) - (pacmanY - 5)
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
            
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX
                
                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  
                
                    else:  
                        diferenca = deltaY + deltaX
        
                caminho[i] = diferenca
        elif opcao == 'S' or opcao == 's':
            for i in range(4):
                #faz o caucluo dos possiveis caminhos do pink
                diferenca = 1000
                if i == 0 and (labirinto[pinkY][pinkX - 1] != '#') and (labirinto[pinkY][pinkX - 1] != '_') and ((pinkX - 1) != passadoPinkX or pinkY != passadoPinkY):
                    deltaX = (pinkX - 1) - pacmanX 
                    deltaY = pinkY - (pacmanY + 5)
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
            
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX
                
                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  
                
                    else:  
                        diferenca = deltaY + deltaX
                            
                elif i == 1 and (labirinto[pinkY][pinkX + 1] != '#') and (labirinto[pinkY][pinkX + 1] != '_') and ((pinkX + 1) != passadoPinkX or pinkY != passadoPinkY):
                    deltaX = (pinkX + 1) - pacmanX
                    deltaY = pinkY - (pacmanY + 5)
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
                
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX

                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  

                    else:  
                        diferenca = deltaY + deltaX                
        
                elif i == 2 and (labirinto[pinkY - 1][pinkX] != '#') and (labirinto[pinkY -1][pinkX] != '_') and (pinkX != passadoPinkX or (pinkY - 1) != passadoPinkY):
                    deltaX =  pinkX - pacmanX
                    deltaY = (pinkY - 1) - (pacmanY + 5)
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
                
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX

                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  

                    else:  
                        diferenca = deltaY + deltaX
                        
                elif i == 3 and (labirinto[pinkY + 1][pinkX] != '#') and (labirinto[pinkY + 1][pinkX] != '_') and (pinkX != passadoPinkX or (pinkY + 1) != passadoPinkY):
                    deltaX =  pinkX - pacmanX
                    deltaY = (pinkY + 1) - (pacmanY + 5)
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
            
                if (labirinto[pinkY][pinkX - 1] != '#') and (labirinto[pinkY][pinkX - 1] != '_'):
                    labirinto[pinkY][pinkX] = pinkAtual 
                    passadoPinkX = pinkX
                    passadoPinkY = pinkY                
                    pinkX -= 1
                    pinkAtual = labirinto[pinkY][pinkX] 
                    
                if pinkX == 0 and pinkY == 14:
                    pinkX = 27
                    
            elif indiceCaminho == 1:
                if (labirinto[pinkY][pinkX + 1] != '#') and (labirinto[pinkY][pinkX + 1] != '_'):
                    labirinto[pinkY][pinkX] = pinkAtual
                    passadoPinkX = pinkX
                    passadoPinkY = pinkY                        
                    pinkX += 1
                    pinkAtual = labirinto[pinkY][pinkX]

                if pinkX == 27 and pinkY == 14:
                    pinkX = 0
                
            elif indiceCaminho == 2:
                if (labirinto[pinkY - 1][pinkX] != '#') and (labirinto[pinkY - 1][pinkX] != '_'):
                    labirinto[pinkY][pinkX] = pinkAtual
                    passadoPinkX = pinkX
                    passadoPinkY = pinkY
                    pinkY -= 1
                    pinkAtual = labirinto[pinkY][pinkX]
                    
            elif indiceCaminho == 3:
                if (labirinto[pinkY + 1][pinkX] != '#') and (labirinto[pinkY + 1][pinkX] != '_'):
                    labirinto[pinkY][pinkX] = pinkAtual                 
                    passadoPinkX = pinkX
                    passadoPinkY = pinkY 
                    pinkY += 1                    
                    pinkAtual = labirinto[pinkY][pinkX]
                        
    return pinkY, pinkX, passadoPinkY, passadoPinkX, pinkAtual