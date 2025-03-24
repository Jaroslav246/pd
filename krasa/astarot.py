import tkinter as tk
from tkinter import messagebox
import re

def paarbaude_vaardu():
    vaards = vaards_entry.get()
    pattern= r'^[A-Z]{1}[a-z]{1,}'

    if re.match(pattern, vaards):
        messagebox.showinfo("Rezultāts", "Vards ir derīgs!")
    else:
        messagebox.showerror("Rezultāts", "Vārds nav derīgs!")
        
def paarbaude_diena():
    diena = diena_entry.get()
    pattern=r'^\d{2}{.}+\d{2}{.}+\d{4}+0\d{2}/\d{2}/\d{4}'

    if re.match(pattern, diena):
        messagebox.showinfo("Rezultāts", "Suņu dzimšanas diena ir derīgs!")
    else:
        messagebox.showerror("Rezultāts", "Suņu dzimšanas diena nav derīgs!")

root = tk.Tk()
root.title("Personas koda pārbaude")
    
tk.Label(root, text="Ievadiet vārdu:").pack(pady=5)
vaards_entry = tk.Entry(root, width=30)
vaards_entry.pack(pady=5)
tk.Button(root, text="Pārbaudīt", command=paarbaude_vaardu).pack(pady=5)


tk.Label(root, text="Ievadiet diena:").pack(pady=5)
diena_entry = tk.Entry(root, width=30)
diena_entry.pack(pady=5)
tk.Button(root, text="Pārbaudīt", command=paarbaude_diena).pack(pady=5)
root.mainloop()

