import csv

save_calculation_steps = None
answer_yes = ["y", "yes", "ye", "yeah", "ja", "j"]
answer_no = ["n", "no", "nope", "nein", "never"]
index_unallowed = []

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
    {list_ebene[0]} x1 {list_ebene[1]} x2 {list_ebene[2]} x3 - {list_ebene[3]} = 0""" )
        if frage_nach_ebene[0].lower() == "j":
            return ({"x": list_ebene[0],"y": list_ebene[1],"z": list_ebene[2],"d": list_ebene[3]})
            break
                
        else:
            print("Versuche erneut")
def main():
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
            print("""
    Bitte erneut versuchen!
    Dies ist nicht Gültig bitte versuche es mit Ja oder mit Nein
            """)
        while True:
            file_or_terminal = input("Bevor wir beginnen, willst du deine ebenen im Terminal eingeben oder aus einer CSV Datei auslesen? (T/CSV) ")
            if file_or_terminal.upper() == "T":
                print("Beginnen wir mit der ersten Ebene:")
                e1 = eingabe_ebene()
                print("Jetzt die zweite Ebene:")
                e2 = eingabe_ebene()
                print(e1,e2)
                
                break
            elif file_or_terminal.upper() == "CSV":
                while True:
                    with open("ebenen.csv", mode="r", encoding="utf-8") as csvfile:
                        reader = csv.reader(csvfile)
                        for index, row in enumerate(reader):
                            if len(row) == 4:
                                print(index+1,row)
                            else:
                                print(index, f"Zeile {index + 1} in der CSV-Datei ist ungültig und wird übersprungen.")
                                index_unallowed.append(index + 1)

                        while True:
                            eingabe_ebenen =  input("Bitte wähle zwei Ebenen durch ihre Nummern aus, getrennt durch ein Komma: ").split(",")
                            if len(eingabe_ebenen) != 2:
                                print("Bitte genau zwei Ebenennummern angeben.")
                                continue
                            
                            try:
                                eingabe_ebene1 = int(eingabe_ebenen[0].strip())
                                eingabe_ebene2 = int(eingabe_ebenen[1].strip())
                                if 1 <= eingabe_ebene1 <= index + 1 and 1 <= eingabe_ebene2 <= index + 1 and eingabe_ebene1 not in index_unallowed and eingabe_ebene2 not in index_unallowed:
                                    break
                                else:
                                    print("Ungültige Ebenennummern. Bitte erneut versuchen.")
                            except ValueError:
                                print("Ungültige Eingabe. Bitte gib zwei Zahlen ein, getrennt durch ein Komma.")    
                        ebenenueberpruefung = input(f"Du hast Ebene {eingabe_ebene1} und Ebene {eingabe_ebene2} ausgewählt. Passt das? (j/n) ")
                        if ebenenueberpruefung in answer_yes:
                            break

                break

main()