# test_programm.py

from Plane import Plane
from main import calc_gauss


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
        # (Ebene 1, Ebene 2, expected_ind, expected_eq)

        # Parallel
        (Plane(1, 0, 0, 1), Plane(1, 0, 0, 2), 0, ""),
        (Plane(2, 1, 0, 3), Plane(2, 1, 0, 5), 0, ""),
        (Plane(3, -2, 1, 1), Plane(3, -2, 1, -4), 0, ""),
        (Plane(4, 5, -2, 0), Plane(4, 5, -2, 7), 0, ""),
        (Plane(-1, 2, 3, 10), Plane(-1, 2, 3, -5), 0, ""),

        # Identisch
        (Plane(2, -1, 3, 5), Plane(4, -2, 6, 10), 1, ""),
        (Plane(-1, 4, -2, 8), Plane(-2, 8, -4, 16), 1, ""),
        (Plane(3, 2, 1, 0), Plane(6, 4, 2, 0), 1, ""),
        (Plane(5, -1, 0, 7), Plane(10, -2, 0, 14), 1, ""),
        (Plane(1, 1, 1, 3), Plane(2, 2, 2, 6), 1, ""),
    ]

    for e1, e2, expected_ind, expected_eq in tests:
        ind, eq, _, _ = calc_gauss(e1, e2, False, False)

        if ind != expected_ind:
            print("Fehler: Falscher Indikator!")
            print(f"Erwartet: {expected_ind}, erhalten: {ind}")
            print(f"E1: {e1}\nE2: {e2}\n")
   
        if eq != expected_eq:
            print("Fehler: Falscher Gleichung!")
            print(f"Erwartet: '{expected_eq}', erhalten: '{eq}'")
            print(f"E1: {e1}\nE2: {e2}\n")



if __name__ == "__main__":
    calc_gauss_test()