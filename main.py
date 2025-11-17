from Plane import Plane
import csv

NAME_INPUT_FILE = ""
NAME_OUTPUT_FILE = "output.txt"
# DECIMAL_PLACES = 3
COEFF_WIDTH = 8

ANSWER_YES = {"y", "yes","ja","j"}
ANSWER_NO = {"n", "no", "nein"}
ANSWER_TERMINAL = {"t", "terminal"}
ANSWER_CSV = {"csv", "c"}
save_calculation_steps = None

#TODO: Dokumentation der Funktionen
#TODO: Ausführichliche Kommentare
#TODO: Testen




def input_plane_terminal():
    """
    Diese funktion ist in der Lage, eine ebene über die Command line als dictionary zu erschaffen und diese auch als solches zurück zu geben. 
    """
    while True:
        list_plane = [0, 0, 0, 0]
        list_plane_index = ["x", "y", "z", "d"]
        for i in range(len(list_plane)):
            while True:
                list_plane[i] = input(f"Bitte gib einen gültigen Wert für {list_plane_index[i]} an ")
                try:
                    if list_plane[i] == "" or list_plane[i] in ("inf","-inf"):
                        print("Bitte erneut versuchen!")
                        continue
                    else:
                        list_plane[i] = float(list_plane[i])
                        break
                except ValueError:
                    print("Bitte erneut versuchen!")
                    continue
        if ask_user_if_plane_is_correct(list_plane):
            return list_plane
        else:
            print("Beginnen wir von vorne!")
        
def ask_user_if_plane_is_correct(list_plane):
    while True:
        ask_is_plane_correct = input(f"""
ist dies Ebene? (j/n) 
{list_plane[0]} x1 + {list_plane[1]} x2 + {list_plane[2]} x3 {"-" if list_plane[3] <= 0 else "+"} {list_plane[3]} = 0
""" )
        if ask_is_plane_correct.lower().strip() in ANSWER_NO:
            return False
        elif ask_is_plane_correct.lower().strip() in ANSWER_YES:
            return True  
        else:
            print("Bitte erneut versuchen! (j/n) ")
            continue  


def start_plane_calculator():
    print(
            """
    Willkommen beim Ebenenrechner!
        
    Dieses Programm ermöglicht es, die Schnittmenge mehrerer Ebenen zu berechnen.  
    Du kannst die Ebenenkoeffizienten entweder über eine CSV-Datei einlesen oder direkt in der Kommandozeile eingeben.  
    Anschließend wird die Schnittmenge berechnet, und du kannst wählen, ob das Ergebnis als CSV-Datei exportiert werden soll oder direkt in der Kommandozeile ausgegeben wird.
            """)

def ask_user_calculation_steps_preferences():
    # global save_calculation_steps
    while True:
        answer = input("Willst du die Rechenschritte Speichern? (j/n) ")
        if answer.lower() in ANSWER_YES:
            save_calculation_steps = True
            break
        elif answer.lower() in ANSWER_NO:
            save_calculation_steps = False
            break
        print("""
        Bitte erneut versuchen!
        Dies ist nicht Gültig bitte versuche es mit Ja oder mit Nein
                """)
    return save_calculation_steps

def input_plane_csv(): 
    index_unallowed = []

    while True:
        try:
            with open("ebenen.csv", mode="r", encoding="utf-8") as csvfile:
                reader = list(csv.reader(csvfile))
                total_rows = len(reader)      

                if len(reader) == 0:
                    print("Die CSV-Datei ist leer.")
                    return None, None
                for index, row in enumerate(reader):
                    if len(row) == 4:
                        try:
                            [float(cell) for cell in row]
                        except ValueError:
                            print(index+1, f"Zeile {index + 1} in der CSV-Datei ist ungültig und wird übersprungen.")
                            index_unallowed.append(index + 1)
                            continue
                        print(index+1,row)
                    else:
                        print(index+1, f"Zeile {index + 1} in der CSV-Datei ist ungültig und wird übersprungen.")
                        index_unallowed.append(index + 1)

                while True:
                    input_choice_of_plane =  input("Bitte wähle zwei Ebenen durch ihre Nummern aus, getrennt durch ein Komma: ").split(",")
                    if (len(input_choice_of_plane) != 2 or not input_choice_of_plane[0].strip().isdigit() or not input_choice_of_plane[1].strip().isdigit()):
                        print("Bitte genau zwei Ebenennummern angeben.")
                        continue
                                
                    input_plane_csv_1 = int(input_choice_of_plane[0].strip())
                    input_plane_csv_2 = int(input_choice_of_plane[1].strip())


                    if (
                            1 <= input_plane_csv_1 <= total_rows and
                            1 <= input_plane_csv_2 <= total_rows and
                            input_plane_csv_1 not in index_unallowed and
                            input_plane_csv_2 not in index_unallowed
                        ):

                        plane_check = input("Du hast die Ebenen " + str(input_plane_csv_1) + " und " + str(input_plane_csv_2) + " ausgewählt. Ist das korrekt? (j/n) ")
                        if plane_check.lower() in ANSWER_YES:
                            row1 = reader[input_plane_csv_1 - 1]
                            row2 = reader[input_plane_csv_2 - 1]
                            e1 = {"x": float(row1[0]), "y": float(row1[1]), "z": float(row1[2]), "d": float(row1[3])}
                            e2 = {"x": float(row2[0]), "y": float(row2[1]), "z": float(row2[2]), "d": float(row2[3])}
                            return e1, e2
                        else:
                            print("Bitte erneut versuchen.")
                            continue
        except FileNotFoundError:
            print("Die Datei 'ebenen.csv' wurde nicht gefunden. Bitte stelle sicher, dass sie im gleichen Verzeichnis wie dieses Programm liegt.")
            return None, None

def read_input():
    #TODO: NaN überprüfen
    #TODO auf 0x + 0y + 0z = d prüfen
    #TODO: Fragen nach Dateispeicherung

    global save_calculation_steps
    start_plane_calculator()
    save_calculation_steps = ask_user_calculation_steps_preferences()

    while True:
        file_or_terminal = input("Bevor wir beginnen, willst du deine ebenen im Terminal eingeben oder aus einer CSV Datei auslesen? (T/CSV) ")
        if file_or_terminal.lower() in ANSWER_TERMINAL:
            print("Beginnen wir mit der ersten Ebene:")
            e1 = input_plane_terminal()
            print("Sehr gut!")
            print("Jetzt die zweite Ebene:")
            e2 = input_plane_terminal()
                
            break
        elif file_or_terminal.lower() in ANSWER_CSV:
            e1, e2 = input_plane_csv()
            if e1 is None or e2 is None:
                continue
            break
        else:
            print("Ungültige Eingabe. Bitte 'T' für Terminal oder 'CSV' für CSV-Datei eingeben.")

    e1 = Plane(e1[0], e1[1], e1[2], e1[3])
    e2 = Plane(e2[0], e2[1], e2[2], e2[3])
    
    return e1, e2, save_calculation_steps, False 


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


def det2(a, b, c, d): #TODO Testfunktion schreiben
    """
    Berechnet die Determinante einer 2x2-Matrix:
        | a  b |
        | c  d |
    """
    return a * d - b * c


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

    steps = "=== Gauß-Berechnung für zwei Ebenen ===\n"

     # Koeffizienten der Ebenen als Listen
    row1 = e1.as_list()  # [a1, b1, c1, d1]
    row2 = e2.as_list()  # [a2, b2, c2, d2]

    # Ausgangssystem speichern
    steps += format_system_state(row1, row2, header="(1) Ausgangssystem:")

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
    steps += f"(2) Führendes Element: Spalte '{pivot_name}'\n"

    # Falls Pivot in Zeile 1 = 0 → Zeilen tauschen
    if row1[pivot_index] == 0 and row2[pivot_index] != 0:
        steps += (f"Zeilen werden vertauscht, da das führende Element in Zeile 1 = 0 ist (Spalte {pivot_name}).\n")
        row1, row2 = row2, row1
        steps += format_system_state(row1, row2, header="Nach Zeilenvertauschung:")

     # Faktor k zur Elimination berechnen
    k = row2[pivot_index] / row1[pivot_index]
    steps += f"    Zeilenoperation: R2 := R2 - ({k:g}) · R1\n"

    # Zeilenoperation anwenden: R2 = R2 − k·R1
    for i in range(4):
        row2[i] = row2[i] - k * row1[i]

    steps += format_system_state(row1, row2, header="(3) Neues System nach der Zeilenoperation:")
    

    # -------------------------------
    # 2. Entscheidung: parallel / identisch / schneidend
    # -------------------------------

    steps += "(4) Klassifikation des Falls:\n"

    a1, b1, c1, d1 = row1
    a2, b2, c2, d2 = row2
    
    # Fall 1: 0x + 0y + 0z = d (d ≠ 0) → Widerspruch → keine Lösung → echt parallel
    if a2 == 0 and b2 == 0 and c2 == 0 and d2 != 0:
        steps += (
            f"Zweite Zeile: 0·x + 0·y + 0·z = {d1:g} ({d1:g} ≠ 0) → Ebenen sind echt parallel (keine Schnittmenge).\n"
        )
        ind = 0
        equation = ""

    # Fall 2: 0x + 0y + 0z = 0 → Zeilen linear abhängig → Ebenen identisch
    elif a2 == 0 and b2 == 0 and c2 == 0 and d2 == 0:
        steps += "Zweite Zeile: 0·x + 0·y + 0·z = 0 → Ebenen sind identisch (unendlich viele Lösungen).\n"
        ind = 1
        equation = ""

    # Fall 3: zwei unabhängige Zeilen → Schnittgerade
    else:
        steps += (
            "Zwei unabhängige Zeilen → Schnittgerade existiert.\n"
        )
        ind = 2

        # -------------------------------
        # 3. Schnittgerade mit Determinanten (Cramersche Regel)
        # -------------------------------
        

        # 2×2-Determinanten der Koeffizientenmatrix
        # Sie entscheiden, welche Variable frei gewählt werden kann.
        D_xy = det2(a1, b1, a2, b2)   # Determinante des Systems in x,y
        D_xz = det2(a1, c1, a2, c2)   # Determinante des Systems in x,z
        D_yz = det2(b1, c1, b2, c2)   # Determinante des Systems in y,z

        # Fall 1:
        # D_xy ≠ 0 → Das 2×2-System in x und y ist eindeutig lösbar
        if D_xy != 0:
            # Führendes Gleichungssystem in x,y – z wird Parameter t
            steps += "Wir wählen z als Parameter: z = t und lösen das 2x2-System in x und y.\n"

            # Für t = 0 erhalten wir den Stützpunkt:
            # (x0, y0, z0)
            x0 = det2(d1, b1, d2, b2) / D_xy
            y0 = det2(a1, d1, a2, d2) / D_xy
            z0 = 0.0

            # Für t ≠ 0 berechnen wir den Richtungsvektor (vx, vy, vz)
            vx = -det2(c1, b1, c2, b2) / D_xy
            vy = -det2(a1, c1, a2, c2) / D_xy
            vz = 1.0  # z = t

        # Fall 2:
        # D_xz ≠ 0 → y = t ist sinnvoll
        elif D_xz != 0:
            steps += "Wir wählen y als Parameter: y = t und lösen das 2x2-System in x und z.\n"

            x0 = det2(d1, c1, d2, c2) / D_xz
            y0 = 0.0
            z0 = det2(a1, d1, a2, d2) / D_xz

            vx = -det2(b1, c1, b2, c2) / D_xz
            vy = 1.0  # y = t
            vz = -det2(a1, b1, a2, b2) / D_xz

        # Fall 3:
        # D_yz ≠ 0 → x = t ist sinnvoll
        elif D_yz != 0:
            steps += "Wir wählen x als Parameter: x = t und lösen das 2x2-System in y und z.\n"

            x0 = 0.0
            y0 = det2(d1, c1, d2, c2) / D_yz
            z0 = det2(b1, d1, b2, d2) / D_yz

            vx = 1.0  # x = t
            vy = -det2(a1, c1, a2, c2) / D_yz
            vz = -det2(b1, a1, b2, a2) / D_yz  # äquivalent umgeformt

        else:
            # Theoretisch dürfte dieser Fall bei ind = 2 nicht auftreten
            steps += (
                "WARNUNG: Alle 2x2-Minoren sind 0, obwohl zwei unabhängige Zeilen erwartet wurden.\n"
            )
            equation = ""
            return ind, equation, steps if vis_calc else "", file_save


        # Parametergleichung der Schnittgeraden
        equation = f"g(t) = ({x0:g}, {y0:g}, {z0:g}) + t · ({vx:g}, {vy:g}, {vz:g})"

        steps += f"\n(5) Schnittgerade (Parametergleichung):\n    {equation}\n"

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

"""
if __name__ == "__main__":
    # Eingabedaten einlesen (entweder CLI oder Datei)
    e1, e2, vis_calc, file_save = read_input()

    # Gauß-Berechnung ausführen
    result, calc_steps = calc_gauss(e1, e2, vis_calc)

    # Ergebnis ausgeben
    output_result(result, calc_steps)

    if file_save:
        save_output_in_file(result)


"""