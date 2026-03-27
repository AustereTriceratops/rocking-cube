import unittest

from IvyCube import IvyCube
from analysis import fixedRelativeTo

class TestIvyCube(unittest.TestCase):
    def test_basic_moves(self):
        # UUU = I
        iv = IvyCube().U().U().U()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)
        self.assertTrue(iv.corner_parity['U'] % 3 == 0)
        self.assertTrue(iv.corner_parity['R'] == 0)
        self.assertTrue(iv.corner_parity['D'] == 0)
        self.assertTrue(iv.corner_parity['L'] == 0)
        
        
        # DDD = I
        iv = IvyCube().D().D().D()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)
        self.assertTrue(iv.corner_parity['D'] % 3 == 0)
        self.assertTrue(iv.corner_parity['U'] == 0)
        self.assertTrue(iv.corner_parity['R'] == 0)
        self.assertTrue(iv.corner_parity['L'] == 0)
        
        # LLL = I
        iv = IvyCube().L().L().L()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)
        self.assertTrue(iv.corner_parity['L'] % 3 == 0)
        self.assertTrue(iv.corner_parity['U'] == 0)
        self.assertTrue(iv.corner_parity['D'] == 0)
        self.assertTrue(iv.corner_parity['R'] == 0)
        
        # RRR = I
        iv = IvyCube().R().R().R()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)
        self.assertTrue(iv.corner_parity['R'] % 3 == 0)
        self.assertTrue(iv.corner_parity['U'] == 0)
        self.assertTrue(iv.corner_parity['D'] == 0)
        self.assertTrue(iv.corner_parity['L'] == 0)

    def test_inverse_moves(self):
        # U'U = I
        iv = IvyCube().UInv().U()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)
        self.assertTrue(iv.corner_parity['L'] == 0)
        self.assertTrue(iv.corner_parity['R'] == 0)
        self.assertTrue(iv.corner_parity['U'] == 0)
        self.assertTrue(iv.corner_parity['D'] == 0)

        # UU' = I
        iv = IvyCube().U().UInv()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)
        self.assertTrue(iv.corner_parity['L'] == 0)
        self.assertTrue(iv.corner_parity['R'] == 0)
        self.assertTrue(iv.corner_parity['U'] == 0)
        self.assertTrue(iv.corner_parity['D'] == 0)
        
        # D'D = I
        iv = IvyCube().DInv().D()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)
        self.assertTrue(iv.corner_parity['L'] == 0)
        self.assertTrue(iv.corner_parity['R'] == 0)
        self.assertTrue(iv.corner_parity['U'] == 0)
        self.assertTrue(iv.corner_parity['D'] == 0)

        # DD' = I
        iv = IvyCube().D().DInv()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)
        self.assertTrue(iv.corner_parity['L'] == 0)
        self.assertTrue(iv.corner_parity['R'] == 0)
        self.assertTrue(iv.corner_parity['U'] == 0)
        self.assertTrue(iv.corner_parity['D'] == 0)
        
         # L'L = I
        iv = IvyCube().LInv().L()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)
        self.assertTrue(iv.corner_parity['L'] == 0)
        self.assertTrue(iv.corner_parity['R'] == 0)
        self.assertTrue(iv.corner_parity['U'] == 0)
        self.assertTrue(iv.corner_parity['D'] == 0)

        # LL' = I
        iv = IvyCube().L().LInv()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)
        self.assertTrue(iv.corner_parity['L'] == 0)
        self.assertTrue(iv.corner_parity['R'] == 0)
        self.assertTrue(iv.corner_parity['U'] == 0)
        self.assertTrue(iv.corner_parity['D'] == 0)
        
         # R'R = I
        iv = IvyCube().RInv().R()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)
        self.assertTrue(iv.corner_parity['L'] == 0)
        self.assertTrue(iv.corner_parity['R'] == 0)
        self.assertTrue(iv.corner_parity['U'] == 0)
        self.assertTrue(iv.corner_parity['D'] == 0)

        # RR' = I
        iv = IvyCube().R().RInv()
        self.assertTrue(iv.edges == IvyCube.START_EDGES)
        self.assertTrue(iv.corner_parity['L'] == 0)
        self.assertTrue(iv.corner_parity['R'] == 0)
        self.assertTrue(iv.corner_parity['U'] == 0)
        self.assertTrue(iv.corner_parity['D'] == 0)
    
    def test_squared_moves(self):
        # UU = U'
        iv1 = IvyCube().U().U()
        iv2 = IvyCube().UInv()
        self.assertTrue(iv1.edges == iv2.edges)
        self.assertTrue(iv1.corner_parity['U'] % 3 == iv2.corner_parity['U'] % 3)
        
        # U'U' = U
        iv1 = IvyCube().U()
        iv2 = IvyCube().UInv().UInv()
        self.assertTrue(iv1.edges == iv2.edges)
        self.assertTrue(iv1.corner_parity['U'] % 3 == iv2.corner_parity['U'] % 3)

        # DD = D'
        iv1 = IvyCube().D().D()
        iv2 = IvyCube().DInv()
        self.assertTrue(iv1.edges == iv2.edges)
        self.assertTrue(iv1.corner_parity['D'] % 3 == iv2.corner_parity['D'] % 3)
        
        # D'D' = D
        iv1 = IvyCube().D()
        iv2 = IvyCube().DInv().DInv()
        self.assertTrue(iv1.edges == iv2.edges)
        self.assertTrue(iv1.corner_parity['D'] % 3 == iv2.corner_parity['D'] % 3)
        
        # LL = L'
        iv1 = IvyCube().L().L()
        iv2 = IvyCube().LInv()
        self.assertTrue(iv1.edges == iv2.edges)
        self.assertTrue(iv1.corner_parity['L'] % 3 == iv2.corner_parity['L'] % 3)
        
        # L'L' = L
        iv1 = IvyCube().L()
        iv2 = IvyCube().LInv().LInv()
        self.assertTrue(iv1.edges == iv2.edges)
        self.assertTrue(iv1.corner_parity['L'] % 3 == iv2.corner_parity['L'] % 3)
        
        # RR = R'
        iv1 = IvyCube().R().R()
        iv2 = IvyCube().RInv()
        self.assertTrue(iv1.edges == iv2.edges)
        self.assertTrue(iv1.corner_parity['R'] % 3 == iv2.corner_parity['R'] % 3)
        
        # R'R' = R
        iv1 = IvyCube().R()
        iv2 = IvyCube().RInv().RInv()
        self.assertTrue(iv1.edges == iv2.edges)
        self.assertTrue(iv1.corner_parity['R'] % 3 == iv2.corner_parity['R'] % 3)
    
    def test_fixed_edges(self):
        self.assertTrue(fixedRelativeTo(IvyCube().edges, IvyCube().U().edges) == {"W", "G", "O"})
        self.assertTrue(fixedRelativeTo(IvyCube().edges, IvyCube().UInv().edges) == {"W", "G", "O"})
        
        self.assertTrue(fixedRelativeTo(IvyCube().edges, IvyCube().D().edges) == {"Y", "R", "G"})
        self.assertTrue(fixedRelativeTo(IvyCube().edges, IvyCube().DInv().edges) == {"Y", "R", "G"})
        
        self.assertTrue(fixedRelativeTo(IvyCube().edges, IvyCube().L().edges) == {"B", "R", "W"})
        self.assertTrue(fixedRelativeTo(IvyCube().edges, IvyCube().LInv().edges) == {"B", "R", "W"})
        
        self.assertTrue(fixedRelativeTo(IvyCube().edges, IvyCube().R().edges) == {"O", "Y", "B"})
        self.assertTrue(fixedRelativeTo(IvyCube().edges, IvyCube().RInv().edges) == {"O", "Y", "B"})
    
    def test_move_parser(self):
        self.assertTrue(IvyCube.parseMoves("LLL").edges == IvyCube().edges)
        self.assertTrue(IvyCube.parseMoves("L'L").edges == IvyCube().edges)
        self.assertTrue(IvyCube.parseMoves("LL'").edges == IvyCube().edges)
        
        self.assertTrue(IvyCube.parseMoves("RRR").edges == IvyCube().edges)
        self.assertTrue(IvyCube.parseMoves("R'R").edges == IvyCube().edges)
        self.assertTrue(IvyCube.parseMoves("RR'").edges == IvyCube().edges)
        
        self.assertTrue(IvyCube.parseMoves("UUU").edges == IvyCube().edges)
        self.assertTrue(IvyCube.parseMoves("U'U").edges == IvyCube().edges)
        self.assertTrue(IvyCube.parseMoves("UU'").edges == IvyCube().edges)
        
        self.assertTrue(IvyCube.parseMoves("DDD").edges == IvyCube().edges)
        self.assertTrue(IvyCube.parseMoves("D'D").edges == IvyCube().edges)
        self.assertTrue(IvyCube.parseMoves("DD'").edges == IvyCube().edges)

        self.assertTrue(IvyCube.parseMoves("RLR'L'").edges == IvyCube().R().L().RInv().LInv().edges)
        self.assertTrue(IvyCube.parseMoves("UDU'D'").edges == IvyCube().U().D().UInv().DInv().edges)
        self.assertTrue(IvyCube.parseMoves("RUDULR").edges == IvyCube().R().U().D().U().L().R().edges)
        self.assertTrue(IvyCube.parseMoves("R'LRL'R'L").edges == IvyCube().RInv().L().R().LInv().RInv().L().edges)

if __name__ == '__main__':
    unittest.main()
