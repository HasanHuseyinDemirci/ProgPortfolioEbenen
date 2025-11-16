from Plane import Plane


NAME_INPUT_FILE = ""
NAME_OUTPUT_FILE = "output.txt"
DECIMAL_PLACCES = 3

def read_input():
    """
    TODO: CLI- oder Datei-Eingabe implementieren.
    Platzhalter für Entwicklung.
    """
    return Plane(1, 1, 1, 3), Plane(1, -1, 1, 1), True, False


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

    # Ebenenkoeffizienten extrahieren
    a1, b1, c1, d1 = e1.as_tuple()
    a2, b2, c2, d2 = e2.as_tuple()

    # Rechenschritte protokollieren
    steps += "Ausgangssystem:\n"
    steps += f"{a1}·x + {b1}·y + {c1}·z = {d1}\n"
    steps += f"{a2}·x + {b2}·y + {c2}·z = {d2}\n\n"

    # -------------------------------
    # 1. Gauß-Schritt zur Klassifikation
    # -------------------------------

    # Falls a1 = 0 und a2 ≠ 0: Zeilen vertauschen, damit wir mit x eliminieren können
    if a1 == 0 and a2 != 0:
        steps += "Zeilen werden vertauscht, da a1 = 0 und a2 ≠ 0.\n"
        a1, b1, c1, d1, a2, b2, c2, d2 = a2, b2, c2, d2, a1, b1, c1, d1

    # Zeilenoperation R2 := R2 - k·R1 (falls a1 ≠ 0)
    if a1 != 0:
        k = a2 / a1
        steps += f"Zeilenoperation: R2 := R2 - ({k}) · R1\n"

        a2n = a2 - k * a1
        b2n = b2 - k * b1
        c2n = c2 - k * c1
        d2n = d2 - k * d1

        steps += "Neues System nach der Zeilenoperation:\n"
        steps += f"{a1}·x + {b1}·y + {c1}·z = {d1}\n"
        steps += f"{a2n}·x + {b2n}·y + {c2n}·z = {d2n}\n\n"
    else:
        # Sonderfall: beide a1 und a2 = 0 → wir vereinfachen nicht weiter
        a2n, b2n, c2n, d2n = a2, b2, c2, d2
        steps += "Kein Gauß-Schritt mit x möglich (a1 = a2 = 0).\n"
        # TODO: Sonderfall Klärung

    # Entscheidung anhand der zweiten Zeile
    if a2n == 0 and b2n == 0 and c2n == 0 and d2n != 0:
        # 0x + 0y + 0z = d (d ≠ 0) → Widerspruch → keine Lösung
        steps += "Zweite Zeile: 0x + 0y + 0z = d (d ≠ 0) → Ebenen sind echt parallel.\n"
        return 0, "", (steps if vis_calc else ""), file_save

    if a2n == 0 and b2n == 0 and c2n == 0 and d2n == 0:
        # 0x + 0y + 0z = 0 → Zeilen linear abhängig → Ebenen identisch
        steps += "Zweite Zeile: 0x + 0y + 0z = 0 → Ebenen sind identisch.\n"
        return 1, "", (steps if vis_calc else ""), file_save

    # Ansonsten: zwei unabhängige Zeilen → Ebenen schneiden sich in einer Geraden
    steps += "Zwei unabhängige Zeilen → Ebenen schneiden sich in einer Geraden.\n"


    # TODO: Dozent fragen – ist Geometrie (Kreuzprodukt) zur Geradenbestimmung erlaubt,
    # oder muss die Parametergleichung rein über Gauß entstehen?


    # TODO: Implementierung der Geradengleichungsermittlung
    pass


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
 