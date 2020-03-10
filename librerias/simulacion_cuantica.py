import cal_complejos

def confirmar_matriz(a):
    estado = True
    columnas = len(a[0])
    for i in range(columnas):
        temp = (0,0)
        for j in range(len(a)):
            temp = cal_complejos.suma(temp,a[j][i])
        if temp == 0:
            estado = False
            break
    return estado
    

def t_clics(a,t):
    if confirmar_matriz(a):
        res = [[a[j][i] for i in range(len(a[0]))] for j in range(len(a))]
        for i in range(t-1):
            res = cal_complejos.multiplicacionMatriz(res, a)
        return res

def multiples_rendijas_real(r):
    n = 2+3*r
    matriz = [[(0,0) for i in range(n)] for j in range(n)]
    for j in range(1,r+1):
        matriz[j][0] = (1/r,0)
    temp = r+1       
    for j in range(1,r+1):
        matriz[temp][j] = (1/3,0)
        matriz[temp+1][j] = (1/3,0)
        matriz[temp+2][j] = (1/3,0)
        temp+=2
    for i in range(r+1,n):
        matriz[i][i] = (1,0)
    
    return matriz

def multiples_rendijas_imaginario(r):
    n = 2+3*r
    matriz = [[(0,0) for i in range(n)] for j in range(n)]
    for j in range(1,r+1):
        matriz[j][0] = (1/(2**0.5),0)
    temp = r+1       
    for j in range(1,r+1):
        matriz[temp][j] = (-1/(6**0.5),1/(6**0.5))
        matriz[temp+1][j] = (-1/(6**0.5),-1/(6**0.5))
        matriz[temp+2][j] = (1/(6**0.5),-1/(6**0.5))
        temp+=2
    for i in range(r+1,n):
        matriz[i][i] = (1,0)    
    return matriz


def vector_final_real(num_rendijas):
    vectori = [[(0,0)] for i in range(2+3*num_rendijas)]
    vectori[0][0] = (1,0)
    return cal_complejos.multiplicacionMatriz(t_clics(multiples_rendijas_real(num_rendijas),2),vectori)

def vector_final_imaginario(num_rendijas):
    vectori = [[(0,0)] for i in range(2+3*num_rendijas)]
    vectori[0][0] = (1,0)
    return cal_complejos.multiplicacionMatriz(t_clics(multiples_rendijas_imaginario(num_rendijas),2),vectori)

def imprimir_matriz(a):
    for i in range(len(a)):
        print(a[i])
def union_sistemas(a,b):
    return cal_complejos.tensorMatrices(a,b)

##def main():
####    imprimir_matriz(vector_final_real(2))
####    print("--------")
####    imprimir_matriz(vector_final_imaginario(2))
####    print("--------")
##    imprimir_matriz(cal_complejos.transpuestaMatriz(vector_final_imaginario(2)))
##
##main()

    


        
            
            

            
