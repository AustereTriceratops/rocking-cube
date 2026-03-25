def applyPermutation(edges, permutation):
    n = len(permutation)
    result = [edges[permutation[i]] for i in range(n)]

    return result
