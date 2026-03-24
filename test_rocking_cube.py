import unittest

from RockingCube import RockingCube
from analysis import fixedRelativeTo

class TestEverything(unittest.TestCase):
    rc = RockingCube() # TODO: should probably remove
    
    def setUp(self):
        self.rc.reset()

    def test_L(self):
        # LLL = I
        self.rc.L().L().L()
        self.assertTrue(self.rc.edges == self.rc.START_EDGES)

    def test_R(self):
        # RRR = I
        self.rc.R().R().R()
        self.assertTrue(self.rc.edges == self.rc.START_EDGES)

    def test_inverse_moves(self):
        # R'R = I
        self.rc.RInv().R()
        self.assertTrue(self.rc.edges == self.rc.START_EDGES)
        self.assertTrue(self.rc.corner_parity['L'] == 0)
        self.assertTrue(self.rc.corner_parity['R'] == 0)

        # RR' = I
        self.rc.R().RInv()
        self.assertTrue(self.rc.edges == self.rc.START_EDGES)
        self.assertTrue(self.rc.corner_parity['L'] == 0)
        self.assertTrue(self.rc.corner_parity['R'] == 0)

        # L'L = I
        self.rc.LInv().L()
        self.assertTrue(self.rc.edges == self.rc.START_EDGES)
        self.assertTrue(self.rc.corner_parity['L'] == 0)
        self.assertTrue(self.rc.corner_parity['R'] == 0)

        # LL' = I
        self.rc.L().LInv()
        self.assertTrue(self.rc.edges == self.rc.START_EDGES)
        self.assertTrue(self.rc.corner_parity['L'] == 0)
        self.assertTrue(self.rc.corner_parity['R'] == 0)
    
    def test_squared_moves(self):
        # RR = R'
        rc1 = RockingCube().R().R()
        rc2 = RockingCube().RInv()
        self.assertTrue(rc1.edges == rc2.edges)
        self.assertTrue(rc1.corner_parity['L'] == 0)
        self.assertTrue(rc1.corner_parity['R'] % 3 == 2)
        self.assertTrue(rc1.corner_parity['R'] % 3 == rc2.corner_parity['R'] % 3)

        # LL = L'
        rc1 = RockingCube().L().L()
        rc2 = RockingCube().LInv()
        self.assertTrue(rc1.edges == rc2.edges)
        self.assertTrue(rc1.corner_parity['R'] == 0)
        self.assertTrue(rc1.corner_parity['L'] % 3 == 2)
        self.assertTrue(rc1.corner_parity['L'] % 3 == rc2.corner_parity['L'] % 3)
        
        # R'R' = R
        rc1 = RockingCube().RInv().RInv()
        rc2 = RockingCube().R()
        self.assertTrue(rc1.edges == rc2.edges)
        self.assertTrue(rc1.corner_parity['L'] == 0)
        self.assertTrue(rc1.corner_parity['R'] % 3 == 1)
        self.assertTrue(rc1.corner_parity['R'] % 3 == rc2.corner_parity['R'] % 3)

        # L'L' = L
        rc1 = RockingCube().LInv().LInv()
        rc2 = RockingCube().L()
        self.assertTrue(rc1.edges == rc2.edges)
        self.assertTrue(rc1.corner_parity['R'] == 0)
        self.assertTrue(rc1.corner_parity['L'] % 3 == 1)
        self.assertTrue(rc1.corner_parity['L'] % 3 == rc2.corner_parity['L'] % 3)
    
    def test_fixed_edges(self):
        # R and R' leave GRl and BOl fixed
        self.assertTrue(fixedRelativeTo(RockingCube().edges, RockingCube().R().edges) == {'GRl', 'BOl'})
        self.assertTrue(fixedRelativeTo(RockingCube().edges, RockingCube().RInv().edges) == {'GRl', 'BOl'})

        # L and L' leave GRr and BOr fixed
        self.assertTrue(fixedRelativeTo(RockingCube().edges, RockingCube().L().edges) == {'GRr', 'BOr'})
        self.assertTrue(fixedRelativeTo(RockingCube().edges, RockingCube().LInv().edges) == {'GRr', 'BOr'})
    
    def test_move_parser(self):
        self.assertTrue(RockingCube.parseMoves("R'R").edges == self.rc.edges)
        self.assertTrue(RockingCube.parseMoves("RR'").edges == self.rc.edges)
        self.assertTrue(RockingCube.parseMoves("L'L").edges == self.rc.edges)
        self.assertTrue(RockingCube.parseMoves("LL'").edges == self.rc.edges)
        self.assertTrue(RockingCube.parseMoves("LLL").edges == self.rc.edges)
        self.assertTrue(RockingCube.parseMoves("RRR").edges == self.rc.edges)

        self.assertTrue(RockingCube.parseMoves("RLR'L'").edges == self.rc.R().L().RInv().LInv().edges)
        self.rc.reset()
        self.assertTrue(RockingCube.parseMoves("R'LRL'R'L").edges == self.rc.RInv().L().R().LInv().RInv().L().edges)
    
    def test_move_parser_on_existing_permutation(self):
        self.assertTrue(RockingCube.parseMoves("LL", RockingCube.parseMoves("L")).edges == self.rc.edges)
        self.assertTrue(RockingCube.parseMoves("L'", RockingCube.parseMoves("L")).edges == self.rc.edges)
    
    def test_permutation_order(self):
        self.assertTrue(RockingCube.permutationOrder("L") == 3)
        self.assertTrue(RockingCube.permutationOrder("L'") == 3)
        self.assertTrue(RockingCube.permutationOrder("R") == 3)
        self.assertTrue(RockingCube.permutationOrder("R'") == 3)
        
        self.assertTrue(RockingCube.permutationOrder("RLR'L'") == 7)
        self.assertTrue(RockingCube.permutationOrder("L'R'L'RLR'") == 3)
        self.assertTrue(RockingCube.permutationOrder("RLR'LRL'") == 2)
        self.assertTrue(RockingCube.permutationOrder("RL'R'LRLRL'") == 6)

    def test_exhaustive_move_generation(self):
        generated_moves_0 = RockingCube.generate_all_moves_of_len(0)
        self.assertTrue(generated_moves_0 == set())
        
        generated_moves_1 = RockingCube.generate_all_moves_of_len(1)
        self.assertTrue(generated_moves_1 == {"L", "L'", "R", "R'"})
        
        generated_moves_2 = RockingCube.generate_all_moves_of_len(2)
        self.assertTrue(generated_moves_2 == {"LR", "L'R", "RL", "R'L", "LR'", "L'R'", "RL'", "R'L'"})
        
        generated_moves_4 = RockingCube.generate_all_moves_of_len(4)
        self.assertTrue(len(generated_moves_4) == 32)
    
    def test_oriented_move_generation(self):
        generated_moves_0 = RockingCube.generate_all_moves_of_len(0, oriented=True)
        self.assertTrue(generated_moves_0 == set())
        
        generated_moves_1 = RockingCube.generate_all_moves_of_len(1, oriented=True)
        self.assertTrue(generated_moves_1 == set())
        
        generated_moves_2 = RockingCube.generate_all_moves_of_len(2, oriented=True)
        self.assertTrue(generated_moves_2 == set())
        
        generated_moves_4 = RockingCube.generate_all_moves_of_len(4, oriented=True)
        self.assertTrue(generated_moves_4 == {
            "LRL'R'", "LR'L'R", "L'RLR'", "L'R'LR", "RL'R'L", "R'L'RL", "RLR'L'", "R'LRL'"
        })
        
        generated_moves_5 = RockingCube.generate_all_moves_of_len(5, oriented=True)
        self.assertTrue(generated_moves_5 == {
            "LRLR'L", "LR'LRL", "RLRL'R", "RL'RLR", "L'RL'R'L'", "L'R'L'RL'", "R'LR'L'R'", "R'L'R'LR'"
        })
        
        generated_moves_6 = RockingCube.generate_all_moves_of_len(6, oriented=True)
        self.assertTrue(generated_moves_6 == {
            "LRLRLR", "LR'LR'LR'", "L'RL'RL'R", "L'R'L'R'L'R'", "RLRLRL", "RL'RL'RL'", "R'LR'LR'L", "R'L'R'L'R'L'"
        })
    
    def test_oriented_solution_generation(self):
        edges = [
            'WR', 'BOr', 'GRr', 'YB', 'GRl', 'WB', 'YG', 
            'YR', 'WG', 'WO', 'BOl', 'YO', 'BR', 'GO'
        ]

        rc = RockingCube(edges)

        solutions = rc.generate_solutions()
        
        self.assertTrue("R'L'RLRL'R'LRLR'L'R'L'RL" in solutions)

if __name__ == '__main__':
    unittest.main()
