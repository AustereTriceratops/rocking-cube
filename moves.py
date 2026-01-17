def applyPermutation(edges, permutation):
    n = len(permutation)
    result = [edges[permutation[i]] for i in range(n)]

    return result

## IVY CUBE 

# START_EDGES_IVY = [
#   "B", "Y", "R", "W", "O", "G"
# ]

# Cycles: (B Y R)
# (0 1 2) 
def T(edges):
    return applyPermutation(edges, [2, 0, 1, 3, 4, 5])

def TInv(edges):
    return applyPermutation(edges, [1, 2, 0, 3, 4, 5])

# Cycles: (B W O)
# (0 3 4) 
def F(edges):
    return applyPermutation(edges, [4, 1, 2, 0, 3, 5])

def FInv(edges):
    return applyPermutation(edges, [3, 1, 2, 4, 0, 5])

# Cycles: (Y O G)
# (1 4 5)
def BL(edges):
    return applyPermutation(edges, [0, 5, 2, 3, 1, 4])

def BLInv(edges):
    return applyPermutation(edges, [0, 4, 2, 3, 5, 1])

# Cycles: (W R G)
# (3 2 5)
def BR(edges):
    return applyPermutation(edges, [0, 1, 3, 5, 4, 2])

def BRInv(edges):
    return applyPermutation(edges, [0, 1, 5, 2, 4, 3])
