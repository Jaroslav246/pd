import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect('Celjojumi.db')
cursor = conn.cursor()

def pievienot_marsruti():
    def saglabat_marsruti():
        id_marsruti = id_marsruta_entry.get()
        valsts = valsts_entry.get()
        cena = cena_entry.get()
        dienu_skaits = dienu_skaits_entry.get()

        if valsts and cena and dienu_skaits:
            cursor.execute(
                "INSERT INTO Marsruti (id_marsruti, valsts, cena, dienu_skaits) VALUES (?, ?, ?, ?)",
                (id_marsruti, valsts, cena, dienu_skaits)
            )
            conn.commit()
            messagebox.showinfo("Veiksmīgi", "Marsruts pievienots!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus korekti!")

    logs = tk.Toplevel()
    logs.title("Pievienot marsruti")
    logs.geometry("300x300")

    tk.Label(logs, text="id_marsruta:").pack()
    id_marsruta_entry = tk.Entry(logs)
    id_marsruta_entry.pack()

    tk.Label(logs, text="valsts:").pack()
    valsts_entry = tk.Entry(logs)
    valsts_entry.pack()

    tk.Label(logs, text="cena:").pack()
    cena_entry = tk.Entry(logs)
    cena_entry.pack()

    tk.Label(logs, text="dienu_skaits:").pack()
    dienu_skaits_entry = tk.Entry(logs)
    dienu_skaits_entry.pack()


    saglabat_btn = tk.Button(logs, text="Saglabāt", command=saglabat_marsruti)
    saglabat_btn.pack(pady=10)


def meklēt_marsruti():
    def atrast_marsruti():
        vards = vards_entry.get()
        if vards:
            cursor.execute("SELECT * FROM Marsruti WHERE vards LIKE ?", (f"%{vards}%",))
            rezultati = cursor.fetchall()
            if rezultati:
                rezultati_str = ""
                for r in rezultati:
                    rezultati_str += f"{r[0]}: {r[1]} {r[2]}, {r[3]}\n"
            else:
                messagebox.showinfo("Rezultāti", "Netika atrasts neviens marsruts.")
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet marsruti!")

    logs = tk.Toplevel()
    logs.title("Meklēt marsruti")
    logs.geometry("300x200")

    tk.Label(logs, text="Marsruts:").pack()
    vards_entry = tk.Entry(logs)
    vards_entry.pack()

    meklēt_btn = tk.Button(logs, text="Meklēt marsrutu", command=atrast_marsruti)
    meklēt_btn.pack(pady=10)


def dzēst_marsruti():
    def dzēst_marsruti_no_db():
        id_marsruti = id_marsruta_entry.get()
        if id_marsruti.isdigit():
            cursor.execute("DELETE FROM Marsruts WHERE id_klienta = ?", (id_marsruti,))
            conn.commit()
            messagebox.showinfo("Veiksmīgi", f"Marsruts ar ID {id_marsruti} tika izdzēsts!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet derīgu Marsruta ID!")

    logs = tk.Toplevel()
    logs.title("Dzēst marsrut")
    logs.geometry("300x150")

    tk.Label(logs, text="Marsruta ID:").pack()
    id_marsruta_entry = tk.Entry(logs)
    id_marsruta_entry.pack()

    dzēst_btn = tk.Button(logs, text="Dzēst", command=dzēst_marsruti_no_db)
    dzēst_btn.pack(pady=10)


def marsruti_logs():
    marsruti_logs = tk.Toplevel()
    marsruti_logs.title("Marsrutu pārvaldība")
    marsruti_logs.geometry("300x250")

    pievienot_btn = tk.Button(marsruti_logs, text="Pievienot marsruti", command=pievienot_marsruti, width=25, height=2, bg="lightblue")
    pievienot_btn.pack(pady=10)

    meklēt_btn = tk.Button(marsruti_logs, text="Meklēt marsrutu", command=meklēt_marsruti, width=25, height=2, bg="lightgreen")
    meklēt_btn.pack(pady=10)

    dzēst_btn = tk.Button(marsruti_logs, text="Dzēst marsruti", command=dzēst_marsruti, width=25, height=2, bg="lightyellow")
    dzēst_btn.pack(pady=10)

    iziet_btn = tk.Button(marsruti_logs, text="Iziet marsruti", command=marsruti_logs.destroy, width=25, height=2, bg="red", fg="white")
    iziet_btn.pack(pady=10)

def izveidot_galveno_logu():
    def klienta_poga():
        #klienta_logs()
        messagebox.showinfo("Klienta", "Atvērta klienti pārvaldība.")
    def marsruti_poga():
        marsruti_logs()
        messagebox.showinfo("Marsruti", "Atvērta marsruti pārvaldība.")

    def celjojumi_poga():
        #celjojumu_logs()
        messagebox.showinfo("Celjojumi", "Atvērta celjojumi pārvaldība.")

    logs = tk.Tk()
    logs.title("Celojumi")
    logs.geometry("300x200")

    treneri_btn = tk.Button(logs, text="Klienti", command=marsruti_poga, width=20, height=2, bg="lightblue")
    treneri_btn.pack(pady=10)

    treneri_btn = tk.Button(logs, text="Marsruti", command=marsruti_poga, width=20, height=2, bg="lightgreen")
    treneri_btn.pack(pady=10)

    apmeklejumi_btn = tk.Button(logs, text="Celjojumi", command=celjojumi_poga, width=20, height=2, bg="lightyellow")
    apmeklejumi_btn.pack(pady=10)

    logs.mainloop()


if __name__ == "__main__":
    izveidot_galveno_logu()