
# Importing NumPy Library
import numpy as np
import sys

n = int(input("coloque o tamanho da matriz ao qual vc quer criar:\n"))

#gerador de matriz
a = np.random.randint(10, size=(n, n+1))
print(a)

#gerador de matriz vazia
x = np.zeros(n)

def GaussElimination(n):
    # aplicando eliminação de gauss
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('divisão por zero detectada!')
            
        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]
            
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    # substituição por traz
    x[n-1] = a[n-1][n]/a[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
        
        x[i] = x[i]/a[i][i]

    # mostrando a solução
    print('\a solução encontrada foi: ')
    for i in range(n):
        print(f'{i} = {x[i]}', end = '\t')


GaussElimination(n)
