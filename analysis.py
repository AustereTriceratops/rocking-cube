import random as rand

from moves import *
from constants import *

def fixedRelativeTo(base_edges, permuted_edges):
    result = set()

    if len(base_edges) != len(permuted_edges):
        return result
    for i in range(len(base_edges)):
        if base_edges[i] == permuted_edges[i]:
            result.add(base_edges[i])

    return result

# will parse sequences of moves like LR, R'LRL', R'LRL'R'R, etc.
# TODO: assumes that whatever string is passed to it is valid,
# but this should be checked
def parseMoves(moves: str, edges: list[str] = []):
    if len(edges) == 0:
        edges = [edge for edge in START_EDGES]

    N = len(moves)

    for i in range(N):
        if moves[i] == "'":
            continue
        elif moves[i] == 'R':
            if i + 1 < N and moves[i + 1] == "'":
                edges = RInv(edges)
            else:
                edges = R(edges)
        elif moves[i] == 'L':
            if i + 1 < N and moves[i + 1] == "'":
                edges = LInv(edges)
            else:
                edges = L(edges)

    return edges

def permutationOrder(moves):
    edges = parseMoves(moves)
    n = 1
        
    while edges != START_EDGES:
        edges = parseMoves(moves, edges)
        n += 1

    return n

def randomPermutation(n_moves):
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
    edges = parseMoves(move_str)
    return edges, move_str

# generate a random permutation that leaves the corners oriented
# i.e. #L - #L' must be 0 mod 3, same with R and R'
# n_moves is a lower bound, the actual number of moves this method produces
# will be in the range [n, n+2] (inclusive)
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
    edges = parseMoves(move_str)
    return edges, move_str

# oriented movesets will preserve the orientation of the corner pieces
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
def solve(edges):
    solutions = []

    generated_moves = generate_all_moves_of_len(16, oriented=True)

    for sequence in generated_moves:
        guessed_solution = parseMoves(sequence, edges)
        
        if guessed_solution == START_EDGES:
            solutions.append(sequence)

    return solutions
