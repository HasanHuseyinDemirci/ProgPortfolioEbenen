import math
import csv

NAME_INPUT_FILE = "ebenen.csv"
NAME_OUTPUT_FILE = "output.txt"
COEFF_WIDTH = 8

ANSWER_YES = {"y", "yes","ja","j"}
ANSWER_NO = {"n", "no", "nein"}
ANSWER_TERMINAL = {"t", "terminal"}
ANSWER_CSV = {"csv", "c"}

def greet_user():
    """
    Begrüßung für den Nutzer
    """
    print(
            """
    Willkommen beim Ebenenrechner!
        
    Dieses Programm ermöglicht es, die Schnittmenge mehrerer Ebenen zu berechnen.  
    Du kannst die Ebenenkoeffizienten entweder über eine CSV-Datei einlesen oder direkt in der Kommandozeile eingeben.  
    Anschließend wird die Schnittmenge berechnet, und du kannst wählen, ob das Ergebnis als TXT-Datei exportiert werden soll oder direkt in der Kommandozeile ausgegeben wird.
            """)

def is_valid_number(value):
    """
    Prüft, ob eine Eingabe eine valide Zahl ist.
    Gibt einen boolschen Wert zurück
    """
    if  value == "":
        return False
    try:
        if math.isfinite(float(value)): 
            return True
        else:
            return False
    except ValueError:
        return False
    
def is_valid_plane(list_plane):
    """
    Prüft ob die Koeffizienten A,B,C nicht gleichzeitig 0 sind.
    Gibt einen boolschen Wert zurück
    """
    if list_plane[0] == 0 and list_plane[1] == 0 and list_plane[2] == 0:
        return False
    else:
        return True
    
def row_to_str(list_plane,index=None):
    """    
    Formatiert die Koeffizienten einer Ebene der Form [a, b, c, d] zu einer lesbaren 
    Gleichung ax +/- by +/- cz = d. Optional kann ein Index mit ausgegeben werden.
    """
    x, y, z, d = list_plane
    y_sign = '-' if y < 0 else '+'
    z_sign = '-' if z < 0 else '+'
    string = f"{x} x {y_sign} {abs(y)} y {z_sign} {abs(z)} z = {d}"

    if index is not None:
        return f"({index+1}) {string}"
    return string

def ask_user_bool_question(question):
    """
    Stellt dem Benutzer eine Ja/Nein-Frage und wartet auf eine gültige Antwort.
    Gibt einen boolschen Wert zurück.
    """
    while True:
        answer = input(f"{question}(j/n) ").lower().strip()
        if answer in ANSWER_YES:
            return True
        elif answer in ANSWER_NO:
            return False
        else:
            print("\nBitte erneut versuchen!\nDies ist nicht gültig, bitte versuche es mit Ja oder Nein.")

def print_csv_rows(rows):
    """
    Gibt CSV-Zeilen aus.
    """
    for row in rows:
        print(row)

def input_plane_terminal():
    """
    Liest im Terminal vier Koeffizienten einer Ebene ein und gibt die Liste [a, b, c, d] zurück.
    """
    while True:
        list_plane = [0, 0, 0, 0]
        list_plane_index = ["x", "y", "z", "d"]
        for i in range(len(list_plane)):

            value = ask_user_for_values(list_plane_index[i])
            value = value.replace(",", ".") # Kommazahlen (deutsche Eingabe wie 2,5) in Punktnotation (2.5) umwandeln
            list_plane[i] = float(value)

        if is_valid_plane(list_plane):
            if ask_user_bool_question(f"Ist dies deine Ebene?:\n{row_to_str(list_plane)}\n"):
                return list_plane
            else:
                print("Beginnen wir von vorne!")
                continue
        else:
            print("\nDie Ebene ist ungültig, da die Koeffizienten für x, y und z nicht alle 0 sein dürfen. Bitte erneut versuchen!")
            continue

def ask_user_for_values(coefficient):
    """
    Liest einen einzelnen Koeffizienten ein und gibt diesen zurück
    """
    while True:
        value = input(f"\nBitte gib einen gültigen Wert für {coefficient} an ")

        if is_valid_number(value):
            return value
            
        print("\nBitte erneut versuchen!")
    

def valid_rows(row, index_allowed, total_rows, index):
    """
    Speichert und formatiert eine gültige CSV-Zeile in total_rows und deren Index in index_allowed,
    und gibt beide Listen zurück.
    """
    index_allowed.append(index+1)
    total_rows.append(row_to_str(row, index))
    return index_allowed, total_rows

def invalid_rows(rows_unallowed, index_unallowed, total_rows, index):
    """
    Speichert und formatiert eine ungültige CSV-Zeile in total_rows und deren Index in index_unallowed,
    und gibt beide Listen zurück.
    """
    rows_unallowed.append(f"(X)  Zeile {index + 1} in der CSV-Datei ist ungültig und wird übersprungen.")
    index_unallowed.append(index+1)
    total_rows.append(f"(X)  Zeile {index + 1} in der CSV-Datei ist ungültig und wird übersprungen.")
    return rows_unallowed, index_unallowed, total_rows

def validate_csv_planes(reader):
    """
    Prüft alle Zeilen der CSV-Datei auf Anzahl und Zahlformat.
    Gib total_rows, index_allowed zurück
    """
    rows_unallowed = []
    index_unallowed = []
    index_allowed = []
    total_rows = []
    for index, row in enumerate(reader):
        try:
            if len(row) != 4:
                raise ValueError("Ungültige Zeile")
            float_row = [float(cell) for cell in row]
            if not all(math.isfinite(val) for val in float_row):
                raise ValueError("Ungültige Zeile")
            
            if float_row[0] == 0 and float_row[1] == 0 and float_row[2] == 0:
                raise ValueError("Ungültige Zeile")

            index_allowed,total_rows = valid_rows(float_row,index_allowed, total_rows, index)
        except ValueError:
            rows_unallowed, index_unallowed, total_rows = invalid_rows(rows_unallowed, index_unallowed,total_rows, index)

    if len(index_allowed) <2:
        print("\nDie CSV-Datei muss mindestens zwei Ebenen enthalten.")
        return None, None
    return total_rows, index_allowed

def load_csv_file(path):
    """
    Lädt CSV-Datei und gibt Zeilen zurück.
    """
    try:
        with open(path, mode="r", encoding="utf-8")as f:
            return list(csv.reader(f))
    except Exception as e: 
        print(f"\nFehler beim Öffnen der Datei: {e}")
        return None
    
def choose_two_planes(index_allowed):
    """
    Lässt den Nutzer zwei Ebenen wählen und überprüft ob sie Möglich sind.
    Gibt die gewählten Indizes zurück.
    """
    while True:
        choice = input("Bitte gib zwei Ebenen mit einem \",\" voneinander getrennt ein: ").split(",")
        if len(choice) != 2:
            print("\nWähle bitte genau zwei Ebenen aus.")
            continue
        if not all(c.strip().isdigit() for c in choice):
            print("\nEs sind nur Zahlen erlaubt")
            continue

        choice[0] = int(choice[0])
        choice[1] = int(choice[1])
        
        if choice[0] == choice[1]:
            print("\nDu kannst nicht dieselben Ebenen wählen")
            continue

        if not (choice[0] in index_allowed and choice[1] in index_allowed):
            print("\nDie angegebenen Ebenen sind außerhalb des gültigen Bereichs")
            continue
        
        return choice[0], choice[1]
    
def input_plane_csv():
    """
    Liest Ebenenkoeffizienten aus einer CSV-Datei und validiert die Daten.
    Gibt Ebenen als Listen [a, b, c, d] zurück
    """
    reader = load_csv_file(NAME_INPUT_FILE)

    if reader is None:
        print("\n Fehler: CSV-Datei konnte  nicht geladen werden.")
        return None, None
    
    validated = validate_csv_planes(reader)

    if validated == (None, None):
        return None, None
    
    total_rows, index_allowed = validated
    print_csv_rows(total_rows)

    while True:
        choice_1, choice_2 = choose_two_planes(index_allowed)
        if ask_user_bool_question(f"\nDu hast Ebene {choice_1} und Ebene {choice_2} angegeben stimmt dies? "):
            e1 = [float(x) for x in reader[choice_1-1]]
            e2 = [float(x) for x in reader[choice_2-1]]
            return e1, e2
        else:
            print("\nBitte erneut versuchen.")

def ask_terminal_or_csv():
    """
    Fragt User über Inputpräferenz und gibt eine formatierte Antwort zurück
    """
    return input("Bevor wir beginnen, willst du deine " \
    "Ebenen im Terminal eingeben oder aus einer CSV Datei auslesen? (T/CSV) ").lower().strip()

def read_input():
    """
    Liest zwei Ebenen ein und ermittelt die Programmeinstellungen.
    """

    greet_user()
    show_calculation_steps = ask_user_bool_question("Willst du die Rechenschritte im Terminal anzeigen ")
    save_output_in_file = ask_user_bool_question("Willst du das Ergebnis in einer Textdatei speichern ")


    while True:
        question_terminal_csv = ask_terminal_or_csv()

        if question_terminal_csv in ANSWER_TERMINAL:
            print("Beginnen wir mit der ersten Ebene:")
            e1 = input_plane_terminal()

            print("Jetzt die zweite Ebene:")
            e2 = input_plane_terminal()
            break

        elif question_terminal_csv in ANSWER_CSV:
            e1, e2 = input_plane_csv()
            if e1 is None or e2 is None:
                print("\nDie von dir übergebene hat nicht genug Einträge")
                continue
            break

        else:
            print("Ungültige Eingabe. Bitte 'T' für Terminal oder 'CSV' für CSV-Datei eingeben.")
            continue

    return e1, e2, show_calculation_steps, save_output_in_file 


def format_system_state(row1, row2, header=None):
    """
    Formatiert den aktuellen Zustand des linearen Gleichungssystems
    mit zwei Ebenengleichungen als Textblock für die Rechenschritte.

    Parameter:
        row1, row2: Listen der Form [a, b, c, d]
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


def det2x2(a, b, c, d): 
    """
    Berechnet die Determinante einer 2x2-Matrix und gibt diese zurück:
        | a  b |
        | c  d |
    """
    return a * d - b * c


def calc_gauss(row1, row2, vis_calc):
    """
    Führt den Gauß-Algorithmus für zwei Ebenen durch und bestimmt ihre Lagebeziehung.

    e1, e2: Sequenzen der Form [a, b, c, d] mit ax + by + cz = d.
    vis_calc: bool – Wenn True, werden die Rechenschritte als Text mit zurückgegeben.

    Rückgabe:
    result: str – Beschreibung der Lagebeziehung bzw. Parametergleichung der Schnittgeraden.
    calc_steps: str – Formatierte Rechenschritte oder "" (wenn vis_calc False ist).
    """

    steps = "\n\n======= Gauß-Berechnung für zwei Ebenen =======\n"

    # Ausgangssystem speichern
    steps += format_system_state(row1, row2, header="(1) Ausgangssystem:")

    # 1. Gauß-Schritt: Pivot suchen und zweite Zeile eliminieren

    # Pivot-Spalte bestimmen: zuerst x, dann y, sonst z
    if row1[0] != 0 or row2[0] != 0: # 0 = x, 1 = y, 2 = z
        pivot_index = 0
    elif row1[1] != 0 or row2[1] != 0:
        pivot_index = 1
    else:
        pivot_index = 2

    pivot_name = ["x", "y", "z"][pivot_index]
    steps += f"(2) Führendes Element: Spalte '{pivot_name}'\n"

    # Falls Pivot in Zeile 1 = 0 -> Zeilen tauschen
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
    
    # 2. Entscheidung: parallel / identisch / schneidend

    steps += "(4) Klassifikation des Falls:\n"

    a1, b1, c1, d1 = row1
    a2, b2, c2, d2 = row2
    
    # Fall 1: 0x + 0y + 0z = d (d != 0) -> Widerspruch -> keine Lösung -> echt parallel
    if a2 == 0 and b2 == 0 and c2 == 0 and d2 != 0:
        steps += (
            f"Zweite Zeile: 0·x + 0·y + 0·z = {d2:g} ({d2:g} != 0)\n"
        )
        result = "Die Ebenen sind echt parallel und haben keine Schnittmenge."

    # Fall 2: 0x + 0y + 0z = 0 -> Zeilen linear abhängig -> Ebenen identisch
    elif a2 == 0 and b2 == 0 and c2 == 0 and d2 == 0:
        steps += "Zweite Zeile: 0·x + 0·y + 0·z = 0 \n"
        result = "Die Ebenen sind identisch und haben unendlich viele Schnittpunkte."

    # Fall 3: zwei unabhängige Zeilen -> Schnittgerade
    else:

        # 3. Schnittgerade mit Determinanten
        
        # 2×2-Determinanten der Koeffizientenmatrix
        # Sie entscheiden, welche Variable frei gewählt werden kann.
        D_xy = det2x2(a1, b1, a2, b2)   # Determinante des Systems in x,y
        D_xz = det2x2(a1, c1, a2, c2)   # Determinante des Systems in x,z
        D_yz = det2x2(b1, c1, b2, c2)   # Determinante des Systems in y,z

        # Fall 1:
        # D_xy != 0 -> Das 2×2-System in x und y ist eindeutig lösbar
        if D_xy != 0:
            # Führendes Gleichungssystem in x,y – z wird Parameter t
            steps += "Wir wählen z als Parameter: z = t und lösen das 2x2-System in x und y.\n"

            # Für t = 0 erhalten wir den Stützpunkt:
            # (x0, y0, z0)
            x0 = det2x2(d1, b1, d2, b2) / D_xy
            y0 = det2x2(a1, d1, a2, d2) / D_xy
            z0 = 0.0

            # Für t != 0 berechnen wir den Richtungsvektor (vx, vy, vz)
            vx = -det2x2(c1, b1, c2, b2) / D_xy
            vy = -det2x2(a1, c1, a2, c2) / D_xy
            vz = 1.0  # z = t

        # Fall 2:
        # D_xz != 0 -> y = t ist sinnvoll
        elif D_xz != 0:
            steps += "Wir wählen y als Parameter: y = t und lösen das 2x2-System in x und z.\n"

            x0 = det2x2(d1, c1, d2, c2) / D_xz
            y0 = 0.0
            z0 = det2x2(a1, d1, a2, d2) / D_xz

            vx = -det2x2(b1, c1, b2, c2) / D_xz
            vy = 1.0  # y = t
            vz = -det2x2(a1, b1, a2, b2) / D_xz

        # Fall 3:
        # D_yz != 0 -> x = t ist sinnvoll
        elif D_yz != 0:
            steps += "Wir wählen x als Parameter: x = t und lösen das 2x2-System in y und z.\n"

            x0 = 0.0
            y0 = det2x2(d1, c1, d2, c2) / D_yz
            z0 = det2x2(b1, d1, b2, d2) / D_yz

            vx = 1.0  # x = t
            vy = -det2x2(a1, c1, a2, c2) / D_yz
            vz = -det2x2(b1, a1, b2, a2) / D_yz  

        else:
            # Theoretisch dürfte dieser Fall bei ind = 2 nicht auftreten

            result = "WARNUNG: Alle 2x2-Minoren sind 0, obwohl zwei unabhängige Zeilen erwartet wurden.\n"
            
            return result, steps if vis_calc else "" # Rechenschritte nur zurückgeben, falls vis_calc == True


        # Parametergleichung der Schnittgeraden
        equation = f"g(t) = ({x0:g}, {y0:g}, {z0:g}) + t · ({vx:g}, {vy:g}, {vz:g})"

        result = f"Schnittgerade (Parametergleichung):\n    {equation}\n"

        
    steps += "\nErgebnis: "
    
    return result, steps if vis_calc else "" # Rechenschritte nur zurückgeben, falls vis_calc == True



def output_result(result, calc_steps):
    """
    Gibt optional Rechenschritte und danach das Ergebnis aus.
    """
    if calc_steps != "":
        print(calc_steps)

    print(result)

    
def save_output_in_file(result):
    """
    Speichert das Ergebnis in die Ausgabedatei.
    """
    try:
        with open(NAME_OUTPUT_FILE, "w") as f:
            f.write(result)
           
    except Exception as e:
        print(f"Fehler beim Speichern: {e}")



if __name__ == "__main__":
    # Eingabedaten einlesen (entweder CLI oder Datei)
    e1, e2, vis_calc, file_save = read_input()

    # Gauß-Berechnung ausführen
    result, calc_steps = calc_gauss(e1, e2, vis_calc)

    # Ergebnis ausgeben
    output_result(result, calc_steps)

    if file_save:
        save_output_in_file(result)