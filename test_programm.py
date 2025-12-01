from main import *

VIS_CALC = False
NAME_INPUT_FILE = "test_ebenen.csv"
NAME_OUTPUT_FILE = "output.txt"


def test_is_valid_number():
    tests = [
        ("", False),
        ("inf", False),
        ("-inf", False),
        ("NaN", False),
        ("C3-PO", False),
        ("-1", True),
        ("2", True),
        ("Andreas", False),
        ("3.14", True),
        ("-0.5", True),
        ("1e10", True)
    ]

    for val, expected in tests:
        result = is_valid_number(val)
        if result != expected:
            print(f"FAIL: Eingabe '{val}' -> Ausgabe: {result}, erwartet: {expected}")

def test_is_valid_plane():
    tests = [
        ([0, 0, 0, 1], False),
        ([1, 0, 0, 1], True),
        ([0, 1, 0, 1], True),
        ([0, 0, 1, 1], True),
        ([1, 2, 3, 4], True)
    ]

    for val, expected in tests:
        result = is_valid_plane(val)
        if result != expected:
            print(f"FAIL: Eingabe {val} -> Ausgabe: {result}, erwartet: {expected}")

def test_row_to_str():
    tests = [
        (([1, 2, 3, 4], None), "1 x + 2 y + 3 z = 4"),
        (([1, -2, 3, -4], None), "1 x - 2 y + 3 z = -4"),
        (([1.5, -2.25, 0, 4], 0), "(1) 1.5 x - 2.25 y + 0 z = 4"),
        (([-1, 0, -3, 4], 1), "(2) -1 x + 0 y - 3 z = 4")
    ]

    for (plane, index), expected in tests:
        result = row_to_str(plane, index)
        if result != expected:
            print(f"FAIL: Eingabe {plane}, {index} -> Ausgabe: {result}, erwartet: {expected}")

def test_valid_rows():
    tests = [
        # ((row, index), (expected_index_allowed, expected_string_in_total_rows))
        (([1, 2, 3, 4], 0), ([1], "(1) 1 x + 2 y + 3 z = 4")),
        (([0.5, -2, 0, 1], 3), ([4], "(4) 0.5 x - 2 y + 0 z = 1"))
    ]

    for (row, index), (expected_idx, expected_str) in tests:
        index_allowed = []
        total_rows = []

        idx_res, total_res = valid_rows(row, index_allowed, total_rows, index)

        if idx_res != expected_idx or total_res != [expected_str]:
            print(
                f"FAIL: Eingabe {row}, index={index} -> "
                f"index_allowed={idx_res}, total_rows={total_res}, "
                f"erwartet: {expected_idx}, [{expected_str}]"
            )

def test_invalid_rows():
    tests = [
        # (index, erwartete Ausgabestr)
        (1, "(X)  Zeile 2 in der CSV-Datei ist ungültig und wird übersprungen."),
        (4, "(X)  Zeile 5 in der CSV-Datei ist ungültig und wird übersprungen.")
    ]

    for index, expected_str in tests:
        total_rows = []

        result = invalid_rows(total_rows, index)

        if result != [expected_str]:
            print(
                f"FAIL: invalid_rows(index={index}) -> "
                f"{result}, erwartet: [{expected_str}]"
            )


def test_validate_csv_planes():
    """Testet validate_csv_planes() als Gesamtkontrolle der CSV-Prüfung.

    Es wird geprüft, ob index_allowed und die Anzahl der Einträge in total_rows
    zu den erwarteten gültigen/ungültigen Zeilen passen.
    """
    tests = [
        (
            [
                ["1", "2", "3", "4"],        # gültig
                ["0", "0", "0", "1"],        # ungültig (0,0,0 bei x,y,z)
                ["1", "2", "a", "4"],        # ungültig (kein Float)
                ["5", "6", "7", "8", "9"],   # ungültig (zu viele Spalten)
                ["-1.5", "2.0", "3", "0"],   # gültig
            ],
            [1, 5],  # erwartete gültige Zeilen (1-basiert!)
        )
    ]

    for rows, expected_index_allowed in tests:
        result = validate_csv_planes(rows)

        if result is False:
            print("FAIL: validate_csv_planes() hat False zurückgegeben, "
                  "obwohl mindestens zwei gültige Ebenen vorhanden sind.")
            continue

        total_rows, index_allowed = result

        if index_allowed != expected_index_allowed or len(total_rows) != len(rows):
            print(
                f"FAIL: validate_csv_planes() -> "
                f"index_allowed = {index_allowed} "
                f"erwartet: index_allowed={expected_index_allowed}"
            )

def test_load_csv_file():
    rows = [
        ["1", "2", "3", "4"],
        ["0", "1", "0", "2"],
    ]

    with open(NAME_INPUT_FILE, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(",".join(row) + "\n")

    result = load_csv_file(NAME_INPUT_FILE)

    if result != rows:
        print(f"FAIL: load_csv_file('{NAME_INPUT_FILE}') -> erhalten: {result}, erwartet: {rows}")


def calc_gauss_test():
    """
    Testet calc_gauss() mit mehreren festen Ebenenpaaren.

    Überprüft:
    - Parallelfälle
    - Identische Ebenen
    - Fälle mit Schnittgerade (inkl. Zeilentausch)
    """
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
         "Schnittgerade (Parametergleichung):\n"
         "    g(t) = (2.42857, -0.285714, 0) + t · (-2.42857, 1.28571, 1)\n"),

        # Zeilentausch nötig – führendes Element in x
        ([0, 3, 1, 2], [5, 3, 1, 2],
         "Schnittgerade (Parametergleichung):\n"
         "    g(t) = (0, 0.666667, 0) + t · (-0, -0.333333, 1)\n"),

        # Zeilentausch nötig – führendes Element in y
        ([0, 0, 1, 2], [0, 3, 1, 2],
         "Schnittgerade (Parametergleichung):\n"
         "    g(t) = (0, 0, 2) + t · (1, -0, -0)\n"),
]

    for e1, e2, expected_result in tests:
        result, steps  = calc_gauss(e1, e2, VIS_CALC)

        if result!= expected_result:
            print("Fehler: Falscher Indikator!")
            print(f"Erwartet: {expected_result}, erhalten: {result}")
            print(f"E1: {e1}\nE2: {e2}\n")
   
        if VIS_CALC: # Optional: Rechenschritte anzeigen   
            print(steps) 
            print(result)

def format_system_state_test():
    """
    Testet format_system_state() mit drei festen Beispielsystemen.

    Geprüft werden:
    - Ganze Zahlen
    - Kurze Nachkommastellen
    - Lange Nachkommastellen
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

def det2x2_test():
    """
    Testet det2x2() mit festen Beispielwerten.

    Vergleicht die berechnete 2x2-Determinante mit dem erwarteten Wert
    und meldet Abweichungen auf der Konsole.
    """
    tests = [
        (1,1,1,1,0),
        (4,1,1,4,15),
        (0,0,0,0,0),
        (0,0.1,-10,2,1)
    ]
    for a,b,c,d,expected_value in tests:
        result = det2x2(a,b,c,d)
        if result != expected_value:
            print(f"Fehler: Inkorrekte Determinante.\nErwartet: {expected_value}\nErhalten: {result}.")

def save_output_in_file_test():
    """
    Testet save_output_in_file(), indem mehrere Beispieltexte
    gespeichert und anschließend korrekt aus der Datei ausgelesen werden.
    """
    tests = ["Die Ebenen sind identisch und haben unendlich viele Schnittpunkte.",
             "Die Ebenen sind echt parallel und haben keine Schnittmenge.",
             "Schnittgerade (Parametergleichung): g(t) = (7, 0, -4) + t · (-2, 1, 0)"]
    for test in tests:
        save_output_in_file(test)
        try:
            with open(NAME_OUTPUT_FILE, "r") as f:
                result = f.read()
        except Exception as e:
            print(f"Fehler beim Speichern: {e}")
            continue
        if  result != test:
            print(f"Fehler: Fehler beim Speichern. \nErwartet: {test}\nErhalten: {result}.")


if __name__ == "__main__":
    test_is_valid_number()
    test_is_valid_plane()
    test_row_to_str()
    test_valid_rows()
    test_invalid_rows()
    test_validate_csv_planes()
    test_load_csv_file()
    calc_gauss_test()
    format_system_state_test()
    det2x2_test()
    save_output_in_file_test()