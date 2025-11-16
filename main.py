from Plane import Plane


NAME_INPUT_FILE = ""
NAME_OUTPUT_FILE = "output.txt"
# DECIMAL_PLACES = 3
COEFF_WIDTH = 8


def read_input():
    """
    TODO: CLI- oder Datei-Eingabe implementieren.
    Platzhalter für Entwicklung.
    """
    return Plane(1, 1, 1, 3), Plane(1, -1, 1, 1), True, False


def format_system_state(row1, row2, header=None):
    """
    Formatiert den aktuellen Zustand des linearen Gleichungssystems
    mit zwei Ebenengleichungen als Textblock für die Rechenschritte.

    Parameter:
        row1, row2: Listen oder Tupel der Form [a, b, c, d]
        header (str oder None): Optionaler Überschriftstext
    """
    lines = ""
    if header:
        lines += header + "\n"

    a1, b1, c1, d1 = row1
    a2, b2, c2, d2 = row2

    lines += (
        f"{a1:>{COEFF_WIDTH}g}·x + "
        f"{b1:>{COEFF_WIDTH}g}·y + "
        f"{c1:>{COEFF_WIDTH}g}·z = "
        f"{d1:>{COEFF_WIDTH}g}\n"
    )      
    lines += (
        f"{a2:>{COEFF_WIDTH}g}·x + "
        f"{b2:>{COEFF_WIDTH}g}·y + "
        f"{c2:>{COEFF_WIDTH}g}·z = "
        f"{d2:>{COEFF_WIDTH}g}\n\n"
    )
    return lines


def calc_gauss(e1, e2, vis_calc, file_save):
    """
    Führt den Gauß-Algorithmus für zwei Ebenen durch.

    Parameter:
        e1 (Plane): Erste Ebene in der Form ax + by + cz = d
        e2 (Plane): Zweite Ebene in der Form ax + by + cz = d
        vis_calc (bool): Falls True, werden die Rechenschritte als Text ausgegeben
        file_save (bool): Falls True, wird das Ergebnis zusätzlich in eine Datei gespeichert

    Rückgabe:
        ind (int): 
            0 = Ebenen sind echt parallel (keine Schnittmenge)
            1 = Ebenen sind identisch (unendlich viele Lösungen)
            2 = Die Ebenen schneiden sich in einer Geraden
        equation (str): Gleichung der Schnittgeraden (falls ind == 2, sonst "")
        calc_steps (str): Textdarstellung der Rechenschritte (optional)
        file_save (bool): Wird unverändert zurückgegeben
    """

    steps = ""

     # Koeffizienten der Ebenen als Listen
    row1 = e1.as_list()  # [a1, b1, c1, d1]
    row2 = e2.as_list()  # [a2, b2, c2, d2]

    # Ausgangssystem speichern
    steps += format_system_state(row1, row2, header="Ausgangssystem:")

    # -------------------------------
    # 1. Gauß-Schritt: Pivot suchen und zweite Zeile eliminieren
    # -------------------------------

    # Pivot-Spalte bestimmen: zuerst x, dann y, sonst z
    if row1[0] != 0 or row2[0] != 0: # 0 = x, 1 = y, 2 = z
        pivot_index = 0
    elif row1[1] != 0 or row2[1] != 0:
        pivot_index = 1
    else:
        pivot_index = 2

    pivot_name = ["x", "y", "z"][pivot_index]
    steps += (f"Führendes Element in Spalte '{pivot_name}' wird für den Gauß-Schritt verwendet.\n")

    # Falls Pivot in Zeile 1 = 0 → Zeilen tauschen
    if row1[pivot_index] == 0 and row2[pivot_index] != 0:
        steps += (f"Zeilen werden vertauscht, da das führende Element in Zeile 1 = 0 ist (Spalte {pivot_name}).\n")
        row1, row2 = row2, row1
        steps += format_system_state(row1, row2, header="Nach Zeilenvertauschung:")

     # Faktor k zur Elimination berechnen
    k = row2[pivot_index] / row1[pivot_index]
    steps += f"Zeilenoperation: R2 := R2 - ({k:>{COEFF_WIDTH}g}) · R1\n"

    # Zeilenoperation anwenden: R2 = R2 − k·R1
    for i in range(4):
        row2[i] = row2[i] - k * row1[i]

    steps += format_system_state(row1, row2, header="Neues System nach der Zeilenoperation:")

    # -------------------------------
    # 2. Entscheidung: parallel / identisch / schneidend
    # -------------------------------

    # Fall 1: 0x + 0y + 0z = d (d ≠ 0) → Widerspruch → keine Lösung → echt parallel
    if row2[0] == 0 and row2[1] == 0 and row2[2] == 0 and row2[3] != 0:
        steps += (
            "Zweite Zeile: 0·x + 0·y + 0·z = d (d ≠ 0) → "
            "Ebenen sind echt parallel (keine Schnittmenge).\n"
        )
        ind = 0
        equation = ""

    # Fall 2: 0x + 0y + 0z = 0 → Zeilen linear abhängig → Ebenen identisch
    elif row2[0] == 0 and row2[1] == 0 and row2[2] == 0 and row2[3] == 0:
        steps += (
            "Zweite Zeile: 0·x + 0·y + 0·z = 0 → "
            "Ebenen sind identisch (unendlich viele Lösungen).\n"
        )
        ind = 1
        equation = ""

    # Fall 3: zwei unabhängige Zeilen → Schnittgerade
    else:
        steps += (
            "Zwei unabhängige Zeilen → Ebenen schneiden sich in einer Geraden.\n"
        )
        ind = 2

        # TODO: Dozent fragen – ist Geometrie (Kreuzprodukt) zur Geradenbestimmung erlaubt,
        # oder muss die Parametergleichung rein über Gauß entstehen?

        # TODO: Implementierung der Geradengleichungsermittlung
        equation = ""

    return ind, equation, steps if vis_calc else "", file_save # Rechenschritte nur zurückgeben, falls vis_calc == True


def output_result(ind, equation, calc_steps, file_save):
    """
    Gibt das Ergebnis der Gauß-Berechnung in der Konsole aus
    und speichert es optional in einer Ausgabedatei.

    Parameter:
        ind (int):
            0 = Die Ebenen sind echt parallel (keine Schnittmenge)
            1 = Die Ebenen sind identisch (unendlich viele Lösungen)
            2 = Die Ebenen schneiden sich in einer Geraden
        equation (str):
            Enthält die Gleichung der Schnittgeraden, falls ind == 2.
            Ist ansonsten ein leerer String.
        calc_steps (str):
            Textdarstellung der Rechenschritte (falls vis_calc == True),
            sonst ein leerer String.
        file_save (bool):
            Falls True, wird die Ausgabe zusätzlich in die Datei
            NAME_OUTPUT_FILE geschrieben.

    Rückgabe:
        None
    """

    if calc_steps != "":
        print("Rechenschritte:\n\n" + calc_steps + "\n")
    
    if ind == 0:
        print("Die beiden Ebenen sind echt parallel.")
    elif ind == 1:
        print("Die beiden Ebenen sind identisch.")
    elif ind == 2:
        print("Die Schnittmenge der beiden Ebenen lautet: " + equation)
    else:
        print("Fehler: Indikator muss 0,1 oder 2 sein.")

    if file_save:
        try:
            with open(NAME_OUTPUT_FILE, "w") as f:
                if ind == 2:
                    f.write("Die Schnittmenge der beiden Ebenen lautet: " + equation)
                else:
                    # Alternativer Text, falls keine Gerade existiert
                    f.write("Kein eindeutige Schnittgerade vorhanden.\n")
        except Exception as e:
            print(f"Fehler beim Speichern: {e}")


if __name__ == "__main__":
    # Eingabedaten einlesen (entweder CLI oder Datei)
    e1, e2, vis_calc, file_save = read_input()

    # Gauß-Berechnung ausführen
    ind, equation, calc_steps, file_save = calc_gauss(e1, e2, vis_calc, file_save)

    # Ergebnis ausgeben
    output_result(ind, equation, calc_steps, file_save)