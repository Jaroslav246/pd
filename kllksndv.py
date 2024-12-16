from tkinter import *

def in_count():
    global count
    count += 1
    label.config(text=f"Klikšķi: {count}")

root = Tk()
root.title("Klikšķu skaitītājs")
root.geometry("300x200")

count = 0 

label = Label(root, text=f"Klikšķi: {count}", font=("Arial", 16))
label.pack(pady=20)

btn = Button(root, text="Klikšķi mani!", font=("Arial", 14), command=in_count)
btn.pack()

root.mainloop()
