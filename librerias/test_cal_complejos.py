import unittest
import cal_complejos


class testNumerosComplejosCal(unittest.TestCase):
    
    def testSuma(self):
        a = (12,11)
        b = (20,3.5)
        self.assertEqual(cal_complejos.suma(a,b),(32,14.5))
        self.assertFalse(cal_complejos.suma(a,b)==(50,14.5))

    def testResta(self):
        a = (12,11)
        b = (20,3.5)
        self.assertEqual(cal_complejos.resta(a,b),(-8,7.5))        
        self.assertFalse(cal_complejos.resta(a,b)==(23,14.5))
        
    def testEscalar(self):
        a = (12,11)
        self.assertEqual(cal_complejos.porEscalar(5,a),(60,55))

        self.assertFalse(cal_complejos.porEscalar(5,a)==(30,14.5))
        
    def testMult(self):
        a = (12,11)
        b = (20,3.5)
        self.assertEqual(cal_complejos.multiplicacion(a,b),(201.5,262))

        self.assertFalse(cal_complejos.multiplicacion(a,b)==(200,565))

    def testDiv(self):
        a = (12,11)
        b = (20,3.5)
        self.assertEqual(cal_complejos.division(a,b),(0.6755609460278957,0.4317768344451183))
        
        self.assertFalse(cal_complejos.division(a,b)==(0.626,0.2626))
        
    def testDiv(self):
        a = (12,11)
        b = (20,3.5)
        self.assertEqual(cal_complejos.division(a,b),(0.6755609460278957,0.4317768344451183))

        self.assertFalse(cal_complejos.division(a,b)==(0.626,0.2626))
        
    def testModulo(self):
        a = (12,11)
        self.assertEqual(cal_complejos.modulo(a),16.278820596099706)
        
        self.assertFalse(cal_complejos.modulo(a)==26)

    def testConjugado(self):
        a = (12,11)
        self.assertEqual(cal_complejos.conjugado(a),(12,-11))
        
        self.assertFalse(cal_complejos.conjugado(a)==(12,11))

    def testPolar(self):
        a = (12,11)
        self.assertEqual(cal_complejos.aPolar(a),(16.278820596099706,0.7419472680059175))
        self.assertFalse(cal_complejos.aPolar(a)==(12,11))
        
        
    def testPrint(self):
        a = (12,11)
        self.assertEqual(cal_complejos.prettyPrint(a),"12+11i")
        
        self.assertFalse(cal_complejos.aPolar(a)=="12-11i")


        

    def testTensor(self):
        h = [[(1/(2**0.5),0),(1/(2**0.5),0)],[(1/(2**0.5),0),(1/(2**0.5)*-1,0)]]
        x = [[(0,0),(1,0)],[(1,0),(0,0)]]    
        c = cal_complejos.tensorMatrices(h,x)
        self.assertEqual(c,[[(0.0, 0.0), (0.7071067811865475, 0.0), (0.0, 0.0), (0.7071067811865475, 0.0)], [(0.7071067811865475, 0.0), (0.0, 0.0), (0.7071067811865475, 0.0), (0.0, 0.0)], [(0.0, 0.0), (0.7071067811865475, 0.0), (-0.0, 0.0), (-0.7071067811865475, 0.0)], [(0.7071067811865475, 0.0), (0.0, 0.0), (-0.7071067811865475, 0.0), (-0.0, 0.0)]])
        
    '''test vectores'''
    def testSumaV(self):
        a = [(12,31),(15,31),(19,64)]
        b = [(15,41),(65,13),(46,49)]
        self.assertEqual(cal_complejos.sumaVector(a,b),[(27, 72), (80, 44), (65, 113)])

    def testInversoAdVector(self):
        a = [(12,31),(15,31),(19,64)]
        self.assertEqual(cal_complejos.vectorInversoAd(a),[(-12, -31), (-15, -31), (-19, -64)])

    def testVectorPorEscalar(self):
        a = [(12,31),(15,31),(19,64)]
        self.assertEqual(cal_complejos.vectorPorEscalar(5,a),[(60, 155), (75, 155), (95, 320)])

    def testConjugadoVector(self):
        a = [(12,31),(15,31),(19,64)]
        self.assertEqual(cal_complejos.conjugadoVector(a),[(12, -31), (15, -31), (19, -64)])

    def testProductoInterno(self):
        a = [(12,31),(15,31),(19,64)]
        b = [(15,41),(65,13),(46,49)]
        self.assertEqual(cal_complejos.productoInterno(a,b),(-2781, 7042))
  
    
        

if __name__ == '__main__':
    unittest.main()
