from tkinter import *

root=Tk()
root.title('Attēla pārvietošana')
root.geometry('400x400')
root.resizable(width=False, height=False)

img_x, img_y = 50, 50

btn = Button(root, text="Pārvietot attēlu")
btn.pack(pady=20)

root.mainloop()