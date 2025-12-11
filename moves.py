# Fixed: GRd, BOd
# Cycles: (YO YG GO), (YB YR BR), (WG WR GRu), (WB WO BOu)
# (5 13 12) (0 6 1) (11 7 10) (2 8 4) 3 9
def R(edges):
    permutation = [1, 6, 4, 3, 8, 12, 0, 11, 2, 9, 7, 10, 13, 5]
    result = [edges[permutation[i]] for i in range(14)]

    return result

# Fixed: GRd, BOd
# Cycles: (GO YG YO), (BR YR YB), (GRu WR WG), (BOu WO WB)
# (12 13 5) (1 6 0) (10 7 11) (4 8 2) 3 9
def RInv(edges):
    permutation = [6, 0, 8, 3, 2, 13, 1, 10, 4, 9, 11, 7, 5, 12]
    result = [edges[permutation[i]] for i in range(14)]

    return result

# Fixed: GRu, BOu
# Cycles: (WO WG GO), (WB WR BR), (YR YG GRd), (YO YB BOd)
# (8 11 12) (2 7 1) (6 13 9) (5 0 3) 4 10
def L(edges):
    permutation = [5, 7, 1, 0, 4, 3, 9, 2, 12, 13, 10, 8, 11, 6]
    result = [edges[permutation[i]] for i in range(14)]

    return result

# Fixed: GRu, BOu
# Cycles: (GO WG WO), (BR WR WB), (GRd YG YR), (BOd YB YO)
# (12 11 8) (1 7 2) (9 13 6) (3 0 5) 4 10
def LInv(edges):
    permutation = [3, 2, 7, 5, 4, 0, 13, 1, 11, 6, 10, 12, 8, 9]
    result = [edges[permutation[i]] for i in range(14)]

    return result
