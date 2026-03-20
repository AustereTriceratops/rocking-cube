import random as rand

def fixedRelativeTo(base_edges, permuted_edges):
    result = set()

    if len(base_edges) != len(permuted_edges):
        return result
    for i in range(len(base_edges)):
        if base_edges[i] == permuted_edges[i]:
            result.add(base_edges[i])

    return result
