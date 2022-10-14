
# Importing NumPy Library
from matplotlib import pyplot
import numpy as np
import sys

n = int(input("coloque o tamanho da matriz ao qual vc quer criar:\n"))

#gerador de matriz
a = np.random.randint(10, size=(n, n+1))
print(a)

# Making numpy array of n size and initializing 
# to zero for storing solution vector
x = np.zeros(n)

def GaussElimination(n):
    # Applying Gauss Elimination
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
            
        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]
            
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    # Back Substitution
    x[n-1] = a[n-1][n]/a[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
        
        x[i] = x[i]/a[i][i]

    # Displaying solution
    print('\a solução encontrada foi: ')
    for i in range(n):
        print(f'{i} = {x[i]}', end = '\t')



def graph_series(list_of_execution_time):
    


    values = {}
    for element in list_of_execution_time:
        if element[0] not in values:
            values[element[0]] = [(element[2] - element[1])]
        else:
            values[element[0]].append(element[2] - element[1])
    for key, value in values.items():
        pyplot.plot(value, markersize=20,label=key)
    pyplot.legend()
    pyplot.show()

graph_series(GaussElimination(n))
