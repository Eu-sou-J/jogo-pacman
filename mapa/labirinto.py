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
                labirinto[i][j] = ' '
                
#caixa dos fantasmas     
    for i in range(12,17):
        for j in range(10,18):
            labirinto[i][j] = '#'
            
    for i in range(13,16):
        for j in range(11,17):
            labirinto[i][j] = ' '
            
    labirinto[12][13] = '_'
    labirinto[12][14] = '_'
    
    for i in range(30, 31):
        for j in range(28):
            labirinto[i][j] = '#'
    
    for i in range(20, 31):
        for j in range(27, 28):
            labirinto[i][j] = '#'

def mostrarLabirinto(labirinto):
    tela = ''
    for i in range(31):
        for j in range(28):
            tela += labirinto[i][j] + " "
        tela += "\n"
    
    print(tela)