class Plane:
    def __init__(self, a, b, c, d):
        # Ebene in der Form: a·x + b·y + c·z = d
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, other):
        # Zeilenoperation: R1 + R2
        return Plane(
            self.a + other.a,
            self.b + other.b,
            self.c + other.c,
            self.d + other.d
        )

    def __mul__(self, faktor):
        # Zeilenoperation: k · R
        return Plane(
            self.a * faktor,
            self.b * faktor,
            self.c * faktor,
            self.d * faktor
        )

    __rmul__ = __mul__  # ermöglicht: k · Ebene

    def as_list(self):
        # Rückgabe der Koeffizienten als Tupel (für Gauss-Berechnung)
        return [self.a, self.b, self.c, self.d]

    def __str__(self):
        # Formatierte Ausgabe der Ebenengleichung für die Konsole
        return f"{self.a}x + {self.b}y + {self.c}z = {self.d}"