from tkinter import *
from PIL import Image, ImageTk
from Functions import *
from time import strftime as time
from datetime import date

#from tkinter import messagebox,import columns as columns,from tkinter import ttk



class Frames:
    def __init__(self, nome, bg="#E0FFFF", relevo="ridge", borda="2"):
        """
        Configura Frames de forma simples
        chamar a função " .config() " para funcionar !!
        :param nome: Nome do Frame
        :param bg: Cor de fundo do frame
        :param relevo: Relevo do frame
        :param borda: Borda do frame
        """
        self.nome = nome
        self.relevo = relevo
        self.borda = borda
        self.cordefundo = bg

    def config(self):
        self.nome.configure(relief=self.relevo)
        self.nome.configure(borderwidth=self.borda)
        self.nome.configure(background=self.cordefundo)
        self.nome.configure(highlightbackground="#d9d9d9")
        self.nome.configure(highlightcolor="black")


class Mensagens:
    def __init__(self, nome, msg, tam=12, bg="#2BC48A", fg="#000000"):
        """
        Está é uma claase para configurar uma msg, com
        os seguites parametros e funcionalidades extras
        como mudar cor da letra e cor da fonte!
        chamar a função " .config() " para funcionar !!
        :param nome: Nome da mensagem a ser modificada
        :param msg: Mensagem a ser exibida
        :param tam: (( Opçional )) Tamanho da fonte da mensagem
        :param bg: (( Opçional )) Cor do fundo da mensagem
        :param fg: (( Opçional )) Cor da letra da menssagem
        """
        self.nome = nome
        self.mensagem = str(msg)
        self.font = "-family {Segoe UI} -size"f" {tam} ""-weight bold"
        self.cordefundo = bg
        self.cordaletra = fg

    def config(self):
        self.nome.configure(text=self.mensagem)
        self.nome.configure(font=self.font)
        self.nome.configure(background=self.cordefundo)
        self.nome.configure(foreground=self.cordaletra)
        self.nome.configure(highlightbackground="#d9d9d9")
        self.nome.configure(highlightcolor="black")
        self.nome.configure(width=290)

#A9D2F6
class RadiosButtons:
    def __init__(self, nome, text, value, variavel):
        """
        Essa Função pega nome,texto,valor e variavel de um radio button
        e faz uma configuração podendo mudar fonte e cor do fundo, cor da letra
        e a cor de quando o radio button está ativado.
        chamar a função " .config() " para funcionar !!
        :param nome: Nome do Radio Button
        :param text: Texto do Radio Button
        :param value: Valor Int Para o Radio Button
        :param variavel: Variavel Responsavel pelos Radios Buttons
        """
        self.nome = nome
        self.text = text
        self.value = value
        self.variavel = variavel
        self.font = "-family {Segoe UI} -size 12 -weight bold"
        self.cordefundo = "#E0FFFF"
        self.cordaletra = "#000000"
        self.corclicado = "#E0FFFF"

    def config(self):
        self.nome.configure(activeforeground="#000000")
        self.nome.configure(disabledforeground="#000000")
        self.nome.configure(highlightbackground="#000000")
        self.nome.configure(highlightcolor="black")
        self.nome.configure(justify='left')
        self.nome.configure(font=self.font)
        self.nome.configure(activebackground=self.corclicado)
        self.nome.configure(foreground=self.cordaletra)
        self.nome.configure(background=self.cordefundo)
        self.nome.configure(text=self.text)
        self.nome.configure(value=self.value)
        self.nome.configure(variable=self.variavel)


class Botoes:
    def __init__(self, nome, texto, comando):
        """
        Configura os Botões de forma pratica é obrigatorio
        chamar a função " .config() " para funcionar !!
        :param nome: Nome do Botão
        :param texto: Texto a ser exibido
        :param comando: Comando ou seja nome da Função a ser chamada
        """
        self.nome = nome
        self.text = str(texto)
        self.command = comando

    def config(self, tam=12, bg="#2BC48A", fg="#000000"):
        """
        Configurações do botão
        :param tam: Tamanho da letras do Botão
        :param bg: Cor do Fundo do Botão
        :param fg: Cor da Letra do Botão
        """
        self.font = "-family {Segoe UI} -size" + f" {tam} " + "-weight bold"
        self.cordefundo = bg
        self.cordaletra = fg

        self.nome.configure(text=self.text)
        self.nome.configure(command=self.command)
        self.nome.configure(foreground=self.cordaletra)
        self.nome.configure(background=self.cordefundo)
        self.nome.configure(font=self.font)
        self.nome.configure(activebackground="#ececec")
        self.nome.configure(activeforeground="#000000")
        self.nome.configure(disabledforeground="#a3a3a3")
        self.nome.configure(highlightbackground="#d9d9d9")
        self.nome.configure(highlightcolor="black")
        self.nome.configure(pady="0")


class SpinBoox:
    def __init__(self, nome,bg="white", fg="black"):
        self.nome = nome
        self.cordefundo = bg
        self.cordaletra = fg

    def config(self):
        self.nome.configure(background=self.cordefundo)
        self.nome.configure(foreground=self.cordaletra)
        self.nome.configure(font="TkDefaultFont")
        self.nome.configure(textvariable="spinbox")
        self.nome.configure(activebackground="#f9f9f9")
        self.nome.configure(buttonbackground="#d9d9d9")
        self.nome.configure(disabledforeground="#a3a3a3")
        self.nome.configure(highlightbackground="black")
        self.nome.configure(highlightcolor="black")
        self.nome.configure(insertbackground="black")
        self.nome.configure(selectbackground="#c4c4c4")
        self.nome.configure(selectforeground="black")



def data_atual():
    """
    Função que pega a dada atual do sistema!
    :return: A data do sistema.
    """
    dataatual = date.today()
    data = dataatual.strftime('%d.%m.%Y')
    return data


def calculadora(n1, n2, tipo="i", sinal="sub"):
    """
    Calculadora de subtrair e multiplicar e dividir.
    comandos = tipos duas opções i para inteiro ou f para float
    :param n1: Numero 1 da calculadora
    :param n2: Numero 2 da calculadora
    :param tipo: "i" para inteiro, "f" para float
    :param sinal: "sub" para subtrair, "mul" paramultiplicar,
    "som" para somar, "div" para dividir.
    :return: a operação feita
    """

    if tipo == "i":
        numero1 = int(n1)
        numero2 = int(n2)
        if sinal == 'sub':
            if numero1 < numero2:
                calculo = numero2 - numero1
                return calculo
            else:
                calculo = numero1 - numero2
                return calculo
        elif sinal == 'mul':
            calculo = numero2 * numero1
            return calculo
        elif sinal == 'som':
            calculo = numero1 + numero2
            return calculo
        elif sinal == 'div':
            calculo = numero1 / numero2
            return calculo
    elif tipo == "f":
        numero1 = float(n1)
        numero2 = float(n2)
        if sinal == 'sub':
            if numero1 < numero2:
                calculo = numero2 - numero1
                return calculo
            else:
                calculo = numero1 - numero2
                return calculo
        elif sinal == 'mul':
            calculo = numero2 * numero1
            return calculo
        elif sinal == 'som':
            calculo = numero1 + numero2
            return calculo
        elif sinal == 'div':
            calculo = numero1 / numero2
            return calculo


def converter_em_str(nomevar):
    if nomevar == 3:
        print("Cartão")
    elif nomevar == 2:
        print("Credito")
    else:
        print("Dinheiro")


def somarttv(treev, msg, pos):
    total = 0.0
    for child in treev.get_children():
        total += float(treev.item(child, 'values')[pos])
    msg.configure(text=total)

def Sairrr(app):
    app.destroy()
    open(main)




