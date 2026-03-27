import unittest

from moves import *
from analysis import *

class TestAnalysis(unittest.TestCase):
    def test_get_inverse(self):
        self.assertTrue(get_inverse("R") == "R'")
        self.assertTrue(get_inverse("R'") == "R")
        self.assertTrue(get_inverse("L") == "L'")
        self.assertTrue(get_inverse("L'") == "L")
        self.assertTrue(get_inverse("RLR'L'") == "LRL'R'")
    
    def testFixedRelativeTo(self):
        self.assertTrue(fixedRelativeTo(['A', 'B', 'C', 'D'], ['B', 'A', 'C', 'D']) == {'C', 'D'})

if __name__ == '__main__':
    unittest.main()
