import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect('Celjojumi.db')
cursor = conn.cursor()

def pievienot_klients():
    def saglabat_klients():
        vards = vards_entry.get()
        uzvards = uzvards_entry.get()
        pilseta = pilseta_entry.get()

        if vards and uzvards and pilseta:
            cursor.execute(
                "INSERT INTO Klienti (vards, uzvards, pilseta) VALUES (?, ?, ?)",
                (vards, uzvards, pilseta)
            )
            conn.commit()
            messagebox.showinfo("Veiksmīgi", "Klients pievienots!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus korekti!")

    logs = tk.Toplevel()
    logs.title("Pievienot klientu")
    logs.geometry("300x300")

    tk.Label(logs, text="Vārds:").pack()
    vards_entry = tk.Entry(logs)
    vards_entry.pack()

    tk.Label(logs, text="Uzvārds:").pack()
    uzvards_entry = tk.Entry(logs)
    uzvards_entry.pack()

    tk.Label(logs, text="Pilseta:").pack()
    pilseta_entry = tk.Entry(logs)
    pilseta_entry.pack()


    saglabat_btn = tk.Button(logs, text="Saglabāt", command=saglabat_klients)
    saglabat_btn.pack(pady=10)


def meklēt_klienti():
    def atrast_klientu():
        vards = vards_entry.get()
        if vards:
            cursor.execute("SELECT * FROM Klienti WHERE vards LIKE ?", (f"%{vards}%",))
            rezultati = cursor.fetchall()
            if rezultati:
                rezultati_str = ""
                for r in rezultati:
                    rezultati_str += f"{r[0]}: {r[1]} {r[2]}, {r[3]}, {r[4]}, {r[5]}\n"
            else:
                messagebox.showinfo("Rezultāti", "Netika atrasts neviens klients.")
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet klienti!")

    logs = tk.Toplevel()
    logs.title("Meklēt klientu")
    logs.geometry("300x200")

    tk.Label(logs, text="Klienta vārds:").pack()
    vards_entry = tk.Entry(logs)
    vards_entry.pack()

    meklēt_btn = tk.Button(logs, text="Meklēt", command=atrast_klientu)
    meklēt_btn.pack(pady=10)


def dzēst_klientu():
    def dzēst_klientu_no_db():
        id_klienti = id_klienta_entry.get()
        if id_klienti.isdigit():
            cursor.execute("DELETE FROM Klienti WHERE id_klienta = ?", (id_klienti,))
            conn.commit()
            messagebox.showinfo("Veiksmīgi", f"Klients ar ID {id_klienti} tika izdzēsts!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet derīgu ID!")

    logs = tk.Toplevel()
    logs.title("Dzēst klientu")
    logs.geometry("300x150")

    tk.Label(logs, text="Klienta ID:").pack()
    id_klienta_entry = tk.Entry(logs)
    id_klienta_entry.pack()

    dzēst_btn = tk.Button(logs, text="Dzēst", command=dzēst_klientu_no_db)
    dzēst_btn.pack(pady=10)


def klienti_logs():
    klienti_logs = tk.Toplevel()
    klienti_logs.title("Klientu pārvaldība")
    klienti_logs.geometry("300x250")

    pievienot_btn = tk.Button(klienti_logs, text="Pievienot klienti", command=pievienot_klients, width=25, height=2, bg="lightblue")
    pievienot_btn.pack(pady=10)

    meklēt_btn = tk.Button(klienti_logs, text="Meklēt klienti", command=meklēt_klienti, width=25, height=2, bg="lightgreen")
    meklēt_btn.pack(pady=10)

    dzēst_btn = tk.Button(klienti_logs, text="Dzēst klienti", command=dzēst_klientu, width=25, height=2, bg="lightyellow")
    dzēst_btn.pack(pady=10)

    iziet_btn = tk.Button(klienti_logs, text="Iziet", command=klienti_logs.destroy, width=25, height=2, bg="red", fg="white")
    iziet_btn.pack(pady=10)

def izveidot_galveno_logu():
    def klienti_poga():
        klienti_logs()
        messagebox.showinfo("Klienti", "Atvērta klienti pārvaldība.")
    def marsruti_poga():
        #marsrutu_logs()
        messagebox.showinfo("Marsruti", "Atvērta marsruti pārvaldība.")

    def celjojumi_poga():
        #celjojumu_logs()
        messagebox.showinfo("Celjojumi", "Atvērta celjojumi pārvaldība.")

    logs = tk.Tk()
    logs.title("Trenažieru zāles pārvaldība")
    logs.geometry("300x200")

    treneri_btn = tk.Button(logs, text="Klienti", command=klienti_poga, width=20, height=2, bg="lightblue")
    treneri_btn.pack(pady=10)

    treneri_btn = tk.Button(logs, text="Marsruti", command=marsruti_poga, width=20, height=2, bg="lightgreen")
    treneri_btn.pack(pady=10)

    apmeklejumi_btn = tk.Button(logs, text="Celjojumi", command=celjojumi_poga, width=20, height=2, bg="lightyellow")
    apmeklejumi_btn.pack(pady=10)

    logs.mainloop()


if __name__ == "__main__":
    izveidot_galveno_logu()