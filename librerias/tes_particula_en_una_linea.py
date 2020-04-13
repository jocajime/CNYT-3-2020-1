import unittest
import particula_una_linea as p
class testPenUnaLinea(unittest.TestCase):
    
    def testProb(self):
        v = [(-3,-1),(0,-2),(0,1),(2,0)]
        self.assertEqual(p.prob_pos(v,2),0.05263157894736841)

    
if __name__ == '__main__':
    unittest.main()

