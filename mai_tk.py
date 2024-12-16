from tkinter import *
root=Tk()
root.title('Pirmā proga')
root.geometry('600x600')
root.resizable(width=False, height=False)
'''root.iconbitmap('icon.ico')'''

#background
root.config(bg='yellow')
root['bg']='lime'
def click():
    print('Sveiciens!')


'''label=Label(root, 
           text='Poga', 
           command=click,
           font='Comic Sans Ms', 20, 'bold'),
           bg='green',
           activebackground='orange',
           activebackground='white',
           fg='blue'
           )

label.pack()'''
label.place(x=100, y=50)

img=PhotoImage(file='logo2.png')
l_logo=Label(root,image=img)
l_logo.place(x=100, y=250)
root.mainloop()
