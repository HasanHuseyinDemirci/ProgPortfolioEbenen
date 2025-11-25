#from Plane import Plane
import math
import csv

NAME_INPUT_FILE = ""
NAME_OUTPUT_FILE = "output.txt"
# DECIMAL_PLACES = 3
COEFF_WIDTH = 8

ANSWER_YES = {"y", "yes","ja","j"}
ANSWER_NO = {"n", "no", "nein"}
ANSWER_TERMINAL = {"t", "terminal"}
ANSWER_CSV = {"csv", "c"}

#TODO: Dokumentation der Funktionen
#TODO: Ausführichliche Kommentare
#TODO: Testen

def start_plane_calculator():
    """
    Begrüßung für den Nutzer
    """
    print(
            """
    Willkommen beim Ebenenrechner!
        
    Dieses Programm ermöglicht es, die Schnittmenge mehrerer Ebenen zu berechnen.  
    Du kannst die Ebenenkoeffizienten entweder über eine CSV-Datei einlesen oder direkt in der Kommandozeile eingeben.  
    Anschließend wird die Schnittmenge berechnet, und du kannst wählen, ob das Ergebnis als CSV-Datei exportiert werden soll oder direkt in der Kommandozeile ausgegeben wird.
            """)


def is_valid_number(value):
    """
    Prüft ob ein Wert in eine endliche Zahl umwandelbar ist.
    """

    try:
        # Versucht, den Wert in einen float umzuwandeln.
        # math.isfinite() prüft auf numerische Endlichkeit (nicht NaN oder Inf)
        # Die Prüfung auf value != "" schließt leere Strings aus, da float("") einen ValueErrorauslösen würde, den wir abfangen aber ein leerer String per Definition keine gültige Zahl ist.
        if math.isfinite(float(value)) and value != "": 
            return True
        else:
            return False
    except ValueError:
        # Wird ausgelöst beinicht numerischen Strings
        return False
    


def is_valid_plane(list_plane):
    """
    Prüft ob A,B,C nicht gleichzeitig 0 sind und lässt sich bestätigen, dass der Nutzer die richtige Ebene eingegeben hat.
    """
    if list_plane[0] == 0 and list_plane[1] == 0 and list_plane[2] == 0:
            print("\nDie Ebene ist ungültig, da die Koeffizienten für x, y und z nicht alle 0 sein dürfen. Bitte erneut versuchen!")
            return False
    else:
        if ask_user_if_plane_is_correct(list_plane):
            return list_plane
        else:
            print("\nBeginnen wir von vorne!")
      
            
def ask_user_if_plane_is_correct(list_plane):
    """
    Fragt Nutzer, ob er die richtige Ebene eingegeben hat.
    """

    while True:
        ask_is_plane_correct = input(f"\nist dies Ebene? (j/n) \n{list_plane[0]} x1 + {list_plane[1]} x2 + {list_plane[2]} x3 {"-" if list_plane[3] <= 0 else "+"} {list_plane[3]} = 0 " )
        if ask_is_plane_correct.lower().strip() in ANSWER_NO:
            return False
        elif ask_is_plane_correct.lower().strip() in ANSWER_YES:
            return True  
        else:
            print("Bitte erneut versuchen! (j/n) ")
            continue  







def ask_user_bool_question(question):
    """
    Stellt dem Benutzer eine Ja/Nein-Frage und wartet auf eine gültige Antwort.

    Die Funktion läuft in einer Endlosschleife (`while True`), bis der Benutzer 
    eine Antwort eingibt, die in den extern definierten Mengen `ANSWER_YES` oder 
    `ANSWER_NO` enthalten ist (nachdem die Antwort in Kleinbuchstaben umgewandelt 
    und Leerzeichen entfernt wurden).

    Wenn die Eingabe ungültig ist, wird der Benutzer aufgefordert, es erneut zu versuchen.

    :param question: Der Text der dem Benutzer gestellten Frage. 
                     Ein "(j/n) " wird automatisch an die Frage angehängt.
    :type question: str
    :raises NameError: Falls die externen Konstanten `ANSWER_YES` oder `ANSWER_NO` 
                       nicht definiert sind, schlägt die Funktion fehl.
    :returns: **True**, wenn die Antwort als "Ja" interpretiert wird, 
              **False**, wenn die Antwort als "Nein" interpretiert wird.
    :rtype: bool
    """
    while True:
        answer = input(question + " (j/n) ")
        if answer.lower().strip() in ANSWER_YES:
            return True
        elif answer.lower().strip() in ANSWER_NO:
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
    Baut eine Ebene über Terminaleingaben zusammen
    """
    while True:
        list_plane = [0, 0, 0, 0]
        list_plane_index = ["x", "y", "z", "d"]
        for i in range(len(list_plane)):
            while True:
                if ask_user_for_values(i,list_plane_index,list_plane) == False:
                    continue
                else:
                    break
        if is_valid_plane(list_plane):
            return list_plane
        

def ask_user_for_values(i,list_plane_index,list_plane):
    """
    Liest einen einzelnen Koeffizienten ein.
    """
    list_plane[i] = input(f"\nBitte gib einen gültigen Wert für {list_plane_index[i]} an ")
    if is_valid_number(list_plane[i]) == False:
        print("\nBitte erneut versuchen!")
        return False
    else:
        list_plane[i] = float(list_plane[i])
        return True


def row_to_str(index, row):
    """
    Formatiert eine Ebenengleichung als String.
    """
    return f"({index+1})  {row[0]}x {'-' if float(row[1]) <= 0 else '+'} {abs(float(row[1]))}y {'-' if float(float(row[2])) <= 0 else '+'} {abs(float(row[2]))}z {'-' if float(row[3]) >= 0 else '+'} {abs(float(row[3]))} = 0"


def possible_row(row,rows_allowed, index_allowed, total_rows, index):
    """
    Speichert und Formatiert eine gültige CSV-Zeile und deren Index
    """
    rows_allowed.append(row_to_str(index, row))
    index_allowed.append(index+1)
    total_rows.append(row_to_str(index, row))
    return rows_allowed,index_allowed,total_rows

def impossible_row(rows_unallowed, index_unallowed, total_rows, index):
    """
    Speichert und Formatiert ungültige CSV-Zeilen und deren Index
    """
    rows_unallowed.append(f"(X)  Zeile {index + 1} in der CSV-Datei ist ungültig und wird übersprungen.")
    index_unallowed.append(index+1)
    total_rows.append(f"(X)  Zeile {index + 1} in der CSV-Datei ist ungültig und wird übersprungen.")
    return rows_unallowed,index_unallowed,total_rows

def validate_csv_planes(reader):
    """
    Prüft alle Zeilen der CSV-Datei auf Anzahl und Zahlformat.
    """
    rows_unallowed = []
    index_unallowed = []
    rows_allowed = []
    index_allowed = []
    total_rows = []
    for index, row in enumerate(reader):
        if len(row) == 4:
            try:
                [math.isfinite(float(cell)) for cell in row]
                rows_allowed, index_allowed, total_rows = possible_row(row,rows_allowed, index_allowed, total_rows, index)
            except ValueError:
                rows_unallowed,index_unallowed,total_rows = impossible_row(rows_unallowed, index_unallowed, total_rows, index)
                # immposible_row = [row in total_rows if row not in possible_rows]
                continue
        else:
            rows_unallowed,index_unallowed,total_rows = impossible_row(rows_unallowed, index_unallowed, total_rows, index)
            
    

    if len(reader)-len(rows_unallowed) < 1:
        print("\nDie CSV-Datei muss mindestens zwei Ebenen enthalten.")
        return False
    return reader, total_rows,index_allowed

def load_csv_file(path):
    """
    Lädt CSV-Datei und giebt Zeilen zurück.
    """
    try:
        with open(path, mode="r", encoding="utf-8")as f:
            return list(csv.reader(f))
    except Exception as e: #FileNotFoundError:
        print(f"\n{e}") #TODO Ausführicher beschreiben
        return None
    
def choose_two_planes(index_allowed):
    """
    Lässt den Nutzer zwei Ebenen wählen und überprüft ob sie Möglich sind.
    """
    while True:
        choice = input("\nBitte wähle zwei Ebenen durch ihre Nummern aus, getrennt durch ein Komma: ").strip().split(",")
        if len(choice) != 2:
            print("\nBitte genau zwei Ebenennummern angeben.")
            continue
        if not all(c.strip().isdigit() for c in choice):
            print("\nEs sind nur Zahlen erlaubt")
            continue
        if choice[0] == choice[1]:
            print("\nDu kannst nicht die selben ebenen wählen")
            continue
        if not (int(choice[0]) in index_allowed and int(choice[1]) in index_allowed):
            print("\nDie angegebenen Ebenen sind außerhalb des gültigen Bereichs")
            continue
        
        return int(choice[0]),int(choice[1])
    


def confirm_choice(choice_1, choice_2):# TODO mach zu question
    confirm = input(f"\nDu hast Ebene {choice_1} und Ebene {choice_2} angegeben stimmt dies? (j/n)")
    return confirm in ANSWER_YES

def input_plane_csv():
    """
    Ließt Ebenenkoeffizienten aus einer CSV-Dateiund validiert die Daten.
    """
    reader = load_csv_file("ebenen.csv")
    if reader is None:
        return None, None
    validated = validate_csv_planes(reader)

    if validated is False:
        return None, None
    
    reader, total_rows,index_allowed= validated

    print_csv_rows(total_rows)

    while True:
        choice_1 , choice_2 = choose_two_planes(index_allowed)
        if confirm_choice(choice_1,choice_2):
            return reader[choice_1-1], reader[choice_2-1]
        else:
            print("\nBitte erneut versuchen. ")





def read_input():
    """
    Liest zwei Ebenenein und ermittelt die Programmeinstellungen.
    """
    #TODO: NaN überprüfen
    #TODO: Fragen nach Dateispeicherung

    start_plane_calculator()
    show_calculation_steps = ask_user_bool_question("Willst du die Rechenschritte im Terminal anzeigen")
    save_output_in_file = ask_user_bool_question("Willst du das Ergebnis in einer Text Datei speichern")


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
                print("\n Die von dir übergebene hat nicht genug Einträge")
                continue
            e1 = [float(e1[0]), float(e1[1]), float(e1[2]), float(e1[3])]
            e2 = [float(e2[0]), float(e2[1]), float(e2[2]), float(e2[3])]
            break
        else:
            print("Ungültige Eingabe. Bitte 'T' für Terminal oder 'CSV' für CSV-Datei eingeben.")
            continue

    #e1 = Plane(float(e1[0]), float(e1[1]), float(e1[2]), float(e1[3]))
    #e2 = Plane(float(e2[0]), float(e2[1]), float(e2[2]), float(e2[3]))

    
    return e1, e2, show_calculation_steps, save_output_in_file 


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


def calc_gauss(e1, e2, vis_calc):
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
    row1 = e1#.as_list()  # [a1, b1, c1, d1]
    row2 = e2#.as_list()  # [a2, b2, c2, d2]

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
    
    # 2. Entscheidung: parallel / identisch / schneidend

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

        # 3. Schnittgerade mit Determinanten (Cramersche Regel)
        
        # 2×2-Determinanten der Koeffizientenmatrix
        # Sie entscheiden, welche Variable frei gewählt werden kann.
        D_xy = det2(a1, b1, a2, b2)   # Determinante des Systems in x,y
        D_xz = det2(a1, c1, a2, c2)   # Determinante des Systems in x,z
        D_yz = det2(b1, c1, b2, c2)   # Determinante des Systems in y,z

        # Fall 1:
        # D_xy != 0 → Das 2×2-System in x und y ist eindeutig lösbar
        if D_xy != 0:
            # Führendes Gleichungssystem in x,y – z wird Parameter t
            steps += "Wir wählen z als Parameter: z = t und lösen das 2x2-System in x und y.\n"

            # Für t = 0 erhalten wir den Stützpunkt:
            # (x0, y0, z0)
            x0 = det2(d1, b1, d2, b2) / D_xy
            y0 = det2(a1, d1, a2, d2) / D_xy
            z0 = 0.0

            # Für t != 0 berechnen wir den Richtungsvektor (vx, vy, vz)
            vx = -det2(c1, b1, c2, b2) / D_xy
            vy = -det2(a1, c1, a2, c2) / D_xy
            vz = 1.0  # z = t

        # Fall 2:
        # D_xz != 0 → y = t ist sinnvoll
        elif D_xz != 0:
            steps += "Wir wählen y als Parameter: y = t und lösen das 2x2-System in x und z.\n"

            x0 = det2(d1, c1, d2, c2) / D_xz
            y0 = 0.0
            z0 = det2(a1, d1, a2, d2) / D_xz

            vx = -det2(b1, c1, b2, c2) / D_xz
            vy = 1.0  # y = t
            vz = -det2(a1, b1, a2, b2) / D_xz

        # Fall 3:
        # D_yz != 0 → x = t ist sinnvoll
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

            result = "WARNUNG: Alle 2x2-Minoren sind 0, obwohl zwei unabhängige Zeilen erwartet wurden.\n"
            
            return result, steps if vis_calc else "" # Rechenschritte nur zurückgeben, falls vis_calc == True


        # Parametergleichung der Schnittgeraden
        equation = f"g(t) = ({x0:g}, {y0:g}, {z0:g}) + t · ({vx:g}, {vy:g}, {vz:g})"

        result= f"Schnittgerade (Parametergleichung):\n    {equation}\n"

    return result, steps if vis_calc else "" # Rechenschritte nur zurückgeben, falls vis_calc == True



def output_result(result, calc_steps):
    if calc_steps != "":
        print(calc_steps)

    print(result)

    
def save_output_in_file(result):
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