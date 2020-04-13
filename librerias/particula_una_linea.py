import cal_complejos as cal

def prob_pos(v,p):
    r1 = cal.modulo(v[p])**2
    r2 = cal.normaVectorial(v)**2
    return r1/r2

def valorEsperado(m,v):
    r1=cañ.matrizporvector_h(m,v)
    return cal.productoInterno(r1, v)


