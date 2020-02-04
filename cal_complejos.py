from sys import stdin
import math

#suma dos numeros complejos representados por una tupla, y retorna un numero complejo representado por una tupla
def suma(a,b):
    return (a[0]+b[0],a[1]+b[1])

#resta dos numeros complejos representados por una tupla, y retorna un numero complejo representado por una tupla
def resta(a,b):
    return (a[0]-b[0],a[1]-b[1])

#multiplica un numero complejo representado por una tupla con un numero escalar, y retorna un numero complejo representado por una tupla
def porEscalar(r,a):
    return (r*a[0],r*a[1])

#multiplica dos numeros complejos representados por una tupla, y retorna un numero complejo representado por una tupla
def multiplicacion(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])

#divide dos numeros complejos representados por una tupla, y retorna un numero complejo representado por una tupla
def division(a,b):
    return ((a[0]*b[0]+a[1]*b[1])/(b[0]**2+b[1]**2),(a[1]*b[0]-a[0]*b[1])/(b[0]**2+b[1]**2))

#retorna el modulo de un numero complejo representado por una tupla
def modulo(a):
    return (a[0]**2+a[1]**2)**0.5

#retorna el conjugado de un numero complejo representado por una tupla
def conjugado(a):
    return (a[0],a[1]*-1)

#recibe un numero complejo y retorna el mismo en coordenadas polares
def aPolar(a):
    return (modulo(a),math.atan(a[1]/a[0]))

#imprime un numero complejo 
def prettyPrint(a):
    if a[1] < 0:
        return ""+str(a[0])+str(a[1])+"i"
    else:
        
        return ""+str(a[0])+"+"+str(a[1])+"i"

#retorna la phase de un numero complejo
def phase(a):
    return math.atan2(a[1]/a[0])

''' vectores complejos '''

def sumaVector(a,b):
    return [suma(a[i],b[i]) for i in range(len(a))]

def vectorInversoAd(a):
    return [(a[i][0]*-1,a[i][1]*-1) for i in range(len(a))]

def vectorPorEscalar(r,a):
    return [porEscalar(r,a[i]) for i in range(len(a))]

def conjugadoVector(a):
    return [conjugado(a[i]) for i in range(len(a))]

def productoInterno(a, b):
    if len(a) == len(b):
        res = (0, 0)
        for i in range(len(a)):
            res = suma(multiplicacion(a[i], b[i]),res)
        return res
    else: print("la dimension de los vectores es incorrecta")

'''matrices complejas'''

def sumaMatrices(a,b):
    return [sumaVector(a[i],b[i]) for i in range(len(a))]

def matrizInversoAd(a):
    return [[(a[i][j][0]*-1,a[i][j][1]*-1) for j in range(len(a[0]))] for i in range(len(a)) ]

def matrizPorEscalar(r,a):
    return [vectorPorEscalar(r,a[i]) for i in range(len(a))]

def transpuestaMatriz(a):
    return [[matriz[j][i] for j in range(len(a))] for i in range(len(a[0]))]

def conjugadoMatriz(a):
    return [conjugadoVector(a[i]) for i in range(len(a))]

def adjuntaMatriz(a):
    b = transpuestaMatriz(a)
    return conjugadoMatriz(b)

def multiplicacionMatriz(a, b):
    if len(a[0]) == len(b):
        filas = len(a)
        columnas = len(b[0])
        res = [[(0, 0) for i in range(columnas)] for j in range(filas)]
        for i in range(0, filas):
            for j in range(0, columnas):
                temp = (0,0)
                for k in range(0, len(b)):
                    temp = suma(temp,multiplicacion(a[i][k], b[k][j]))
                res[i][j] = temp
        return res
    else:
        print("las matrices no se pueden multiplicar")
        return False

























