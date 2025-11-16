from Plane import Plane


NAME_INPUT_FILE = ""
NAME_OUTPUT_FILE = "output.txt"
DECIMAL_PLACCES = 3

def read_input():
    pass
# return Ebene: e1, Ebene: e2, bool: vis_calc, bool: file_save

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
            2 = Schnittmenge ist eine Gerade
        equation (str): Gleichung der Schnittgeraden (falls ind == 2, sonst "")
        calc_steps (str): Textdarstellung der Rechenschritte (optional)
        file_save (bool): Wird unverändert zurückgegeben
    """
    # TODO: Hier den eigentlichen Gauß-Algorithmus implementieren
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
        except FileNotFoundError:
            print(f"Fehler: {NAME_OUTPUT_FILE} nicht gefunden.")


if __name__ == "__main__":
    # Eingabedaten einlesen
    e1, e2, vis_calc, file_save = read_input()

    # Gauß-Berechnung ausführen
    ind, equation, calc_steps, file_save = calc_gauss(e1, e2, vis_calc, file_save)

    # Ergebnis ausgeben
    output_result(ind, equation, calc_steps, file_save)
 