import Plane


NAME_INPUT_FILE = ""
NAME_OUTPUT_FILE = "output.txt"
DECIMAL_PLACCES = 3

def input():
    pass
# return Ebene: e1, Ebene: e2, bool: vis_calc, bool: file_save

def calc_gauss(e1, e2, vis_calc, file_save):
    pass
#return int: ind, str: equation, str: calc_steps, boll: file_save

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

