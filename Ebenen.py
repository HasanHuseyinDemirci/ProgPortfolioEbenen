import random as rnd
class Ebene:
    def __init__(self,x,y,z,b):
        self.x = x
        self.y = y
        self.z = z
        self.b = b
    def __add__(self,summand):
        result = Ebene(
            self.x + summand.x,
            self.y + summand.y,
            self.z + summand.z,
            self.b + summand.b
        )
        return result
    def __mul__(self,factor):
        result = Ebene(
            self.x * factor,
            self.y * factor,
            self.z * factor,
            self.b * factor
        )
        return result
## AB HIER BEGINNT BERECHNUNG (HASAN) 0DIVISION PROBLEM
ebene1 = Ebene(rnd.randint(-10,10),rnd.randint(-10,10),rnd.randint(-10,10),rnd.randint(-10,10))
ebene2 = Ebene(rnd.randint(-10,10),rnd.randint(-10,10),rnd.randint(-10,10),rnd.randint(-10,10))
print(ebene1.x,ebene1.y,ebene1.z, "|",ebene1.b)
print(ebene2.x,ebene2.y,ebene2.z, "|",ebene2.b)
print("--------------")
def gauss(e1, e2):
    if e1.x < 0:
        e1 = e1*(-1)
    if e2.x < 0:
        e2 = e2*(-1)

    e1= e1*(-e2.x/e1.x)
    e2= e2+e1
    print(e1.x, e1.y, e1.z, "|", e1.b)
    print(e2.x, e2.y, e2.z, "|", e2.b)
    print("--------------")

    if e1.y < 0:
        e1 = e1*(-1)
    if e2.y < 0:
        e2 = e2*(-1)
    e2= e2*(-e1.y/e2.y)
    e1= e1+e2
    print(e1.x, e1.y, e1.z, "|", e1.b)
    print(e2.x, e2.y, e2.z, "|", e2.b)
    print("--------------")
    return e1, e2

ebene1, ebene2 = gauss(ebene1, ebene2)


## AB HIER ENDET DIE BERECHNUNG (HASAN)
