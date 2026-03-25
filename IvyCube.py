import random as rand
from typing import Final, Self

from moves import applyPermutation 

# oriented with blue face facing you, yellow face on the back left and red face on the back right
class IvyCube:
    START_EDGES: Final[list[str]] =["B", "Y", "R", "W", "O", "G"]
    
    def __init__(self, edges: list[str] = None, corner_parity: dict[str, int] = None):
        self.edges = self.START_EDGES if edges is None else edges
        self.corner_parity = {"U": 0, "D": 0, "L": 0, "R": 0} if corner_parity is None else corner_parity
    
    def reset(self):
        self.edges = self.START_EDGES
        self.corner_parity = {"U": 0, "D": 0, "L": 0, "R": 0}
    
    def copy(self) -> Self:
        edges = [edge for edge in self.edges]
        corner_parity = self.corner_parity.copy()
        
        return IvyCube(edges=edges, corner_parity=corner_parity)
    
    # Cycles: (B Y R)
    # (0 1 2) 
    def U(self):
        self.edges = applyPermutation(self.edges, [2, 0, 1, 3, 4, 5])
        self.corner_parity["U"] += 1
        return self

    def UInv(self):
        self.edges = applyPermutation(self.edges, [1, 2, 0, 3, 4, 5])
        self.corner_parity["U"] -= 1
        return self

    # Cycles: (B W O)
    # (0 3 4) 
    def D(self):
        self.edges = applyPermutation(self.edges, [4, 1, 2, 0, 3, 5])
        self.corner_parity["D"] += 1
        return self

    def DInv(self):
        self.edges = applyPermutation(self.edges, [3, 1, 2, 4, 0, 5])
        self.corner_parity["D"] -= 1
        return self

    # Cycles: (Y O G)
    # (1 4 5)
    def L(self):
        self.edges = applyPermutation(self.edges, [0, 5, 2, 3, 1, 4])
        self.corner_parity["L"] += 1
        return self

    def LInv(self):
        self.edges = applyPermutation(self.edges, [0, 4, 2, 3, 5, 1])
        self.corner_parity["L"] -= 1
        return self

    # Cycles: (W R G)
    # (3 2 5)
    def R(self):
        self.edges = applyPermutation(self.edges, [0, 1, 3, 5, 4, 2])
        self.corner_parity["R"] += 1
        return self

    def RInv(self):
        self.edges = applyPermutation(self.edges, [0, 1, 5, 2, 4, 3])
        self.corner_parity["R"] -= 1
        return self