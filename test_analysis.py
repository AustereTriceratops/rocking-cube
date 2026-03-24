import unittest

from constants import *
from moves import *
from analysis import *

class TestAnalysis(unittest.TestCase):
    edges = [i for i in START_EDGES_IVY]

    def test_get_inverse(self):

        self.assertTrue(get_inverse("R") == "R'")
        self.assertTrue(get_inverse("R'") == "R")
        self.assertTrue(get_inverse("L") == "L'")
        self.assertTrue(get_inverse("L'") == "L")
        self.assertTrue(get_inverse("RLR'L'") == "LRL'R'")

if __name__ == '__main__':
    unittest.main()
