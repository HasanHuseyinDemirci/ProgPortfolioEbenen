import csv

save_calculation_steps = None
answer_yes = ["y", "yes", "ye", "yeah", "ja", "j"]
answer_no = ["n", "no", "nope", "nein", "never"]


def eingabe_ebene():
    while True:
        list_ebene = [0, 0, 0, 0]
        list_ebene_index = ["x", "y", "z", "d"]
        for i in range(len(list_ebene)):
            while True:
                list_ebene[i] = input(f"Bitte gib einen gültigen Wert für {list_ebene_index[i]} an ")
                try:
                    list_ebene[i] = float(list_ebene[i])
                    break
                except ValueError:
                    print("Bitte erneut versuchen!")
                    list_ebene[i] = list_ebene_index[i]

        frage_nach_ebene = input(f"""
    ist dies Ebene? (j/n) 
    {list_ebene[0]} x1 {list_ebene[1]} x2 {list_ebene[2]} x3 - {list_ebene[3]} = 0""")
        if frage_nach_ebene[0].lower() == "j":
            return ({"x": list_ebene[0],"y": list_ebene[1],"z": list_ebene[2],"d": list_ebene[3]})
            break
                
        else:
            print("Versuche erneut")

while True:
    print(
        """
Willkommen beim Ebenenrechner!
    
Dieses Programm ermöglicht es, die Schnittmenge mehrerer Ebenen zu berechnen.  
Du kannst die Ebenenkoeffizienten entweder über eine CSV-Datei einlesen oder direkt in der Kommandozeile eingeben.  
Anschließend wird die Schnittmenge berechnet, und du kannst wählen, ob das Ergebnis als CSV-Datei exportiert werden soll oder direkt in der Kommandozeile ausgegeben wird.
        """)
    

    while True:
        answer = input("Willst du die Rechenschritte Speichern? (j/n) ")
        if answer.lower() in answer_yes:
            save_calculation_steps = True
            break
        elif answer.lower() in answer_no:
            save_calculation_steps = False
            break
        print(save_calculation_steps)
        print("""
Bitte erneut versuchen!
Dies ist nicht Gültig bitte versuche es mit Ja oder mit Nein
        """)
    while True:
        file_or_terminal = input("Bevor wir beginnen, willst du deine ebenen im Terminal eingeben oder aus einer CSV Datei auslesen? (T/CSV)")
        if file_or_terminal.upper() == "T":
            e1 = eingabe_ebene()
            e2 = eingabe_ebene()
            print(e1,e2)
            break
        elif file_or_terminal.upper() == "CSV":
            while True:
                with open("ebenen.csv", mode="r", encoding="utf-8") as csvfile:
                    reader = csv.reader(csvfile)
                    for index, row in enumerate(reader):
                        print(index+1, row)
                    while True:
                        eingabe_ebene1, eingabe_ebene2 = input("Bitte wähle zwei Ebenen durch ihre Nummern aus, getrennt durch ein Komma: ").split(",")
                        try:
                            eingabe_ebene1 = int(eingabe_ebene1.strip())
                            eingabe_ebene2 = int(eingabe_ebene2.strip())
                            if 1 <= eingabe_ebene1 <= index + 1 and 1 <= eingabe_ebene2 <= index + 1:
                                break
                            else:
                                print("Ungültige Ebenennummern. Bitte erneut versuchen.")
                        except ValueError:
                            print("Ungültige Eingabe. Bitte gib zwei Zahlen ein, getrennt durch ein Komma.")    
                    print(f"Du hast Ebene {eingabe_ebene1} und Ebene {eingabe_ebene2} ausgewählt.")

            break

