def applyPermutation(edges, permutation):
    n = len(permutation)
    result = [edges[permutation[i]] for i in range(n)]

    return result

# Fixed: GRd, BOd
# Cycles: (YO YG GO), (YB YR BR), (WG WR GRu), (WB WO BOu)
# (5 13 12) (0 6 1) (11 7 10) (2 8 4) 3 9
def R(edges):
    return applyPermutation(edges, [1, 6, 4, 3, 8, 12, 0, 11, 2, 9, 7, 10, 13, 5])

# Fixed: GRd, BOd
# Cycles: (GO YG YO), (BR YR YB), (GRu WR WG), (BOu WO WB)
# (12 13 5) (1 6 0) (10 7 11) (4 8 2) 3 9
def RInv(edges):
    return applyPermutation(edges, [6, 0, 8, 3, 2, 13, 1, 10, 4, 9, 11, 7, 5, 12])

# Fixed: GRu, BOu
# Cycles: (WO WG GO), (WB WR BR), (YR YG GRd), (YO YB BOd)
# (8 11 12) (2 7 1) (6 13 9) (5 0 3) 4 10
def L(edges):
    return applyPermutation(edges, [5, 7, 1, 0, 4, 3, 9, 2, 12, 13, 10, 8, 11, 6])

# Fixed: GRu, BOu
# Cycles: (GO WG WO), (BR WR WB), (GRd YG YR), (BOd YB YO)
# (12 11 8) (1 7 2) (9 13 6) (3 0 5) 4 10
def LInv(edges):
    return applyPermutation(edges, [3, 2, 7, 5, 4, 0, 13, 1, 11, 6, 10, 12, 8, 9])


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
