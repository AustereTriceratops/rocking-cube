import unittest

from constants import *
from moves import *
from analysis import *

class TestEverything(unittest.TestCase):
    edges = [i for i in START_EDGES]

    def test_L(self):
        # LLL = I
        edges_cycled = L(L(L(self.edges)))
        self.assertTrue(self.edges == edges_cycled)

    def test_R(self):
        # RRR = I
        edges_cycled = R(R(R(self.edges)))
        self.assertTrue(self.edges == edges_cycled)

    def test_inverse_moves(self):
        # R'R = I
        self.assertTrue(R(RInv(self.edges)) == self.edges)

        # RR' = I
        self.assertTrue(RInv(R(self.edges)) == self.edges)

        # L'L = I
        self.assertTrue(L(LInv(self.edges)) == self.edges)

        # LL' = I
        self.assertTrue(LInv(L(self.edges)) == self.edges)
    
    def test_squared_moves(self):
        # RR = R'
        self.assertTrue(R(R(self.edges)) == RInv(self.edges))

        # LL = L'
        self.assertTrue(L(L(self.edges)) == LInv(self.edges))
    
    def test_fixed_edges(self):
        # R and R' leave GRd and BOd fixed
        self.assertTrue(fixedRelativeTo(self.edges, R(self.edges)) == {'GRd', 'BOd'})
        self.assertTrue(fixedRelativeTo(self.edges, RInv(self.edges)) == {'GRd', 'BOd'})

        # L and L' leave GRu and BOu fixed
        self.assertTrue(fixedRelativeTo(self.edges, L(self.edges)) == {'GRu', 'BOu'})
        self.assertTrue(fixedRelativeTo(self.edges, LInv(self.edges)) == {'GRu', 'BOu'})
    
    def test_move_parser(self):
        self.assertTrue(parseMoves("R'R") == self.edges)
        self.assertTrue(parseMoves("RR'") == self.edges)
        self.assertTrue(parseMoves("L'L") == self.edges)
        self.assertTrue(parseMoves("LL'") == self.edges)
        self.assertTrue(parseMoves("LLL") == self.edges)
        self.assertTrue(parseMoves("RRR") == self.edges)

        self.assertTrue(parseMoves("RLR'L'") == LInv(RInv(L(R(self.edges)))))
        self.assertTrue(parseMoves("R'LRL'R'L") == L(RInv(LInv(R(L(RInv(self.edges)))))))


if __name__ == '__main__':
    unittest.main()
