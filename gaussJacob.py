import numpy as np
  
# 1st argument --> numbers ranging from 0 to 9, 
# 2nd argument, row = 2, col = 3
array = np.random.randint(10, size=(2, 2))
print(array)

def gaussJacobi(A,b,vetorS,iteracoes):
    iteracao = 0
    vetorAux = []
    for k in range(len(vetorS)):
        vetorAux.append(0)

    while iteracao != iteracoes:
        for i in range(len(A)):
            x = b[i]
            for j in range(len(A)):
                if i != j:
                    x -= A[i][j]*vetorS[j]
            x /= A[i][i]
            vetorAux[i] = x
        iteracao += 1

    for p in range(len(vetorAux)):
        vetorS[p] = vetorAux[p]

    print(vetorS)
    print(f"numero de iterações: {iteracao}")

gaussJacobi(array,[1,-1],[0,0],30)