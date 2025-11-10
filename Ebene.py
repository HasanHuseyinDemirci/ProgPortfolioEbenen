class Ebene:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,summand2):
        result = Ebene(
            self.x + summand2.x,
            self.y + summand2.y,
            self.z + summand2.z
        )
    def __multiply__(self,summand2):
        result = Ebene(
            self.x + summand2.x,
            self.y + summand2.y,
            self.z + summand2.z
        )
        return result