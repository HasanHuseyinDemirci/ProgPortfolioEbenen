import csv

save_calculation_steps = None
ANSWER_YES = {"y", "yes","ja","j"}
ANSWER_NO = {"n", "no", "nein"}
ANSWER_TERMINAL = {"t", "terminal"}
ANSWER_CSV = {"csv", "c"}

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
    global save_calculation_steps
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

def main_input():
    global save_calculation_steps
    start_plane_calculator()
    ask_user_calculation_steps_preferences()

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
    return e1, e2

print(main_input())