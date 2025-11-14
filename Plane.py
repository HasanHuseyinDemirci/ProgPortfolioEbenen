class Plane:
    def __init__(self,x,y,z,b):
        self.x = x
        self.y = y
        self.z = z
        self.b = b
    def __add__(self,summand):
        result = Plane(
            self.x + summand.x,
            self.y + summand.y,
            self.z + summand.z,
            self.b + summand.b
        )
        return result
    def __mul__(self,factor):
        result = Plane(
            self.x * factor,
            self.y * factor,
            self.z * factor,
            self.b * factor
        )
        return result