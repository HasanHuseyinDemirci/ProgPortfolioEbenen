class Plane:
    def __init__(self, a, b, c, d):
        # Ebene in der Form: a·x + b·y + c·z = d
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def as_list(self):
        # Rückgabe der Koeffizienten als Tupel (für Gauss-Berechnung)
        return [self.a, self.b, self.c, self.d]

    def __str__(self):
        return (
            f"{self.a:g}·x "
            f"{self.b:+g}·y "
            f"{self.c:+g}·z = "
            f"{self.d:g}"
        )