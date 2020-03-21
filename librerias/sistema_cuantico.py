import cal_complejos as cal

def prob_pos_v(v,x):
    return cal.modulo(v[x][0])**2/cal.normaVectorial(cal.traspuestaVector_v(v))**2

def prob_pos_h(v,x):
    return cal.modulo(v[x])**2/cal.normaVectorial(v)**2

def main():
    v = [(-3,-1),(0,-2),(0,1),(2,0)]
    print(prob_pos_h(v,2))

main()
