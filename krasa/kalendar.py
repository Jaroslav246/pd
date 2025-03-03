import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import sqlite3
from tkinter import messagebox
conn = sqlite3.connect('datumi.db')
cursor = conn.cursor()
def calendar_view():
    def print_sel():
        print(cal.selection_get())
        if cal.selection_get():
            cursor.execute("INSERT INTO datumi (datums) VALUES (?)", (f"{cal.selection_get()}",))
            conn.commit()
            messagebox.showinfo("Veiksmīgi", "Datums pievienots!")

    top = tk.Toplevel(root)
    cal = Calendar(top,
    font="Arial 14", selectmode='day')
    cursor="hand1", year=2025, month=2, day=5
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()
root = tk.Tk()
s = ttk.Style(root)
root.geometry('160x160+500+300')
s.theme_use('clam')
ttk.Button(root, text='Kalendars', command=calendar_view).pack(padx=10, pady=10)
root.mainloop()