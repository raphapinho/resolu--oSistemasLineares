import numpy as np

def LUDecompose (tabela):
    linhas,colunas=np.shape(tabela)
    L=np.zeros((linhas,colunas))
    U=np.zeros((linhas,colunas))
    if linhas!=colunas:
        return []
    for i in range (colunas):
        for j in range(i-1):
            soma=0
            for k in range (j-1):
                soma+=L[i][k]*U[k][j]
            L[i][j]=(tabela[i][j]-soma)/U[j][j]
        L[i][i]=1
        
        for j in range(i-1,colunas):
            soma1=0
            for k in range(i-1):
                soma1+=L[i][k]*U[k][j]
            U[i][j]=tabela[i][j]-soma1
    return L,U

if __name__ == "__main__":
    
    lista = [10,1000,2000]

    for i in range(len(lista)):

        #n = int(input(f"coloque o tamanho da matriz:\n"))
        matrix = np.random.randint(10, size=(lista[i], lista[i]))
        #print(array)
        L,U = LUDecompose(matrix)
        print(L)
        print(U)
    