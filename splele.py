from tkinter import *
from random import *

root=Tk()
root.title('Spēle')
root.geometry('600x600')
root.resizable(width=False, height=False)
root['bg']='orange'

def Whyknb():
    knb=['Akmens', 'Šķēres', 'Papīrs']
    value=choice(knb)
    labelText.configure(text=value)
labelText=Label(root, 
           text='', 
           font=('Comic Sans Ms', 20, 'bold'),
           bg='green',
           fg='blue'
           )
labelText.place(y=200, x=200)

stone=Button(root, 
           text='Akmens', 
           font=('Comic Sans Ms', 20, 'bold'),
           bg='white',
           command=Whyknb
           )
stone.place(x=20, y=300)

scissors=Button(root, 
           text='Šķēres', 
           font=('Comic Sans Ms', 20, 'bold'),
           bg='white',
           command=Whyknb
           )
scissors.place(x=220, y=300)

paper=Button(root, 
           text='Papīrs', 
           font=('Comic Sans Ms', 20, 'bold'),
           bg='white',
           command=Whyknb
           )
paper.place(x=420, y=300)
root.mainloop()