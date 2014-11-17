import unittest
from gauss_newton import *
from factorizations import *
import math

class GaussNewtonTests(unittest.TestCase):
    
    def setUp(self):
        self.tolerance = 0.5

    def testQuadraticHouseHolder(self):
        result = gauss_newton('quadratic.txt', (1, 3, -1), 5, qr_fact_househ, quadratic_fit, quadratic_partial)
        self.checkAccuracy(result, (0.16, 2.0, 0.85))
   
    def testExponentialHouseHolder(self):
        result = gauss_newton('exponential.txt', (-0.3, 0.3, 0.3), 5, qr_fact_househ, exponential_fit, exponential_partial)
        self.checkAccuracy(result, (-0.2, 0.5, -0.07))

    def testLogarithmicHouseHolder(self):
        result = gauss_newton('logarithmic.txt', (-2, 10, 5), 5, qr_fact_househ, logarithmic_fit, logarithmic_partial)
        self.checkAccuracy(result, (-3.02, 7.8, 2.1))

    def testRationalHouseHolder(self):
        result = gauss_newton('rational.txt', (0.9, 0.2, 0.1) , 5, qr_fact_househ,rational_fit, rational_partial)
        print result
        self.checkAccuracy(result, (0.35, 0.85, 0.038))

    # Tests Using Givens Rotations
    def testQuadraticGivens(self):
        result = gauss_newton('quadratic.txt', (1, 3, -1), 5, qr_fact_givens, quadratic_fit, quadratic_partial)
        self.checkAccuracy(result, (0.16, 2.0, 0.85))

    def testExponentialGivens(self):
        result = gauss_newton('exponential.txt', (-0.3, 0.3, 0.3), 5, qr_fact_givens, exponential_fit, exponential_partial)
        self.checkAccuracy(result, (-0.2, 0.5, -0.07))

    def testLogarithmicGivens(self):
        result = gauss_newton('logarithmic.txt', (-2, 10, 5), 5, qr_fact_givens, logarithmic_fit, logarithmic_partial)
        self.checkAccuracy(result, (-3.02, 7.8, 2.1))

    def testRationalGivens(self):
        result = gauss_newton('rational.txt', (0.9, 0.2, 0.1) , 5, qr_fact_givens, rational_fit, rational_partial)
        print result
        self.checkAccuracy(result, (0.35, 0.85, 0.038))

    def checkAccuracy(self, output, expected):
        print 'expected {} got {}'.format(expected, output)
        for r , e in zip(output, expected):
            difference = abs(r) - abs(e)
            self.assertTrue(abs(difference) < self.tolerance)

if __name__ == '__main__':
    unittest.main()