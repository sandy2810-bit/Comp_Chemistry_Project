import tkinter as tk
from tkinter import messagebox

atm_masses = {
    "H": 1.0, "He": 4.0, "Li": 4.0, "Be": 8.0, "B": 10.0, "F": 19.0, "Ne": 20.0, "Mg": 24.0, "Si": 28.0, "S": 32.0, "Cl": 35.5, "Ar": 40.0, "Sc": 45.0, "Ti": 48.0, "V": 50.0, "Cr": 52.0,"Mn": 55.0, "Co": 59.0, "Ni": 58.0, "Ga": 70.0, "Ge": 73.0, "As": 75.0, "C": 12.0, "Se": 79.0, "N": 14.0,"O": 16.0,"Na": 23.0,"Mg": 24.0,"Al": 27.0, "Si": 28.0,"P": 31.0,"S": 32.0,"Cl": 35.5, "K": 39.0, "Ca": 40.0, "Fe": 56.0, "Cu": 63.5, "Zn": 65.0, "Br": 80.0, "Kr": 84.0, "Rb":85, "Sr":88, "Y":89, "Zr":91, "Nb":93, "Mo":96, "Tc":98, "Ru":101, "Rh":103, "Pd":106, "Ag":108, "Cd":112, "In":115, "Sn":119, "Sb":122, "Te":128, "I":127, "Xe":131, "Cs":133, "Ba":137, "La":139, "Ce":140, "Pr":141, "Nd":144, "Pm":145, "Sm":150, "Eu":152, "Gd":157, "Tb":159, "Dy":163, "Ho":165, "Er":167, "Tm":169, "Yb":173, "Lu":175, "Hf":178, "Ta":181, "W":184, "Re":186, "Os":190, "Ir":192, "Pt":195, "Au":197, "Hg":201, "Tl":204, "Pb":207, "Bi":209, "Po":209, "At":210, "Rn":222, "Fr":223, "Ra":226, "Ac":227, "Th":232, "Pa":231, "U":238, "Np":237, "Pu":244, "Am":243, "Cm":247, "Bk":247, "Cf":251, "Es":252, "Fm":257, "Md":258, "No":259, "Lr":262, "Rf":261, "Db":262, "Sg":266, "Bh":264, "Hs":269, "Mt":278, "Ds":281, "Rg":281, "Cn":285, "Nh":286, "Fl":289, "Mc":289, "Lv":293, "Ts":294, "Og":294,
}

def parse_formula(formula):
    i = 0
    length = len(formula)
    elements = []

    while i < length:

        if not formula[i].isalpha() or not formula[i].isupper():
            return None

        symbol = formula[i]
        i += 1


        if i < length and formula[i].isalpha() and formula[i].islower():
            symbol += formula[i]
            i += 1


        count_str = ""
        while i < length and formula[i].isdigit():
            count_str += formula[i]
            i += 1

        if count_str == "":
            count = 1
        else:
            count = int(count_str)

        elements.append((symbol, count))

    return elements


def calculate_molecular_mass(formula):
    parts = parse_formula(formula)
    if parts is None:
        return None, "Invalid formula format. Use like H2O, CO2, C6H12O6."

    total_mass = 0.0

    for symbol, count in parts:
        if symbol not in atm_masses:
            return None, f"Element {symbol} not found in database."
        total_mass += atm_masses[symbol] * count

    return total_mass, ""


def on_calculate():
    formula = entry_formula.get().strip()

    if formula == "":
        messagebox.showwarning("Input Error", "Please enter a chemical formula.")
        return

    mass, error = calculate_molecular_mass(formula)

    if mass is None:
        messagebox.showerror("Error", error)
        label_result.config(text="Result: -", fg="red")
    else:
        label_result.config(
            text=f"Result: Molecular mass of {formula} = {mass} u",
            fg="white"
        )


root = tk.Tk()
root.title("Molecular Mass Calculator")


root.geometry("1000x600")
root.configure(bg="#1b1f3b")  


label_title = tk.Label(
    root,
    text="Molecular Mass Calculator",
    font=("Arial", 44, "bold"),
    bg="#1b1f3b",
    fg="#ffcc00"  
)
label_title.pack(pady=10)


label_sub = tk.Label(
    root,
    text="Enter a formula like H2O, CO2, C6H12O6, NaCl",
    font=("Arial", 14),
    bg="#1b1f3b",
    fg="#e0e0e0"
)
label_sub.pack(pady=2)


frame_input = tk.Frame(root, bg="#1b1f3b")
frame_input.pack(pady=15)

label_formula = tk.Label(
    frame_input,
    text="Chemical Formula:",
    font=("Arial", 32),
    bg="#1b1f3b",
    fg="#9be7ff"  
)
label_formula.pack(side=tk.LEFT, padx=5)

entry_formula = tk.Entry(
    frame_input,
    width=22,
    font=("Arial", 28),
    bg="#263238",   
    fg="#ffffff",
    insertbackground="white",  #cursor
    relief=tk.FLAT
)
entry_formula.pack(side=tk.LEFT, padx=5)


frame_buttons = tk.Frame(root, bg="#1b1f3b")
frame_buttons.pack(pady=5)

btn_calc = tk.Button(
    frame_buttons,
    text="Calculate",
    font=("Arial", 28, "bold"),
    bg="#00c853",   
    fg="white",
    activebackground="#00e676",
    activeforeground="black",
    relief=tk.FLAT,
    padx=10,
    pady=5,
    command=on_calculate
)
btn_calc.pack(side=tk.LEFT, padx=10)

def on_clear():
    entry_formula.delete(0, tk.END)
    label_result.config(text="Result: -", fg="white")

btn_clear = tk.Button(
    frame_buttons,
    text="Clear",
    font=("Arial", 28, "bold"),
    bg="#d50000",  
    fg="white",
    activebackground="#ff1744",
    activeforeground="black",
    relief=tk.FLAT,
    padx=10,
    pady=5,
    command=on_clear
)
btn_clear.pack(side=tk.LEFT, padx=10)


label_result = tk.Label(
    root,
    text="Result: -",
    font=("Arial", 26, "bold"),
    bg="#1b1f3b",
    fg="white"
)
label_result.pack(pady=20)


label_footer = tk.Label(
    root,
    text="Note: Made by group no 15!",
    font=("Arial", 8),
    bg="#1b1f3b",
    fg="#b0bec5"
)
label_footer.pack(side=tk.BOTTOM, pady=5)

root.mainloop()
