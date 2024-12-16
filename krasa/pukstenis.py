from tkinter import *
from datetime import datetime

def update_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)

root = Tk()
root.title("Laiks un Datums")
root.geometry("300x150")

label = Label(root, text="", font=("Arial", 16), bg="lightgray", fg="black")
label.pack(expand=True, fill=BOTH)

update_time()

root.mainloop()