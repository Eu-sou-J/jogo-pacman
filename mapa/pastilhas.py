def colocartictac(tictac, labirinto):
    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
# evita que que onde não deve ter pastilha não recceba pastilha 
            if(i >= 9 and i <= 19 and j >= 7 and j <= 20) and labirinto[i][j] != '#':
                if labirinto[i][j] == ' ':
                    labirinto[i][j] = ' '
                elif labirinto[i][j] == '_':
                    labirinto[i][j] = '_'
# coloca pastilha
            elif labirinto[i][j] == ' ' and labirinto[i][j] != '#':
                if i == 14 and (j <= 5 or j >= 22):
                    labirinto[i][j] = ' '
                elif i == 4 and (j == 1 or j == 26):
                    labirinto[i][j] = 'O'
                    tictac += 1
                elif i == 23 and (j == 1 or j == 26):
                    labirinto[i][j] = 'O'
                    tictac += 1
                else:
                    labirinto[i][j] = 'o'
                    tictac += 1 
                
    return tictac
    