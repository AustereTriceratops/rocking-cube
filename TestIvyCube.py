import unittest

from constants import *
from moves import *
from analysis import *

class TestIvyCube(unittest.TestCase):
    edges = [i for i in START_EDGES_IVY]

    def test_basic_moves(self):
        # TTT = I
        edges_cycled = T(T(T(self.edges)))
        self.assertTrue(self.edges == edges_cycled)
        
        # FFF = I
        edges_cycled = F(F(F(self.edges)))
        self.assertTrue(self.edges == edges_cycled)
        
        # BLBLBL = I
        edges_cycled = BL(BL(BL(self.edges)))
        self.assertTrue(self.edges == edges_cycled)
        
        # BRBRBR = I
        edges_cycled = BR(BR(BR(self.edges)))
        self.assertTrue(self.edges == edges_cycled)

    def test_inverse_moves(self):
        # T'T = I
        self.assertTrue(T(TInv(self.edges)) == self.edges)

        # TT' = I
        self.assertTrue(TInv(T(self.edges)) == self.edges)
        
        # F'F = I
        self.assertTrue(F(FInv(self.edges)) == self.edges)

        # FF' = I
        self.assertTrue(FInv(F(self.edges)) == self.edges)
        
         # BL'BL = I
        self.assertTrue(BL(BLInv(self.edges)) == self.edges)

        # BLBL' = I
        self.assertTrue(BLInv(BL(self.edges)) == self.edges)
        
         # BR'BR = I
        self.assertTrue(BR(BRInv(self.edges)) == self.edges)

        # BRBR' = I
        self.assertTrue(BRInv(BR(self.edges)) == self.edges)
    
    def test_squared_moves(self):
        # TT = T'
        self.assertTrue(T(T(self.edges)) == TInv(self.edges))

        # FF = F'
        self.assertTrue(F(F(self.edges)) == FInv(self.edges))
        
        # BLBL = BL'
        self.assertTrue(BL(BL(self.edges)) == BLInv(self.edges))
        
        # BRBR = BR'
        self.assertTrue(BR(BR(self.edges)) == BRInv(self.edges))
    
    def test_fixed_edges(self):
        self.assertTrue(fixedRelativeTo(self.edges, T(self.edges)) == {"W", "G", "O"})
        self.assertTrue(fixedRelativeTo(self.edges, TInv(self.edges)) == {"W", "G", "O"})

if __name__ == '__main__':
    unittest.main()
