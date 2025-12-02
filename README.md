# Molecular Mass Calculator

**A Chemistry + Python Mini Project**

The Molecular Mass Calculator is a Python-based graphical application built using Tkinter.
It allows users to enter the chemical formula of any compound (e.g., H₂O, CO₂, C₆H₁₂O₆, NaCl) and instantly calculates the molecular mass using a built-in atomic mass table of elements from Hydrogen (H) to Oganesson (Og).

The GUI is designed in a colorful, modern theme featuring a dark blue background, large fonts, and bright buttons for a smooth user experience.

## 🎓 Developed By:

Group 15 - 

  1. Geet Tiwari (25BAI10389)

  2. Khushi Parashar (25BAI10363)
           
  3. Adhishri Tiwari (25BAI10242)
           
  4. Sumedha Bakshi (25BAI10037)
           
  5. Tarushi Taanvi (25BAI10343)

## 🎯 Features
✅ Colorful & Modern GUI

- Dark mode styling

- Large, clear fonts

- Bright green "Calculate" and red "Clear" buttons

- Clean and easy-to-use layout

✅ Accurate Molecular Mass Calculation

- Uses an extensive dictionary of atomic masses (H → Og)

- Supports multi-element formulas like:

- H2O

- C6H12O6

- NaCl

- Fe2O3

- Supports uppercase + lowercase element symbols (e.g., Na, Cl, Mg, Fe)

✅ Error Handling

- Invalid formulas detected

- Missing elements flagged clearly

- User warnings for empty input

## 🧮 How It Works

The program follows these steps:

- Input Parsing

- Reads each character of the formula

- Identifies element symbols (e.g., H, Na, Cl)

- Detects counts (e.g., the “2” in H₂O)

- Defaults count to 1 when no number is provided

- Mass Calculation

- Looks up each element in the atomic mass dictionary

- Multiplies atomic mass × count

- Adds to total molecular mass

- Output Display

- Shows the final molecular mass on the GUI screen

## 📸 GUI Preview

The interface includes:

- Title: “Molecular Mass Calculator” (gold text)

- Subtitle: shows example formulas

- Input Field: dark textbox for entering formulas

- Buttons:

      🟩 Calculate

      🟥 Clear

- Output Section: displays the result

- Footer: group name

## ⚠️ Limitations

- Does not support parentheses yet (e.g., Ca(OH)2)

- Whitespace inside formulas is not allowed

- The atomic mass table, while large, contains approximate masses
