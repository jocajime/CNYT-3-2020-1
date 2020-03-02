
def multiplicacionMatriz(a, b):
    if len(a[0]) == len(b):
        filas = len(a)
        columnas = len(b[0])
        res = [[0 for i in range(columnas)] for j in range(filas)]
        for i in range(0, filas):
            for j in range(0, columnas):
                temp = 0
                for k in range(0, len(b)):
                    temp += a[i][k]* b[k][j]
                res[i][j] = temp
        return res
    else:
        print("las matrices no se pueden multiplicar")
        return False

def confirmar_matriz(a):
    estado = True
    columnas = len(a[0])
    for i in range(columnas):
        temp = 0
        for j in range(len(a)):
            temp += a[j][i]
        if temp == 0:
            estado = False
            break
    return estado
    

def t_clics(a,t):
    if confirmar_matriz(a):
        res = [[a[j][i] for i in range(len(a[0]))] for j in range(len(a))]
        for i in range(t-1):
            res = multiplicacionMatriz(res, a)
        return res

def multiples_rendijas(r):
    n = 2+3*r
    matriz = [[0 for i in range(n)] for j in range(n)]
    for j in range(1,r+1):
        matriz[j][0] = 1/r
    temp = r+1       
    for j in range(1,r+1):
        matriz[temp][j] = 1/3
        matriz[temp+1][j] = 1/3
        matriz[temp+2][j] = 1/3
        temp+=2
    for i in range(r+1,n):
        matriz[i][i] = 1
    
    
    return matriz

def vector_final(num_rendijas):
    vectori = [[0] for i in range(2+3*num_rendijas)]
    vectori[0][0] = 1
    return multiplicacionMatriz(t_clics(multiples_rendijas(num_rendijas),2),vectori)

def imprimir_matriz(a):
    for i in range(len(a)):
        print(a[i])

def main():
    imprimir_matriz(vector_final(3))


main()
    
        


        
            
            

            
