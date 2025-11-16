from Plane import Plane
from main import calc_gauss

VIS_CALC = False
FILE_SAVE = False

def calc_gauss_test():
    """
    Testet calc_gauss() für:
    - echt parallele Ebenen (ind = 0)
    - identische Ebenen (ind = 1)

    TODO:
    Sobald ind = 2 (Schnittgerade) implementiert ist,
    expected_eq entsprechend anpassen und auf Nicht-Leere prüfen.
    """

    tests = [
        # Parallelfälle (ind = 0)
        # Führendes Element in x
        (Plane(-1, 2, 3, 10), Plane(-2, 4, 6, -5), 0, ""),
        # Führendes Element in y
        (Plane(0, 1, 2, 3), Plane(0, 2, 4, 8), 0, ""),
        # Führendes Element in z
        (Plane(0, 0, 1, 1), Plane(0, 0, 3, 5), 0, ""),

        # Identische Ebenen (ind = 1)
        # Führendes Element in x
        (Plane(1, 1, 1, 3), Plane(2, 2, 2, 6), 1, ""),
        # Führendes Element in y
        (Plane(0, 1, 2, 3), Plane(0, 2, 4, 6), 1, ""),
        # Führendes Element in z
        (Plane(0, 0, 2, 4), Plane(0, 0, 4, 8), 1, ""),

        # Schneidende Ebenen (ind = 2)
        # Führendes Element in x
        (Plane(1, 0, 0, 0), Plane(0, 1, 0, 0), 2, ""),
        # Führendes Element in y
        (Plane(0, 1, 0, 0), Plane(0, 1, 1, 0), 2, ""),
        # Führendes Element in z kann bei ind = 2 nicht auftreten (würde parallel oder identisch sein)
        # Allgemeiner Fall
        (Plane(2, 3, 1, 4), Plane(1, -2, 5, 3), 2, ""),
    ]

    for e1, e2, expected_ind, expected_eq in tests:
        ind, eq, steps, _ = calc_gauss(e1, e2, VIS_CALC, FILE_SAVE)

        if ind != expected_ind:
            print("Fehler: Falscher Indikator!")
            print(f"Erwartet: {expected_ind}, erhalten: {ind}")
            print(f"E1: {e1}\nE2: {e2}\n")
   
        if eq != expected_eq:
            print("Fehler: Falscher Gleichung!")
            print(f"Erwartet: '{expected_eq}', erhalten: '{eq}'")
            print(f"E1: {e1}\nE2: {e2}\n")

        if VIS_CALC:
            print(steps) # Optional: Rechenschritte anzeigen



if __name__ == "__main__":
    calc_gauss_test()