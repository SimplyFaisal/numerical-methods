import unittest
from gauss_newton import *
import math

class GaussNewtonTests(unittest.TestCase):
    
    def setUp(self):
        self.tolerance = 0.5

    def testQuadratic(self):
        result = gauss_newton('quadratic.txt', (1, 3, -1), 5, quadratic_fit, quadratic_partial)
        self.checkAccuracy(result, (0.16, 2.0, 0.85))
   
    def testExponential(self):
        result = gauss_newton('exponential.txt', (-0.3, 0.3, 0.3), 5, exponential_fit, exponential_partial)
        self.checkAccuracy(result, (-0.2, 0.5, -0.07))

    def testLogarithmic(self):
        result = gauss_newton('logarithmic.txt', (-2, 10, 5), 5, logarithmic_fit, logarithmic_partial)
        self.checkAccuracy(result, (-3.02, 7.8, 2.1))

    def testRational(self):
        result = gauss_newton('rational.txt', (0.9, 0.2, 0.1) , 5, rational_fit, rational_partial)
        print result
        self.checkAccuracy(result, (0.35, 0.85, 0.038))

    def checkAccuracy(self, output, expected):
        for r , e in zip(output, expected):
            difference = abs(r) - abs(e)
            self.assertTrue(abs(difference) < self.tolerance)

if __name__ == '__main__':
    unittest.main()