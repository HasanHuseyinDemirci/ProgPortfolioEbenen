from main import *

VIS_CALC = False
NAME_OUTPUT_FILE = "output.txt"

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
   


        if VIS_CALC: # Optional: Rechenschritte anzeigen
            print(result)
            print(steps) 

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
    calc_gauss_test()
    format_system_state_test()
    det2x2_test()
    save_output_in_file_test()



def test_is_valid_number():
    test_values = ["", "inf", "-inf", "NaN", "0", "-1", "2", "Andreas", "3.14", "-0.5", "1e10"]
    expected_results = [False, False, False, False, True, True, True, False, True, True, True]

    print("Testprogramm is_valid_number\n")
    for val, expected in zip(test_values, expected_results):
        result = is_valid_number(val)
        if result == expected:
            print(f"PASS: Eingabe '{val}' -> Ausgabe: {result}")
        else:
            print(f"FAIL: Eingabe '{val}' -> Ausgabe: {result}, erwartet: {expected}")

def test_is_valid_plane():
    test_values = [
        [0, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 1, 1],
        [1, 2, 3, 4]
    ]
    expected_results = [False, True, True, True, True]

    print("\nTestprogramm is_valid_plane\n")
    for val, expected in zip(test_values, expected_results):
        result = is_valid_plane(val)
        if result == expected:
            print(f"PASS: Eingabe {val} -> Ausgabe: {result}")
        else:
            print(f"FAIL: Eingabe {val} -> Ausgabe: {result}, erwartet: {expected}")

def test_row_to_str():
    test_values = [
        ([1, 2, 3, 4], None),
        ([1, -2, 3, -4], None),
        ([1.5, -2.25, 0, 4], 0),
        ([-1, 0, -3, 4], 1)
    ]
    expected_results = [
        "1 x + 2 y + 3 z = + 4",
        "1 x - 2 y + 3 z = - 4",
        "(1) 1.5 x - 2.25 y + 0 z = + 4",
        "(2) -1 x + 0 y - 3 z = + 4"
    ]

    print("\nTestprogramm row_to_str\n")
    for (plane, index), expected in zip(test_values, expected_results):
        result = row_to_str(plane, index)
        if result == expected:
            print(f"PASS: Eingabe {plane}, {index} -> Ausgabe: {result}")
        else:
            print(f"FAIL: Eingabe {plane}, {index} -> Ausgabe: {result}, erwartet: {expected}")

    #TODO Testfunktionen:
    #valid_rows ?
    #invalid_rows ? 
    #validate_csv_planes ?
    #load_csv_file(path):

def test_valid_rows():
    """Testet valid_rows() mit gemischten gültigen und ungültigen CSV-Zeilen.

    Erwartet wird, dass die Funktion die Gesamtanzahl der Zeilen
    und die Indizes der gültigen Ebenen zurückgibt.
    """
    rows = [
        ["1", "2", "3", "4"],          # gültig
        ["0", "0", "0", "1"],          # ungültig: Ebene mit (0,0,0)
        ["1", "2", "a", "4"],          # ungültig: nicht numerischer Eintrag
        ["5", "6", "7", "8", "9"],    # ungültig: zu viele Spalten
        ["-1.5", "2.0", "3", "0"],     # gültig
    ]

    print("\nTestprogramm valid_rows\n")
    try:
        total_rows, index_allowed = valid_rows(rows)
    except Exception as e:
        print(f"FAIL: valid_rows() wirft eine Exception: {e}")
        return

    print(f"Eingabezeilen: {len(rows)}")
    print(f"Ausgabe total_rows: {total_rows}")
    print(f"Ausgabe index_allowed: {index_allowed}")

    expected_total_rows = len(rows)
    expected_index_allowed = [0, 4]

    if total_rows != expected_total_rows:
        print(f"FAIL: total_rows inkorrekt. Erwartet: {expected_total_rows}, erhalten: {total_rows}")
    if index_allowed != expected_index_allowed:
        print(f"FAIL: index_allowed inkorrekt. Erwartet: {expected_index_allowed}, erhalten: {index_allowed}")


def test_invalid_rows():
    """Testet invalid_rows() basierend auf dem Ergebnis von valid_rows().

    Es wird geprüft, ob die Funktion die ungültigen Zeilen korrekt erkennt.
    """
    rows = [
        ["1", "2", "3", "4"],          # gültig
        ["0", "0", "0", "1"],          # ungültig
        ["1", "2", "a", "4"],          # ungültig
        ["5", "6", "7", "8", "9"],    # ungültig
        ["-1.5", "2.0", "3", "0"],     # gültig
    ]

    print("\nTestprogramm invalid_rows\n")
    try:
        total_rows, index_allowed = valid_rows(rows)
        invalid_indices = invalid_rows(rows, index_allowed)
    except Exception as e:
        print(f"FAIL: invalid_rows()/valid_rows() wirft eine Exception: {e}")
        return

    expected_invalid = [1, 2, 3]

    print(f"total_rows: {total_rows}")
    print(f"index_allowed (gültig): {index_allowed}")
    print(f"index_invalid (ungültig): {invalid_indices}")

    if invalid_indices != expected_invalid:
        print(f"FAIL: Ungültige Indizes inkorrekt. Erwartet: {expected_invalid}, erhalten: {invalid_indices}")


def test_validate_csv_planes():
    """Testet validate_csv_planes() als Gesamtkontrolle der CSV-Prüfung.

    Es wird geprüft, ob total_rows und index_allowed konsistent zu den
    erwarteten gültigen Zeilen sind.
    """
    rows = [
        ["1", "2", "3", "4"],          # gültig
        ["0", "0", "0", "1"],          # ungültig
        ["1", "2", "a", "4"],          # ungültig
        ["5", "6", "7", "8", "9"],    # ungültig
        ["-1.5", "2.0", "3", "0"],     # gültig
    ]

    print("\nTestprogramm validate_csv_planes\n")
    try:
        total_rows, index_allowed = validate_csv_planes(rows)
    except Exception as e:
        print(f"FAIL: validate_csv_planes() wirft eine Exception: {e}")
        return

    expected_total_rows = len(rows)
    expected_index_allowed = [0, 4]

    print(f"Eingabezeilen: {len(rows)}")
    print(f"Ausgabe total_rows: {total_rows}")
    print(f"Ausgabe index_allowed: {index_allowed}")

    if total_rows != expected_total_rows:
        print(f"FAIL: total_rows inkorrekt. Erwartet: {expected_total_rows}, erhalten: {total_rows}")
    if index_allowed != expected_index_allowed:
        print(f"FAIL: index_allowed inkorrekt. Erwartet: {expected_index_allowed}, erhalten: {index_allowed}")


def test_load_csv_file():
    """Testet load_csv_file() mit einer kleinen Beispiel-CSV-Datei.

    Es wird geprüft, ob die Funktion die Zeilen ohne Fehler einliest
    und die Struktur der Daten (Anzahl Zeilen/Spalten) stimmt.
    """
    #import os

    test_path = "test_ebenen.csv"
    rows = [
        ["1", "2", "3", "4"],
        ["0", "1", "0", "2"],
    ]

    # Kleine Test-CSV schreiben (mit Semikolon als Trenner)
    with open(test_path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(";".join(row) + "\n")

    print("\nTestprogramm load_csv_file\n")
    try:
        result = load_csv_file(test_path)
    except Exception as e:
        print(f"FAIL: load_csv_file() wirft eine Exception: {e}")
        os.remove(test_path)
        return

    # Aufräumen der Testdatei
    os.remove(test_path)

    if not isinstance(result, list) or len(result) != len(rows):
        print(f"FAIL: Unerwartete Struktur. Erwartete Zeilenanzahl: {len(rows)}, erhalten: {len(result) if isinstance(result, list) else 'kein Listentyp'}")
        return

    if any(len(r) != len(rows[0]) for r in result):
        print("FAIL: Unerwartete Spaltenanzahl in mindestens einer Zeile.")
        return

    print("PASS: CSV-Datei wurde erfolgreich und in erwarteter Struktur eingelesen.")