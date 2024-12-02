import PySimpleGUI as sg

class Gui():
   def __init__(self):
    layout = [  [sg.Text('Ievadiet nopirkto produktu')], 
                [sg.Text('Kategorija', size=(15, 1)), sg.InputText(key='T-KATEG-',focus=True)],
                [sg.Text('Nosaukums ', size=(15, 1)), sg.InputText(key='T-NOSAUK-')],
                [sg.Text('Tehniskais raksturojums ', size=(20, 1)), sg.InputText(key='T-RAKSTUR-')],
                [sg.Text('Nomas cena dienā ', size=(20, 1)), sg.InputText(key='T-Cena-')], 
                [sg.Button('Ievadīt'), sg.Button('Atcelt')] ]   
def logu_veido(self):
    window = sg.Window('Datora komponentes', self.layout) 
    return (window)
