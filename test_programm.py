from Plane import Plane
from main import calc_gauss
from main import format_system_state
from main import det2
from main import save_output_in_file


VIS_CALC = True
FILE_SAVE = False
NAME_OUTPUT_FILE = "output_test.txt"

def calc_gauss_test():
    tests = [
        # Parallelfälle 
        # Führendes Element in x
        ([ -1,  2,  3, 10], [ -2,  4,  6, -5], "Die Ebenen sind echt parallel und haben keine Schnittmenge."),
        # Führendes Element in y
        ([  0,  1,  2,  3], [  0,  2,  4,  8], "Die Ebenen sind echt parallel und haben keine Schnittmenge."),
        # Führendes Element in z
        ([  0,  0,  1,  1], [  0,  0,  3,  5], "Die Ebenen sind echt parallel und haben keine Schnittmenge."),

        # Identische Ebenen 
        # Führendes Element in x
        ([ 1, 1, 1, 3], [ 2, 2, 2, 6], "Die Ebenen sind identisch und haben unendlich viele Schnittpunkte."),
        # Führendes Element in y
        ([ 0, 1, 2, 3], [ 0, 2, 4, 6], "Die Ebenen sind identisch und haben unendlich viele Schnittpunkte."),
        # Führendes Element in z
        ([ 0, 0, 2, 4], [ 0, 0, 4, 8], "Die Ebenen sind identisch und haben unendlich viele Schnittpunkte."),

        # Führendes Element in x
        ([1, 0, 0, 0], [0, 1, 0, 0],
         "Schnittgerade (Parametergleichung):\n    g(t) = (0, 0, 0) + t · (-0, -0, 1)\n"),

        # Führendes Element in y
        ([0, 1, 0, 0], [0, 1, 1, 0],
         "Schnittgerade (Parametergleichung):\n    g(t) = (0, 0, 0) + t · (1, -0, -0)\n"),

        # Allgemeiner Fall
        ([2, 3, 1, 4], [1, -2, 5, 3],
         "Schnittgerade (Parametergleichung):\n    g(t) = (-2.42857, 0.285714, 0) + t · (-2.42857, 1.28571, 1)\n"),

        # Zeilentausch nötig – führendes Element in x
        ([0, 3, 1, 2], [5, 3, 1, 2],
         "Schnittgerade (Parametergleichung):\n    g(t) = (0, -0.666667, 0) + t · (-0, -0.333333, 1)\n"),

        # Zeilentausch nötig – führendes Element in y
        ([0, 0, 1, 2], [0, 3, 1, 2],
         "Schnittgerade (Parametergleichung):\n    g(t) = (0, 0, -2) + t · (1, -0, -0)\n"),
    ]

    for e1, e2, expected_result in tests:
        result, steps  = calc_gauss(e1, e2, VIS_CALC)

        if result!= expected_result:
            print("Fehler: Falscher Indikator!")
            print(f"Erwartet: {expected_result}, erhalten: {result}")
            print(f"E1: {e1}\nE2: {e2}\n")
   


        if VIS_CALC:
            print(steps) # Optional: Rechenschritte anzeigen


def format_system_state_test():
    """
    Testet format_system_state() mit drei festen Fällen: 
    """

    tests = [
    # 1 — Ganze Zahlen
    (
        Plane(1, 2, 3, 4),
        Plane(5, 6, 7, 8),
        "Ganzzahlig:",
        "Ganzzahlig:\n"
        "       1·x +        2·y +        3·z =        4\n"
        "       5·x +        6·y +        7·z =        8\n\n"
    ),

    # 2 — Kurze Nachkommastellen
    (
        Plane(1.1, 2.2, 3.3, 4.4),
        Plane(5.5, 6.6, 7.7, 8.8),
        "Kurzkomma:",
        "Kurzkomma:\n"
        "     1.1·x +      2.2·y +      3.3·z =      4.4\n"
        "     5.5·x +      6.6·y +      7.7·z =      8.8\n\n"
    ),

    # 3 — Lange Nachkommastellen
    (
        Plane(1.234567, 2.999999, 3.141592, 4.000004),
        Plane(5.555555, 6.666666, 7.123456, 8.0000001),
        "Langkomma:",
        "Langkomma:\n"
        " 1.23457·x +        3·y +  3.14159·z =        4\n"
        " 5.55556·x +  6.66667·y +  7.12346·z =        8\n\n"
    ),
]

    for e1, e2, expected_result in tests:
        result, steps  = calc_gauss(e1, e2, VIS_CALC)

        if result!= expected_result:
            print("Fehler: Falscher Indikator!")
            print(f"Erwartet: {expected_result}, erhalten: {result}")
            print(f"E1: {e1}\nE2: {e2}\n")
   
        if VIS_CALC:
            print(steps) # Optional: Rechenschritte anzeigen


def det2_test():
    tests = [
        (1,1,1,1,0),
        (4,1,1,4,15),
        (0,0,0,0,0),
        (0,0.1,-10,2,1)
    ]
    for a,b,c,d,expected_value in tests:
        result = det2(a,b,c,d)
        if result != expected_value:
            print(f"Fehler: Inkorrekte Determinante.\nErwartet: {expected_value}\nErhalten: {result}.")

def format_system_state_test():
    """
    Testet format_system_state() mit drei festen Fällen: 
    """
    tests = [
    # 1 — Ganze Zahlen
    (
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        "Ganzzahlig:",
        "Ganzzahlig:\n"
        "       1·x +        2·y +        3·z =        4\n"
        "       5·x +        6·y +        7·z =        8\n\n"
    ),

    # 2 — Kurze Nachkommastellen
    (
        [1.1, 2.2, 3.3, 4.4],
        [5.5, 6.6, 7.7, 8.8],
        "Kurzkomma:",
        "Kurzkomma:\n"
        "     1.1·x +      2.2·y +      3.3·z =      4.4\n"
        "     5.5·x +      6.6·y +      7.7·z =      8.8\n\n"
    ),

    # 3 — Lange Nachkommastellen
    (
        [1.234567, 2.999999, 3.141592, 4.000004],
        [5.555555, 6.666666, 7.123456, 8.0000001],
        "Langkomma:",
        "Langkomma:\n"
        " 1.23457·x +        3·y +  3.14159·z =        4\n"
        " 5.55556·x +  6.66667·y +  7.12346·z =        8\n\n"
    ),
    ]

    for e1, e2, header, expected in tests:

        result = format_system_state(e1, e2, header)

        if result != expected:
            print("Fehler: Falsche Darstellung des LGS!")
            print(f"Erwartet:\n{expected}")
            print(f"Erhalten:\n{result}")

def det2_test():
    tests = [
        (1,1,1,1,0),
        (4,1,1,4,15),
        (0,0,0,0,0),
        (0,0.1,-10,2,1)
    ]
    for a,b,c,d,expected_value in tests:
        result = det2(a,b,c,d)
        if result != expected_value:
            print(f"Fehler: Inkorrekte Determinante.\nErwartet: {expected_value}\nErhalten: {result}.")

def save_output_in_file_test():
    tests = ["abc", "def", "ghi"]
    for test in tests:
        save_output_in_file(test)
        try:
            with open(NAME_OUTPUT_FILE, "r") as f:
                result = f.read()
        except Exception as e:
            print(f"Fehler beim Speichern: {e}")
        if result != test:
            print(f"Fehler: Fehler beim Speichern. \nErwartet: {test}\nErhalten: {result}.")


if __name__ == "__main__":
    calc_gauss_test()
    format_system_state_test()
    det2_test()