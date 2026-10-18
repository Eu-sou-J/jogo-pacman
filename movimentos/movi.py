def moviPacman(opcao, pacmanY, pacmanX, pacman, pastilhas, labirinto, pontos, poder):
    # A movimentacao que pacman fez de acordo com o usuario
    if opcao == 'w' or opcao == 'W':
        if labirinto[pacmanY - 1][pacmanX] == '#':
               labirinto[pacmanY][pacmanX] = pacman
        else:
            if labirinto[pacmanY -  1][pacmanX] == 'O':
                print("\a")
                poder = True
                pastilhas -= 1
                pacmanY -= 1
            
            elif labirinto[pacmanY - 1][pacmanX] == 'o':
                print("\a")
                labirinto[pacmanY][pacmanX] = ' '
                pacmanY -= 1
                pastilhas -= 1
                labirinto[pacmanY][pacmanX] = pacman
                pontos += 10
            else: 
                labirinto[pacmanY][pacmanX] = ' '
                pacmanY -= 1
                labirinto[pacmanY][pacmanX] = pacman
               
    elif opcao == 'd' or opcao == 'D':
        if pacmanY == 14 and pacmanX == 27:
            labirinto[pacmanY][pacmanX] = ' '
            pacmanX = 0
            labirinto[pacmanY][pacmanX] = pacman        
        
        elif labirinto[pacmanY][pacmanX + 1] == '#':
            labirinto[pacmanY][pacmanX] = pacman        
                 
        else:
            if labirinto[pacmanY][pacmanX + 1] == 'O':
                print("\a")
                poder = True
                pastilhas -= 1
                pacmanX += 1
                
            elif labirinto[pacmanY][pacmanX + 1] == 'o':
                print("\a")
                labirinto[pacmanY][pacmanX] = ' '
                pacmanX += 1
                pastilhas -= 1
                labirinto[pacmanY][pacmanX] = pacman
                pontos += 10
                
            else:
                labirinto[pacmanY][pacmanX] = ' '
                pacmanX += 1
                labirinto[pacmanY][pacmanX] = pacman
    
    elif opcao == 'a' or opcao == 'A':
        if labirinto[pacmanY][pacmanX - 1] == '#':
            labirinto[pacmanY][pacmanX] = pacman
        
        elif pacmanY == 14 and pacmanX == 0:
            labirinto[pacmanY][pacmanX] = ' '
            pacmanX = 27
            labirinto[pacmanY][pacmanX] = pacman                
            
        else:
            if labirinto[pacmanY][pacmanX - 1] == 'O':
                print("\a")
                poder = True
                pastilhas -= 1
                pacmanX -= 1
                
            elif labirinto[pacmanY][pacmanX - 1] == 'o':
                print("\a")
                labirinto[pacmanY][pacmanX] = ' '
                pacmanX -= 1
                pastilhas -= 1
                labirinto[pacmanY][pacmanX] = pacman
                pontos += 10

            else:   
                labirinto[pacmanY][pacmanX] = ' '
                pacmanX -= 1
                labirinto[pacmanY][pacmanX] = pacman
    
    elif opcao == 's' or opcao == 'S':
        if labirinto[pacmanY + 1][pacmanX] == '#':
           labirinto[pacmanY][pacmanX] = pacman
        else:
            if labirinto[pacmanY + 1][pacmanX] == 'O':
                print("\a")
                poder = True
                pastilhas -= 1
                pacmanY += 1

            elif labirinto[pacmanY + 1][pacmanX] == 'o':
                print("\a")
                labirinto[pacmanY][pacmanX] = ' '
                pacmanY += 1
                labirinto[pacmanY][pacmanX] = pacman
                pastilhas -=  1
                pontos += 10

            else:
                labirinto[pacmanY][pacmanX] = ' '
                pacmanY += 1
                labirinto[pacmanY][pacmanX] = pacman

    return pacmanY, pacmanX, pastilhas, pontos, poder 