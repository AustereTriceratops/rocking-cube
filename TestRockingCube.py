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
    
    def test_move_parser_on_existing_permutation(self):
        permuted_edges = parseMoves("L")

        self.assertTrue(parseMoves("LL", permuted_edges) == self.edges)
        self.assertTrue(parseMoves("L'", permuted_edges) == self.edges)
    
    def test_permutation_order(self):
        self.assertTrue(permutationOrder("L") == 3)
        self.assertTrue(permutationOrder("L'") == 3)
        self.assertTrue(permutationOrder("R") == 3)
        self.assertTrue(permutationOrder("R'") == 3)
        
        self.assertTrue(permutationOrder("RLR'L'") == 7)
        self.assertTrue(permutationOrder("L'R'L'RLR'") == 3)
        self.assertTrue(permutationOrder("RLR'LRL'") == 2)
        self.assertTrue(permutationOrder("RL'R'LRLRL'") == 6)

    def test_exhaustive_move_generation(self):
        generated_moves_0 = generate_all_moves_of_len(0)
        self.assertTrue(generated_moves_0 == set())
        
        generated_moves_1 = generate_all_moves_of_len(1)
        self.assertTrue(generated_moves_1 == {"L", "L'", "R", "R'"})
        
        generated_moves_2 = generate_all_moves_of_len(2)
        self.assertTrue(generated_moves_2 == {"LR", "L'R", "RL", "R'L", "LR'", "L'R'", "RL'", "R'L'"})
        
        generated_moves_4 = generate_all_moves_of_len(4)
        self.assertTrue(len(generated_moves_4) == 32)
    
    def test_oriented_move_generation(self):
        generated_moves_0 = generate_all_moves_of_len(0, oriented=True)
        self.assertTrue(generated_moves_0 == set())
        
        generated_moves_1 = generate_all_moves_of_len(1, oriented=True)
        self.assertTrue(generated_moves_1 == set())
        
        generated_moves_2 = generate_all_moves_of_len(2, oriented=True)
        self.assertTrue(generated_moves_2 == set())
        
        generated_moves_4 = generate_all_moves_of_len(4, oriented=True)
        self.assertTrue(generated_moves_4 == {
            "LRL'R'", "LR'L'R", "L'RLR'", "L'R'LR", "RL'R'L", "R'L'RL", "RLR'L'", "R'LRL'"
        })
        
        generated_moves_5 = generate_all_moves_of_len(5, oriented=True)
        self.assertTrue(generated_moves_5 == {
            "LRLR'L", "LR'LRL", "RLRL'R", "RL'RLR", "L'RL'R'L'", "L'R'L'RL'", "R'LR'L'R'", "R'L'R'LR'"
        })
        
        generated_moves_6 = generate_all_moves_of_len(6, oriented=True)
        self.assertTrue(generated_moves_6 == {
            "LRLRLR", "LR'LR'LR'", "L'RL'RL'R", "L'R'L'R'L'R'", "RLRLRL", "RL'RL'RL'", "R'LR'LR'L", "R'L'R'L'R'L'"
        })

if __name__ == '__main__':
    unittest.main()
