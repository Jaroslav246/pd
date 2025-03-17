import tkinter as tk
from tkinter import messagebox
import re

def paarbaude_diena():
    diena = diena_entry.get()
    pattern=r'^\d{2}{.}+\d{2}{.}+\d{4}+0\d{2}/\d{2}/\d{4}'

    if re.match(pattern, diena):
        messagebox.showinfo("Rezultāts", "Suņa dzimšanas diena ir derīgs!")
    else:
        messagebox.showerror("Rezultāts", "Suņa dzimšanas diena nav derīgs!")

root = tk.Tk()
root.title("Personas koda pārbaude")

tk.Label(root, text="Ievadiet diena:").pack(pady=5)
diena_entry = tk.Entry(root, width=30)
diena_entry.pack(pady=5)
tk.Button(root, text="Pārbaudīt", command=paarbaude_diena).pack(pady=5)
root.mainloop()

