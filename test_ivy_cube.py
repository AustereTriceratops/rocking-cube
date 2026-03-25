import unittest

from IvyCube import IvyCube
from analysis import fixedRelativeTo

class TestIvyCube(unittest.TestCase):
    def test_basic_moves(self):
        # UUU = I
        iv = IvyCube().U().U().U()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)
        
        # DDD = I
        iv = IvyCube().D().D().D()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)
        
        # LLL = I
        iv = IvyCube().L().L().L()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)
        
        # RRR = I
        iv = IvyCube().R().R().R()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)

    def test_inverse_moves(self):
        # U'U = I
        iv = IvyCube().UInv().U()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)

        # UU' = I
        iv = IvyCube().U().UInv()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)
        
        # D'D = I
        iv = IvyCube().DInv().D()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)

        # DD' = I
        iv = IvyCube().D().DInv()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)
        
         # L'L = I
        iv = IvyCube().LInv().L()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)

        # LL' = I
        iv = IvyCube().L().LInv()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)
        
         # R'R = I
        iv = IvyCube().RInv().R()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)

        # RR' = I
        iv = IvyCube().R().RInv()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)
    
    def test_squared_moves(self):
        # UU = U'
        self.assertTrue(IvyCube().U().U().edges == IvyCube().UInv().edges)

        # DD = D'
        self.assertTrue(IvyCube().D().D().edges == IvyCube().DInv().edges)
        
        # LL = L'
        self.assertTrue(IvyCube().L().L().edges == IvyCube().LInv().edges)
        
        # RR = R'
        self.assertTrue(IvyCube().R().R().edges == IvyCube().RInv().edges)
    
    def test_fixed_edges(self):
        self.assertTrue(fixedRelativeTo(IvyCube().edges, IvyCube().U().edges) == {"W", "G", "O"})
        self.assertTrue(fixedRelativeTo(IvyCube().edges, IvyCube().UInv().edges) == {"W", "G", "O"})
        
        self.assertTrue(fixedRelativeTo(IvyCube().edges, IvyCube().D().edges) == {"Y", "R", "G"})
        self.assertTrue(fixedRelativeTo(IvyCube().edges, IvyCube().DInv().edges) == {"Y", "R", "G"})
        
        self.assertTrue(fixedRelativeTo(IvyCube().edges, IvyCube().L().edges) == {"B", "R", "W"})
        self.assertTrue(fixedRelativeTo(IvyCube().edges, IvyCube().LInv().edges) == {"B", "R", "W"})
        
        self.assertTrue(fixedRelativeTo(IvyCube().edges, IvyCube().R().edges) == {"O", "Y", "B"})
        self.assertTrue(fixedRelativeTo(IvyCube().edges, IvyCube().RInv().edges) == {"O", "Y", "B"})

if __name__ == '__main__':
    unittest.main()
