import csv

save_calculation_steps = None


def eingabe_ebene(number):
    while True:
        while True:
            x = input("Bitte gib einen gültigen Wert für x an ")
            try:
                x = float(x)
                break
            except ValueError:
                print("Bitte erneut versuchen!")
        while True:
            y = input("Bitte gib einen gültigen Wert für y an ")
            try:
                y = float(y)
                break
            except ValueError:
                print("Bitte erneut versuchen!")
        while True:
            z = input("Bitte gib einen gültigen Wert für z an ")
            try:
                z = float(z)
                break
            except ValueError:
                print("Bitte erneut versuchen!")
        while True:
            d = input("Bitte gib einen gültigen Wert für d an ")
            try:
                d = float(d)
                break
            except ValueError:
                print("Bitte erneut versuchen!")

        frage_nach_ebene = input(f"""
ist dies Ebene? (j/n) 
{x} x1 {y} x2 {z} x3 - {d} = 0""")
        if frage_nach_ebene[0].lower() == "j":
            return ({"x": x,"y": y,"z": z,"d": d})
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
        if answer.lower() == "y" or answer.lower() == "yes" or answer.lower() == "ye" or answer.lower() == "yeah" or answer.lower() == "ja" or answer.lower() == "j":
            save_calculation_steps = True
            break
        elif answer.lower() == "n" or answer.lower() == "no"or answer.lower() == "nope" or answer.lower() == "nein" or answer.lower() == "never":
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
            e1 = eingabe_ebene(1)
            e2 = eingabe_ebene(2)
            print(e1,e2)
            break
        elif file_or_terminal.upper() == "CSV":
            with open("ebenen.csv", mode ="w") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    print(row)

            break

    break