from sys import stdin
import math

#suma dos numeros complejos representados por una tupla, y retorna un numero complejo representado por una tupla
def suma(a,b):
    return (a[0]+b[0],a[1]+b[1])

#resta dos numeros complejos representados por una tupla, y retorna un numero complejo representado por una tupla
def resta(a,b):
    return (a[0]-b[0],a[1]-b[1])

#multiplica dos numeros complejos representados por una tupla, y retorna un numero complejo representado por una tupla
def multiplicacion(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])

#divide dos numeros complejos representados por una tupla, y retorna un numero complejo representado por una tupla
def division(a,b):
    return ((a[0]*b[0]+a[1]*b[1])/(b[0]**2+b[1]**2),(a[1]*b[0]-a[0]*b[1])/(b[0]**2+b[1]**2))

#multiplica un numero complejo representado por una tupla con un numero escalar, y retorna un numero complejo representado por una tupla
def porEscalar(r,a):
    return (r*a[0],r*a[1])

#retorna el modulo de un numero complejo representado por una tupla
def modulo(a):
    return ((a[0]**2)+(a[1]**2))**0.5

#retorna el conjugado de un numero complejo representado por una tupla
def conjugado(a):
    return (a[0],a[1]*-1)

#recibe un numero complejo y retorna el mismo en coordenadas polares
def aPolar(a):
    return (modulo(a),math.atan(a[1]/a[0]))

#retorna la phase de un numero complejo
def phase(a):
    return math.atan2(a[1],a[0])

#imprime un numero complejo 
def prettyPrint(a):
    if a[1] < 0:
        return ""+str(a[0])+str(a[1])+"i"
    else:
        
        return ""+str(a[0])+"+"+str(a[1])+"i"

''' vectores complejos '''

def sumaVector(a,b):
    return [suma(a[i],b[i]) for i in range(len(a))]

def restaVector(a,b):
    return [resta(a[i],b[i]) for i in range(len(a))]

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

def normaVectorial(a):
    res = 0
    for i in a:
        res += modulo(i)**2
    return res**0.5

def distanciaVectores(a,b):
    temp = 0
    for i in range(len(a)):
        temp += (a[i] - b[i])**2
    return (temp)**0.5

def productoEscalar(a,b):
    temp = (0,0)
    for i in range(len(a[0])):
        temp = suma(temp,multiplicacion(a[0][i],b[0][i]))
    return temp

def transpuestaVector_h(a):
    return [[a[i]] for i in range(len(a))]

def transpuestaVector_v(a):
    return [a[i][0] for i in range(len(a))]

'''matrices complejas'''

def sumaMatrices(a,b):
    return [sumaVector(a[i],b[i]) for i in range(len(a))]

def restaMatrices(a,b):
    return [restaVector(a[i],b[i]) for i in range(len(a))]

def matrizInversoAd(a):
    return [vectorInversoAd(a[i]) for i in range(len(a))]

def matrizPorEscalar(r,a):
    return [vectorPorEscalar(r,a[i]) for i in range(len(a))]

def transpuestaMatriz(a):
    return [
        [a[j][i] for j in range(len(a))] for i in range(len(a[0]))]

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
def matrizporvector_h(a,v):
    return multiplicacionMatriz(a, transpuestaVector_h(v))

def matrizporvector_v(a,v):
    return multiplicacionMatriz(a,v)


def matrizHermitania(a):
    if len(a) == len(a[0]):
        temp = transpuestaMatriz(a)
        temp = conjugadoMatriz(temp)
        if temp == a: return True
        else: return False
    else:
        print("no es una matriz cuadrada")
        return False

def matrizUnitaria(a):
    if len(a) == len(a[0]):
        temp = transpuestaMatriz(a)
        temp = conjugadoMatriz(temp)
        c = multiplicacionMatriz(a,temp)
        d= multiplicacionMatriz(temp,a)
        if c == d: return True
        else: return False
    else:
        print("no es una matriz cuadrada")
        return False


def tensorMatrices(a,b):
    res=[]
    for i in range(len(a)):
        for j in range(len(b)):
            c = []
            for x in range(len(a[i])):
                for y in range(len(b[j])): c.append(multiplicacion(a[i][x], b[j][y]))
            res.append(c)
           
    return res

def imprimir_matriz(a):
    for i in range(len(a)):
        print(a[i])


















