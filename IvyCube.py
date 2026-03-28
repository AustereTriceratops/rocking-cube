import random as rand
from typing import Final, Self

from moves import applyPermutation 

# oriented with blue face facing you, yellow face on the back left and red face on the back right
class IvyCube:
    START_EDGES: Final[list[str]] = ["B", "Y", "R", "W", "O", "G"]
    
    START_CORNER_PARITY: Final[dict[str, int]] = {"U": 0, "D": 0, "L": 0, "R": 0}
    
    def __init__(self, edges: list[str] = None, corner_parity: dict[str, int] = None):
        self.edges = self.START_EDGES if edges is None else edges
        self.corner_parity = self.START_CORNER_PARITY.copy() if corner_parity is None else corner_parity
    
    def reset(self):
        self.edges = self.START_EDGES
        self.corner_parity = self.START_CORNER_PARITY.copy()
    
    def copy(self) -> Self:
        edges = [edge for edge in self.edges]
        corner_parity = self.corner_parity.copy()
        
        return IvyCube(edges=edges, corner_parity=corner_parity)
    
    @property
    def corners_oriented(self) -> bool:
        return  (
            self.corner_parity['L'] % 3 == 0 and
            self.corner_parity['R'] % 3 == 0 and
            self.corner_parity['U'] % 3 == 0 and
            self.corner_parity['D'] % 3 == 0
        )
        
    @property
    def edges_oriented(self) -> bool:
        return  self.edges == self.START_EDGES
    
    @property
    def is_solved(self) -> bool:
        return self.corners_oriented and self.edges_oriented
    
    # Cycles: (B Y R)
    # (0 1 2) 
    def U(self):
        self.edges = applyPermutation(self.edges, [2, 0, 1, 3, 4, 5])
        self.corner_parity["U"] += 1
        return self

    def UInv(self):
        self.edges = applyPermutation(self.edges, [1, 2, 0, 3, 4, 5])
        self.corner_parity["U"] -= 1
        return self

    # Cycles: (B W O)
    # (0 3 4) 
    def D(self):
        self.edges = applyPermutation(self.edges, [4, 1, 2, 0, 3, 5])
        self.corner_parity["D"] += 1
        return self

    def DInv(self):
        self.edges = applyPermutation(self.edges, [3, 1, 2, 4, 0, 5])
        self.corner_parity["D"] -= 1
        return self

    # Cycles: (Y O G)
    # (1 4 5)
    def L(self):
        self.edges = applyPermutation(self.edges, [0, 5, 2, 3, 1, 4])
        self.corner_parity["L"] += 1
        return self

    def LInv(self):
        self.edges = applyPermutation(self.edges, [0, 4, 2, 3, 5, 1])
        self.corner_parity["L"] -= 1
        return self

    # Cycles: (W R G)
    # (3 2 5)
    def R(self):
        self.edges = applyPermutation(self.edges, [0, 1, 3, 5, 4, 2])
        self.corner_parity["R"] += 1
        return self

    def RInv(self):
        self.edges = applyPermutation(self.edges, [0, 1, 5, 2, 4, 3])
        self.corner_parity["R"] -= 1
        return self
    
    # will parse sequences of moves like UR, LR'DU'D, D'LRLR'D
    # TODO: assumes that whatever string is passed to it is valid,
    # but this should be checked
    @staticmethod
    def parseMoves(moves: str, cube: Self = None) -> Self:
        cube = IvyCube() if cube is None else cube.copy()
            
        N = len(moves)

        for i in range(N):
            if moves[i] == "'":
                continue
            elif moves[i] == 'R':
                if i + 1 < N and moves[i + 1] == "'":
                    cube.RInv()
                else:
                    cube.R()
            elif moves[i] == 'L':
                if i + 1 < N and moves[i + 1] == "'":
                    cube.LInv()
                else:
                    cube.L()
            elif moves[i] == 'U':
                if i + 1 < N and moves[i + 1] == "'":
                    cube.UInv()
                else:
                    cube.U()
            elif moves[i] == 'D':
                if i + 1 < N and moves[i + 1] == "'":
                    cube.DInv()
                else:
                    cube.D()

        return cube
    
    # def generate_solutions(self):
    #     solutions = []
    #     oriented = (self.corner_parity['L'] % 3) == 0 and (self.corner_parity['R'] % 3) == 0
        
    #     end_loop = False

    #     for depth in range(16):
    #         generated_moves = IvyCube.generate_all_moves_of_len(depth + 1, oriented=oriented)

    #         for sequence in generated_moves:
    #             guessed_solution = IvyCube.parseMoves(sequence, self)
                
    #             edges_solved = guessed_solution.edges == IvyCube.START_EDGES
                
    #             if edges_solved and guessed_solution.corners_oriented:
    #                 solutions.append(sequence)
    #                 end_loop = True
            
    #         if end_loop: break

    #     return solutions
    