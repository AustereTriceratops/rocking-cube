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
def parseMoves(moves: str):
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
