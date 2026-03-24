import random as rand
from RockingCube import RockingCube

def fixedRelativeTo(base_edges, permuted_edges):
    result = set()

    if len(base_edges) != len(permuted_edges):
        return result
    for i in range(len(base_edges)):
        if base_edges[i] == permuted_edges[i]:
            result.add(base_edges[i])

    return result

def get_unique_oriented_configurations_rc():
    unique_oriented_configurations = set()

    # find all unique orientations of the cube
    for i in range(17):
        generated_moves = RockingCube.generate_all_moves_of_len(i, oriented=True)
        
        for sequence in generated_moves:
            permutation = RockingCube.parseMoves(sequence).edges
            unique_oriented_configurations.add(tuple(permutation))
        
        print(len(unique_oriented_configurations))

def get_inverse(move_seq):
  index = 0
  inverse = ""
  
  while index < len(move_seq):
    sym = move_seq[-1 - index]
    
    if sym == "'":
      index += 1
      sym = move_seq[-1 - index]
      inverse += sym
    else:
      inverse += sym + "'"
    
    index += 1
  
  return inverse
