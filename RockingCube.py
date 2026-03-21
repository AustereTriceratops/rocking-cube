import random as rand
from typing import Final, Self

from moves import applyPermutation 

# cube is oriented with the blue face up and the orange face facing you
class RockingCube:
    START_EDGES: Final[list[str]] = [
        "YB", "BR", "WB", "BOr", "BOl", "YO", "YR",
        "WR", "WO", "GRl", "GRr", "WG", "GO", "YG"
    ]
    
    def __init__(self, edges: list[str] = None, corner_parity: dict[str, int] = None):
        self.edges = self.START_EDGES if edges is None else edges
        self.corner_parity = {"L": 0, "R": 0} if corner_parity is None else corner_parity
    
    def reset(self):
        self.edges = self.START_EDGES
        self.corner_parity = {"L": 0, "R": 0}
    
    def copy(self) -> Self:
        edges = [edge for edge in self.edges]
        corner_parity = {'L': self.corner_parity['L'], 'R': self.corner_parity['R']}
        
        return RockingCube(edges=edges, corner_parity=corner_parity)
    
    # Fixed: GRl, BOl
    # Cycles: (YO YG GO), (YB YR BR), (WG WR GRr), (WB WO BOr)
    # (5 13 12) (0 6 1) (11 7 10) (2 8 3) 4 9
    def R(self):
        self.edges = applyPermutation(self.edges, [1, 6, 3, 8, 4, 12, 0, 11, 2, 9, 7, 10, 13, 5])
        self.corner_parity['R'] += 1
        return self

    # Fixed: GRl, BOl
    # Cycles: (GO YG YO), (BR YR YB), (GRr WR WG), (BOr WO WB)
    # (12 13 5) (1 6 0) (10 7 11) (3 8 2) 4 9
    def RInv(self):
        self.edges = applyPermutation(self.edges, [6, 0, 8, 2, 4, 13, 1, 10, 3, 9, 11, 7, 5, 12])
        self.corner_parity['R'] -= 1
        return self

    # Fixed: GRr, BOr
    # Cycles: (WO WG GO), (WB WR BR), (YR YG GRl), (YO YB BOl)
    # (8 11 12) (2 7 1) (6 13 9) (5 0 4) 3 10
    def L(self):
        self.edges = applyPermutation(self.edges, [5, 7, 1, 3, 0, 4, 9, 2, 12, 13, 10, 8, 11, 6])
        self.corner_parity['L'] += 1
        return self

    # Fixed: GRr, BOr
    # Cycles: (GO WG WO), (BR WR WB), (GRl YG YR), (BOl YB YO)
    # (12 11 8) (1 7 2) (9 13 6) (4 0 5) 3 10
    def LInv(self):
        self.edges = applyPermutation(self.edges, [4, 2, 7, 3, 5, 0, 13, 1, 11, 6, 10, 12, 8, 9])
        self.corner_parity['L'] -= 1
        return self

    # will parse sequences of moves like LR, R'LRL', R'LRL'R'R, etc.
    # TODO: assumes that whatever string is passed to it is valid,
    # but this should be checked
    @staticmethod
    def parseMoves(moves: str, cube: Self = None) -> Self:
        cube = RockingCube() if cube is None else cube.copy()
            
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

    @staticmethod
    def permutationOrder(moves):
        cube = RockingCube.parseMoves(moves)
        n = 1
            
        while cube.edges != cube.START_EDGES:
            cube = RockingCube.parseMoves(moves, cube)
            n += 1

        return n

    @staticmethod
    def randomPermutation(n_moves) -> Self:
        moves = []

        for i in range(n_moves):
            r = rand.random()

            if i > 0:
                if moves[i-1] == "R" or moves[i-1] == "R'":
                    if r < 0.5:
                        moves.append("L")
                    else:
                        moves.append("L'")
                elif moves[i-1] == "L" or moves[i-1] == "L'":
                    if r < 0.5:
                        moves.append("R")
                    else:
                        moves.append("R'")
            else:
                if r < 0.25:
                    moves.append("L")
                elif r < 0.5:
                    moves.append("L'")
                elif r < 0.75:
                    moves.append("R")
                else:
                    moves.append("R'")

        move_str = str.join("", moves)
        cube = RockingCube.parseMoves(move_str)
        return cube, move_str

    # generate a random permutation that leaves the corners oriented
    # i.e. #L - #L' must be 0 mod 3, same with R and R'
    # n_moves is a lower bound, the actual number of moves this method produces
    # will be in the range [n, n+2] (inclusive)
    @staticmethod
    def randomOrientedPermutation(n_moves):
        moves = []
        r_parity = 0
        l_parity = 0

        for i in range(n_moves):
            r = rand.random()

            if i > 0:
                if moves[i-1] == "R" or moves[i-1] == "R'":
                    if r < 0.5:
                        moves.append("L")
                        l_parity += 1
                    else:
                        moves.append("L'")
                        l_parity -= 1
                elif moves[i-1] == "L" or moves[i-1] == "L'":
                    if r < 0.5:
                        moves.append("R")
                        r_parity += 1
                    else:
                        moves.append("R'")
                        r_parity -= 1
            else:
                if r < 0.25:
                    moves.append("L")
                    l_parity += 1
                elif r < 0.5:
                    moves.append("L'")
                    l_parity -= 1
                elif r < 0.75:
                    moves.append("R")
                    r_parity += 1
                else:
                    moves.append("R'")
                    r_parity -= 1

        if l_parity % 3 == 1:
            moves.append("L'")
        elif l_parity % 3 == 2:
            moves.append("L")

        if r_parity % 3 == 1:
            moves.append("R'")
        elif r_parity % 3 == 2:
            moves.append("R")

        move_str = str.join("", moves)
        cube = RockingCube.parseMoves(move_str)
        return cube.edges, move_str

    # oriented movesets will preserve the orientation of the corner pieces
    @staticmethod
    def generate_all_moves_of_len(depth, oriented=False):
        N = 2**(depth + 1)
        generated_moves = set()
        
        if depth == 0: return generated_moves
        
        for i in range(N):
            ib = format(i, f'0{depth + 1}b') # convert to binary with leading 0s
            moves = []
            prevMoveType = ""
            l_parity = 0
            r_parity = 0
            
            if ib[0] == "0":
                prevMoveType = "R"
            elif ib[0] == "1":
                prevMoveType = "L"
            
            for j in range(depth):
                if ib[j + 1] == "0":
                    if prevMoveType == "L":
                        moves.append("R")
                        prevMoveType = "R"
                        r_parity += 1
                    elif prevMoveType == "R":
                        moves.append("L")
                        prevMoveType = "L"
                        l_parity += 1
                elif ib[j + 1] == "1":
                    if prevMoveType == "L":
                        moves.append("R'")
                        prevMoveType = "R"
                        r_parity -= 1
                    elif prevMoveType == "R":
                        moves.append("L'")
                        prevMoveType = "L"
                        l_parity -= 1
            
            if not oriented or (oriented and l_parity % 3 == 0 and r_parity % 3 == 0):
                generated_moves.add("".join(moves))
            
        return generated_moves

    # solve the rocking cube from a corners-oriented form
    # God's number for this puzzle is 16, so the search depth is set to 16
    def generate_solutions(self):
        solutions = []
        oriented = (self.corner_parity['L'] % 3 == 0 & self.corner_parity['R'] % 3 == 0)

        generated_moves = RockingCube.generate_all_moves_of_len(16, oriented=oriented)

        for sequence in generated_moves:
            guessed_solution = RockingCube.parseMoves(sequence, self)
            
            edges_solved = guessed_solution.edges == RockingCube.START_EDGES
            corners_oriented = (
                guessed_solution.corner_parity['L'] % 3 == 0 & guessed_solution.corner_parity['R'] % 3 == 0
            )
            
            if edges_solved and corners_oriented:
                solutions.append(sequence)

        return solutions
    