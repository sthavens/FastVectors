class FastVectors:
    def __init__(self):
        return

class Vector(FastVectors):
    vec = tuple() 
    def __init__(self, data):
        self.vec = tuple(data)
    
    def __eq__(self, other):
        return self.vec == other.vec

    def __add__(self, other):
        assert len(self.vec) == len(other.vec)
        return Vector([self.vec[i] + other.vec[i] for i in range(len(self.vec))])

    def __sub__(self, other):
        assert len(self.vec) == len(other.vec)
        return Vector([self.vec[i] - other.vec[i] for i in range(len(self.vec))])

    def __mul__(self, scalar : int):
        return Vector([i * scalar for i in self.vec])