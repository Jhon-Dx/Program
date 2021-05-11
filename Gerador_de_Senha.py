import Gerador_de_senhas.Defs as ge
import PySimpleGUI as sg


class Gerador:
    sg.theme('DarkPurple1')

    def __init__(self):
        layout = [
            [sg.Checkbox('Numeros', key='sonumeros'), sg.Text(size=(3, 1)), sg.Checkbox('Letras', key='soletras'),
            sg.Text(size=(3, 1)), sg.Checkbox('Simbolos', key='sosimbolos')],
            [sg.Text('Quantidade de senhas'), sg.Combo(values=list(range(30)), key='totalchars', default_value=1,
            size=(3, 1))],
            [sg.Text(size=(11, 3)), sg.Button('Gerar Senha')],
            [sg.Text('Resultado:', size=(9, 1)), sg.Text(size=(22, 0))],
            [sg.Output(size=(40, 5))]
        ]
        self.janela = sg.Window("Gerador de Senha").layout(layout)

    def iniciar(self):
        while True:
            self.evento, self.values = self.janela.read()
            com_numeros = self.values['sonumeros']
            com_letras = self.values['soletras']
            com_simbolos = self.values['sosimbolos']
            total_de_caracteres = self.values['totalchars']
            if self.evento == sg.WINDOW_CLOSED:
                break
            if self.evento == 'Gerar Senha':
                newsenha = ge.truefalse(com_numeros, com_simbolos, com_letras, total_de_caracteres)
                print(newsenha)


tela = Gerador()
tela.iniciar()