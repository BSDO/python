picture = [ #matriz com 6 elementos
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for row in picture: #percorra toda matriz
    for pixel in row: #percorra todo conteudo de cada elemento da matriz
        if (pixel == 1): 
            print('*', end='') 
            #quando cada elemento pixel for igual a 1 ira representar como *
        else:
            print(' ',end='')
        #caso for 0 ou vazio o conteudo, deixe em espaço em branco
    print(' ') #separa cada nova linha
    
