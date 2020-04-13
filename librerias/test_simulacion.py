import unittest
import cal_complejos
import simulacion_cuantica as sim

class testSimulacion(unittest.TestCase):
    '''test simulacion cuantica'''
    def testRendijasReal(self):
        res = [(0.0, 0.0),(0.0, 0.0),(0.0, 0.0),(0.16666666666666666, 0.0),(0.16666666666666666, 0.0),(0.3333333333333333, 0.0),(0.16666666666666666, 0.0),(0.16666666666666666, 0.0)]    
        self.assertEqual(cal_complejos.transpuestaVector_v(sim.vector_final_real(2)),res)

    def testRendijasImaginario(self):
        res = [(0.0, 0.0),(0.0, 0.0),(0.0, 0.0),(-0.2886751345948129, 0.2886751345948129),(-0.2886751345948129, -0.2886751345948129),(0.0, 0.0),(-0.2886751345948129, -0.2886751345948129),(0.2886751345948129, -0.2886751345948129)]
        self.assertEqual(cal_complejos.transpuestaVector_v(sim.vector_final_imaginario(2)),res)

    def testSimulacion(self):
        sim.simular(2)

if __name__ == '__main__':
    unittest.main()
