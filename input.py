import csv

save_calculation_steps = None



while True:
    print(
        """
Willkommen beim Ebenenrechner!
    
Dieses Programm ermöglicht es, die Schnittmenge mehrerer Ebenen zu berechnen.  
Du kannst die Ebenenkoeffizienten entweder über eine CSV-Datei einlesen oder direkt in der Kommandozeile eingeben.  
Anschließend wird die Schnittmenge berechnet, und du kannst wählen, ob das Ergebnis als CSV-Datei exportiert werden soll oder direkt in der Kommandozeile ausgegeben wird.
        """)
    while True:
        answer = input("Willst du die Rechenschritte Speichern?")
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
        if file_or_terminal.lower() == "T":
            while True:
                x1 = input("Bitte gib einen gültigen Wert für x an ")
                try:
                    x1 = float(x1)
                    break
                except ValueError:
                    print("Bitte erneut versuchen!")
            while True:
                y1 = input("Bitte gib einen gültigen Wert für y an ")
                try:
                    y1 = float(y1)
                    break
                except ValueError:
                    print("Bitte erneut versuchen!")
            while True:
                z1 = input("Bitte gib einen gültigen Wert für z an ")
                try:
                    z1 = float(z1)
                    break
                except ValueError:
                    print("Bitte erneut versuchen!")
            while True:
                d1 = input("Bitte gib einen gültigen Wert für d an ")
                try:
                    d1 = float(d1)
                    break
                except ValueError:
                    print("Bitte erneut versuchen!")
            while True:
                frage_nach_ebene = input(f"""
ist dies Ebene? (j/n) 
{x1} x1 {y1} x2 {z1} x3 - {d1} = 0""")
                if frage_nach_ebene[0].lower() == "j":
                    break

                elif frage_nach_ebene[0].lower() == "n":
                    break


        elif file_or_terminal.lower() == "CSV":
            with open("ebenen.csv") as csvfile:
                reader = csv.reader(csvfile)
                print(reader)

    break