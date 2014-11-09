import unittest
import power_method
import math

class PowerMethodTests(unittest.TestCase):

    def setUp(self):
        self.A = [[3, 4], [3, 1]]

    def testPowerMethod(self):
        # expected value
        eigenvalue = 2 + math.sqrt(13)

        # tolerance
        e = 0.00005

        result = power_method.power_method(self.A, [1,1], e, 20)
        self.assertTrue(result)
        self.assertTrue(abs(result['value'] - eigenvalue) <= e)
        self.assertTrue(result['iterations'] < 20)

if __name__ == '__main__':
    unittest.main()