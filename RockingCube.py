from typing import Final, Self

from moves import applyPermutation 

class RockingCube:
    START_EDGES: Final[list[str]] = [
        "YB", "BR", "WB", "BOd", "BOu", "YO", "YR",
        "WR", "WO", "GRd", "GRu", "WG", "GO", "YG"
    ]
    
    edges = START_EDGES
    
    def reset(self):
        self.edges = self.START_EDGES
    
    # Fixed: GRd, BOd
    # Cycles: (YO YG GO), (YB YR BR), (WG WR GRu), (WB WO BOu)
    # (5 13 12) (0 6 1) (11 7 10) (2 8 4) 3 9
    def R(self):
        self.edges = applyPermutation(self.edges, [1, 6, 4, 3, 8, 12, 0, 11, 2, 9, 7, 10, 13, 5])
        return self

    # Fixed: GRd, BOd
    # Cycles: (GO YG YO), (BR YR YB), (GRu WR WG), (BOu WO WB)
    # (12 13 5) (1 6 0) (10 7 11) (4 8 2) 3 9
    def RInv(self):
        self.edges = applyPermutation(self.edges, [6, 0, 8, 3, 2, 13, 1, 10, 4, 9, 11, 7, 5, 12])
        return self

    # Fixed: GRu, BOu
    # Cycles: (WO WG GO), (WB WR BR), (YR YG GRd), (YO YB BOd)
    # (8 11 12) (2 7 1) (6 13 9) (5 0 3) 4 10
    def L(self):
        self.edges = applyPermutation(self.edges, [5, 7, 1, 0, 4, 3, 9, 2, 12, 13, 10, 8, 11, 6])
        return self

    # Fixed: GRu, BOu
    # Cycles: (GO WG WO), (BR WR WB), (GRd YG YR), (BOd YB YO)
    # (12 11 8) (1 7 2) (9 13 6) (3 0 5) 4 10
    def LInv(self):
        self.edges = applyPermutation(self.edges, [3, 2, 7, 5, 4, 0, 13, 1, 11, 6, 10, 12, 8, 9])
        return self

    # will parse sequences of moves like LR, R'LRL', R'LRL'R'R, etc.
    # TODO: assumes that whatever string is passed to it is valid,
    # but this should be checked
    @staticmethod
    def parseMoves(moves: str, cube: Self = None):
        if not cube:
            cube = RockingCube()
            
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

        return cube
    