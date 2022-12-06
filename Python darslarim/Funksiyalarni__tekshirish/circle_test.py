 import unittest
from circle import getArea,getPerimetr

class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(5), 78.53975,3)
        self.assertAlmostEqual(getArea(10), 314.159)
        
        
        
    def test_perimetr(self):
        self.assertAlmostEqual(getArea(10),62,8318,3)
        self.assertAlmostEqual(getArea(4),25.13272)
        
unittest.main()