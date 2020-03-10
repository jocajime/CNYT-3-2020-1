import matplotlib.pyplot as plt
import simulacion_cuantica as sim
import cal_complejos as cal


def simular(clicks):
    v = sim.vector_final_imaginario(clicks)
    v = cal.transpuestaMatriz(v)
    a = [cal.modulo(v[0][i]) for i in range(len(v[0]))]
    x1 = [i for i in range(len(a))]
    plt.bar(x1,a, label = 'probabilidad', width = 0.5, color = 'blue')
    plt.ylabel('probabilidad')
    plt.title('Evolucion del sistema '+str(clicks)+' clicks')
    plt.legend()
    plt.savefig("simulacion.png")



simular(2)


    
    
