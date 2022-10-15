import timeit
import numpy as np
import sys
import matplotlib.pyplot as plt

#n = int(input("coloque o tamanho da matriz ao qual vc quer criar:\n"))

lista = []
listTime = []

n = 0
while n <20000:
    n += 1000
    lista.append(n)

def GaussElimination(n):
        start = timeit.default_timer()
        # aplicando eliminação de gauss
        for i in range(n):
            if a[i][i] == 0.0:                
                break
                #sys.exit('divisão por zero detectada!')
                
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
        #print('\a solução encontrada foi: ')
        #for i in range(n):
        #    print(f'{i} = {x[i]}', end = '\t')
        stop = timeit.default_timer()
        time = stop - start
        return time

for i in range(len(lista)):
    a = np.random.randint(10, size=(lista[i], lista[i]+1))
    print(a)
    
    #gerador de matriz vazia
    x = np.zeros(lista[i])

    listTime.append(GaussElimination(lista[i]))
    print(listTime)




lis = np.array(lista)
lis2 = np.array(listTime)
plt.plot(lis, lis2)
plt.ylabel('tempo de execução:')
plt.xlabel('tamanho da metriz:')
plt.show()





def takingTime(programa):
    start = timeit.default_timer()

    programa

    stop = timeit.default_timer()

    #return start-stop
    print(start-stop)

