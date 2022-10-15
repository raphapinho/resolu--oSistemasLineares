import numpy as np
import matplotlib.pyplot as plt

#lista = [10,1000,2000]
lista = []
listaItera = []
n = 0
while n <20000:
    n += 1000
    lista.append(n)

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
    return iteracao

for j in range(len(lista)):
    listaItera.append(gaussSeidel(array,y,x,10))



lis = np.array(lista)
lis2 = np.array(listaItera)
plt.plot(lis, lis2)
plt.ylabel('tamanho da metriz')
plt.xlabel('numero de interações')
plt.show()