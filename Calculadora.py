import PySimpleGUI as sg

class Calculadora:
    sg.theme('LightGreen4')

    def __init__(self):
        layout = [
            [sg.Output(size=(27, 2)), sg.Button('Del')],
            [sg.Button('7'),sg.Button('8'),sg.Button('9'),sg.Button('.'),sg.Button('Raiz Quadr.')],
            [sg.Button('4'),sg.Button('5'),sg.Button('6'),sg.Button('/'),sg.Button('//Potência',size=(10,0))],
            [sg.Button('1'),sg.Button('2'),sg.Button('3'),sg.Button('*'),sg.Button('!Fatorial',size=(10,0))],
            [sg.Button('+'),sg.Button('0',size=(1,1)),sg.Button('-',size=(1,0)),sg.Button(','),sg.Button('Enter->',size=(10,1))]
        ]
        self.janela = sg.Window("Calculadora V0.1").layout(layout)

    def iniciar(self):
        while True:
            self.evento, self.values = self.janela.read()
            if self.evento == sg.WINDOW_CLOSED:
                break

tela = Calculadora()
tela.iniciar()