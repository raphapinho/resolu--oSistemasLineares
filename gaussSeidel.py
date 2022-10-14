import numpy as np
  
# 1st argument --> numbers ranging from 0 to 9, 
# 2nd argument, row = 2, col = 3
lista = [10,1000,2000]

for i in range(len(lista)):
    #n = int(input("coloque o tamanho da matriz:\n"))
    array = np.random.randint(10, size=(lista[i], lista[i]))
    x = np.zeros(lista[i])
    y = np.zeros(lista[i])

for j in range(len(y)):
    y[j] =  1

print(array)

def gaussSeidel(A,b,vetorS,iteracoes):
    iteracao = 0
    while iteracao < iteracoes:
        for i in range(len(A)):
            x = b[i]
            for j in range(len(A)):
                if i != j:
                    x -= A[i][j]*vetorS[j]
            x /= A[i][i]
            vetorS[i] = x
        iteracao += 1
    print(vetorS)

gaussSeidel(array,y,x,10)