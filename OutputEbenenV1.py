# result = (int(Index 0,1,2), str(Gleichung), str(Rechenschritte), bool(Filespeichern))

NAME_OUTPUT_FILE = "output.txt"

def output(ind, equation, calc_steps, file_save):
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
            with open(NAME_OUTPUT_FILE, "w") as output:
                output.write("Die Schnittmenge der beiden Ebenen lautet:" + equation)
        except:
            print(f"Fehler: {NAME_OUTPUT_FILE} nicht gefunden.")