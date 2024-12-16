from tkinter import *

def move_image():
    global img_x, img_y
    img_x += 10
    img_y += 10
    l_logo.place(img_x, img_y)

root=Tk()
root.title('Vienkārša Tkinder programma')
root.geometry('400x400')
root.resizable(width=False, height=False)

img_x, img_y = 50, 50

img = PhotoImage(file='image copy.png')
l_logo = Label(root, image=img)
l_logo.place(x=img_x, y=img_y)

btn = Button(root, text="Pārvietot attēlu", command=move_image)
btn.pack(pady=20)

root.mainloop()