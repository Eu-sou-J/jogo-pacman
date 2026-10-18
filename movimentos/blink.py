import random

vidaAtual = 0

def movimentoBlink(passadoBlinkX, passadoBlinkY, blinkX, blinkY, pacmanX, pacmanY, labirinto, poder, blinkAtual):
    caminho = [0, 0, 0, 0]
    indiciCaminho = 0
    menor = 1000
    # vivo = True
    posicaoX = 0
    posicaoY = 0
    #faz o caucluo dos possiveis caminhos do blink
    
    if poder == True:
        posicaoX = random.randint(1, 26)
        posicaoY = random.randint(1, 29)
        
        for i in range(4):
            diferenca = 1000
            if i == 0 and (labirinto[blinkY][blinkX - 1] != '#') and ((blinkX - 1) != passadoBlinkX or blinkY != passadoBlinkY) and (labirinto[blinkY][blinkX - 1] != '_'):
                deltaX = (blinkX - 1) - posicaoX
                deltaY = blinkY - posicaoY
              
                if deltaY <= 0 and deltaX <= 0:
                    diferenca = (deltaX * -1) + (deltaY * -1) 
                  
                elif deltaY <= 0:
                    diferenca = deltaX + (deltaY * -1)
                  
                elif deltaX <= 0:
                    diferenca = (deltaX * -1) + deltaY
                else:
                    diferenca = deltaX + deltaY
                              
            if i == 1 and (labirinto[blinkY][blinkX + 1] != '#') and ((blinkX + 1) != passadoBlinkX or blinkY != passadoBlinkY) and (labirinto[blinkY][blinkX + 1] != '_'):
                deltaX = (blinkX + 1) - posicaoX
                deltaY = blinkY - posicaoY
              
                if deltaY <= 0 and deltaX <= 0:
                    diferenca = (deltaX * -1) + (deltaY * -1)
                  
                elif deltaY <= 0:
                    diferenca = deltaX + (deltaY * -1)
                  
                elif deltaX <= 0:
                    diferenca = (deltaX * -1) + deltaY
                  
                else:
                    diferenca = deltaX + deltaY   
                              
            if i == 2 and (labirinto[blinkY - 1][blinkX] != '#') and ((blinkY - 1) != passadoBlinkY or blinkX != passadoBlinkX) and (labirinto[blinkY - 1][blinkX] != '_'):
                deltaX = blinkX - posicaoX
                deltaY = (blinkY - 1) - posicaoY
              
                if deltaY <= 0 and deltaX <= 0:
                    diferenca = (deltaX * -1) + (deltaY * -1)
                  
                elif deltaY <= 0:
                    diferenca = deltaX + (deltaY * -1)
                  
                elif deltaX <= 0:
                      diferenca = (deltaX * -1) + deltaY
                else:
                      diferenca = deltaX + deltaY
              
            if i == 3 and (labirinto[blinkY + 1][blinkX] != '#') and  ((blinkY + 1) != passadoBlinkY or blinkX != passadoBlinkX) and (labirinto[blinkY + 1][blinkX] != '_'):
                deltaX = blinkX - posicaoX
                deltaY = (blinkY + 1)- posicaoY
              
                if deltaY <= 0 and deltaX <= 0:
                    diferenca = (deltaX * -1) + (deltaY * -1)
                  
                elif deltaY <= 0:
                    diferenca = deltaX + (deltaY * -1)
                  
                elif deltaX <= 0:
                    diferenca = (deltaX * -1) + deltaY    
                  
                else:
                    diferenca = deltaX + deltaY
  
            caminho[i] = diferenca
            
    elif poder == False:     
        for i in range(4):
            diferenca = 1000
            if i == 0 and (labirinto[blinkY][blinkX - 1] != '#') and ((blinkX - 1) != passadoBlinkX or blinkY != passadoBlinkY) and (labirinto[blinkY][blinkX - 1] != '_'):
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
                            
            if i == 1 and (labirinto[blinkY][blinkX + 1] != '#') and ((blinkX + 1) != passadoBlinkX or blinkY != passadoBlinkY) and (labirinto[blinkY][blinkX + 1] != '_'):
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
                            
            if i == 2 and (labirinto[blinkY - 1][blinkX] != '#') and ((blinkY - 1) != passadoBlinkY or blinkX != passadoBlinkX) and (labirinto[blinkY - 1][blinkX] != '_'):
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
            
            if i == 3 and (labirinto[blinkY + 1][blinkX] != '#') and  ((blinkY + 1) != passadoBlinkY or blinkX != passadoBlinkX) and (labirinto[blinkY + 1][blinkX] != '_'):
                deltaX = blinkX - pacmanX
                deltaY = (blinkY + 1)- pacmanY
            
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
            if labirinto[blinkY][blinkX - 1] != '#' and labirinto[blinkY][blinkX - 1] != '_': 
                labirinto[blinkY][blinkX] = blinkAtual
                passadoBlinkX = blinkX
                passadoBlinkY = blinkY
                blinkX -= 1
                blinkAtual = labirinto[blinkY][blinkX]
            
            if blinkX == 0 and blinkY == 14:
                blinkX = 27
            
        elif indiciCaminho == 1:
            
            if labirinto[blinkY][blinkX + 1] != '#' and labirinto[blinkY][blinkX + 1] != '_':
                labirinto[blinkY][blinkX] = blinkAtual
                passadoBlinkX = blinkX
                passadoBlinkY = blinkY
                blinkX += 1
                blinkAtual = labirinto[blinkY][blinkX]
            
            if blinkX == 27 and blinkY == 14:
                blinkX = 0
                
        elif indiciCaminho == 2:
        
            if labirinto[blinkY - 1][blinkX] != '#' and labirinto[blinkY - 1][blinkX] != '_':
                labirinto[blinkY][blinkX] = blinkAtual
                passadoBlinkX = blinkX
                passadoBlinkY = blinkY
                blinkY -= 1
                blinkAtual = labirinto[blinkY][blinkX]

        elif indiciCaminho == 3:
        
            if labirinto[blinkY + 1][blinkX] != '#' and labirinto[blinkY + 1][blinkX] != '_':                   
                labirinto[blinkY][blinkX] = blinkAtual
                passadoBlinkX = blinkX
                passadoBlinkY = blinkY
                blinkY += 1
                blinkAtual = labirinto[blinkY][blinkX]
                    
                         
    return blinkY, blinkX, passadoBlinkY, passadoBlinkX, blinkAtual