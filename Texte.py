

Labelframe1 = LabelFrame(app)
Labelframe1.place(relx=0.013, rely=0.154, relheight=0.81, relwidth=0.467)
Labelframe1.configure(relief='groove')
Labelframe1.configure(foreground="black")
Labelframe1.configure(text='''Detalhes da Compra''')
Labelframe1.configure(background="#A9D2F6")
Labelframe1.configure(highlightbackground="#d9d9d9")
Labelframe1.configure(highlightcolor="black")

botao_nova_venda = Button(Labelframe1)
botao_nova_venda.place(relx=0.07, rely=0.878, height=24, width=87, bordermode='ignore')
botao_nova_venda.configure(activebackground="#ececec")
botao_nova_venda.configure(activeforeground="#000000")
botao_nova_venda.configure(background="#F7C155")
botao_nova_venda.configure(disabledforeground="#a3a3a3")
botao_nova_venda.configure(font="-family {Segoe UI} -size 10 -weight bold")
botao_nova_venda.configure(foreground="#000000")
botao_nova_venda.configure(highlightbackground="#d9d9d9")
botao_nova_venda.configure(highlightcolor="black")
botao_nova_venda.configure(pady="0")
botao_nova_venda.configure(text='''Nova Venda''')
botao_nova_venda.configure(textvariable="novaVenda")

botao_remover = Button(Labelframe1)
botao_remover.place(relx=0.728, rely=0.884, height=24, width=66, bordermode='ignore')
botao_remover.configure(activebackground="#ececec")
botao_remover.configure(activeforeground="#000000")
botao_remover.configure(background="#e80000")
botao_remover.configure(disabledforeground="#a3a3a3")
botao_remover.configure(font="-family {Segoe UI} -size 10 -weight bold")
botao_remover.configure(foreground="#000000")
botao_remover.configure(highlightbackground="#d9d9d9")
botao_remover.configure(highlightcolor="black")
botao_remover.configure(pady="0")
botao_remover.configure(text='''Remover''')
botao_remover.configure(textvariable="remover")

Message1 = Message(Labelframe1)
Message1.place(relx=0.027, rely=0.084, relheight=0.03, relwidth=0.142, bordermode='ignore')
Message1.configure(background="#A9D2F6")
Message1.configure(font="-family {Segoe UI} -size 10 -weight bold")
Message1.configure(foreground="#000000")
Message1.configure(highlightbackground="#d9d9d9")
Message1.configure(highlightcolor="black")
Message1.configure(text='''Qtd''')
Message1.configure(width=53)

Message2 = Message(Labelframe1)
Message2.place(relx=0.18, rely=0.078, relheight=0.051, relwidth=0.212, bordermode='ignore')
Message2.configure(background="#A9D2F6")
Message2.configure(font="-family {Segoe UI} -size 10 -weight bold")
Message2.configure(foreground="#000000")
Message2.configure(highlightbackground="#d9d9d9")
Message2.configure(highlightcolor="black")
Message2.configure(text='''Produtos''')
Message2.configure(width=60)

Message3 = Message(Labelframe1)
Message3.place(relx=0.535, rely=0.078, relheight=0.051, relwidth=0.18, bordermode='ignore')
Message3.configure(background="#A9D2F6")
Message3.configure(font="-family {Segoe UI} -size 10 -weight bold")
Message3.configure(foreground="#000000")
Message3.configure(highlightbackground="#d9d9d9")
Message3.configure(highlightcolor="black")
Message3.configure(text='''Valor U.''')
Message3.configure(width=50)

Message4 = Message(Labelframe1)
Message4.place(relx=0.715, rely=0.078, relheight=0.051, relwidth=0.177, bordermode='ignore')
Message4.configure(background="#A9D2F6")
Message4.configure(font="-family {Segoe UI} -size 10 -weight bold")
Message4.configure(foreground="#000000")
Message4.configure(highlightbackground="#d9d9d9")
Message4.configure(highlightcolor="black")
Message4.configure(text='''Total''')
Message4.configure(width=50)

TSeparator2 = ttk.Separator(Labelframe1)
TSeparator2.place(relx=0.519, rely=0.057, relheight=0.049, bordermode='ignore')
TSeparator2.configure(orient="vertical")

TSeparator3 = ttk.Separator(Labelframe1)
TSeparator3.place(relx=0.183, rely=0.057, relheight=0.049, bordermode='ignore')
TSeparator3.configure(orient="vertical")

TSeparator4 = ttk.Separator(Labelframe1)
TSeparator4.place(relx=0.731, rely=0.059, relheight=0.049, bordermode='ignore')
TSeparator4.configure(orient="vertical")

Spinbox1 = Spinbox(app, from_=1.0, to=100.0)
Spinbox1.place(relx=0.289, rely=0.085, relheight=0.043, relwidth=0.04)
Spinbox1.configure(activebackground="#f9f9f9")
Spinbox1.configure(background="white")
Spinbox1.configure(buttonbackground="#d9d9d9")
Spinbox1.configure(disabledforeground="#a3a3a3")
Spinbox1.configure(font="TkDefaultFont")
Spinbox1.configure(foreground="black")
Spinbox1.configure(highlightbackground="black")
Spinbox1.configure(highlightcolor="black")
Spinbox1.configure(insertbackground="black")
Spinbox1.configure(selectbackground="#c4c4c4")
Spinbox1.configure(selectforeground="black")
Spinbox1.configure(textvariable="spinbox")

Entry1 = Entry(app)
Entry1.place(relx=0.025, rely=0.085, height=20, relwidth=0.244)
Entry1.configure(background="white")
Entry1.configure(disabledforeground="#a3a3a3")
Entry1.configure(font="TkFixedFont")
Entry1.configure(foreground="#000000")
Entry1.configure(highlightbackground="#d9d9d9")
Entry1.configure(highlightcolor="black")
Entry1.configure(insertbackground="black")
Entry1.configure(selectbackground="#c4c4c4")
Entry1.configure(selectforeground="black")

botao_adicionar = Button(app)
botao_adicionar.place(relx=0.364, rely=0.085, height=24, width=67)
botao_adicionar.configure(activebackground="#ececec")
botao_adicionar.configure(activeforeground="#000000")
botao_adicionar.configure(background="#1C86B4")
botao_adicionar.configure(disabledforeground="#a3a3a3")
botao_adicionar.configure(font="-family {Segoe UI} -size 10 -weight bold")
botao_adicionar.configure(foreground="#000000")
botao_adicionar.configure(highlightbackground="#d9d9d9")
botao_adicionar.configure(highlightcolor="black")
botao_adicionar.configure(pady="0")
botao_adicionar.configure(text='''Adicionar''')

radio_cartao = Radiobutton(app)
radio_cartao.place(relx=0.565, rely=0.068, relheight=0.101, relwidth=0.18)
radio_cartao.configure(activebackground="#ececec")
radio_cartao.configure(activeforeground="#000000")
radio_cartao.configure(background="#A9D2F6")
radio_cartao.configure(disabledforeground="#a3a3a3")
radio_cartao.configure(font="-family {Segoe UI} -size 10 -weight bold")
radio_cartao.configure(foreground="#000000")
radio_cartao.configure(highlightbackground="#d9d9d9")
radio_cartao.configure(highlightcolor="black")
radio_cartao.configure(justify='left')
radio_cartao.configure(text='''Cartão''')
radio_cartao.configure(variable="selectedButton")

radio_dinheiro = Radiobutton(app)
radio_dinheiro.place(relx=0.515, rely=0.137, relheight=0.08, relwidth=0.129)
radio_dinheiro.configure(activebackground="#ececec")
radio_dinheiro.configure(activeforeground="#000000")
radio_dinheiro.configure(background="#A9D2F6")
radio_dinheiro.configure(disabledforeground="#a3a3a3")
radio_dinheiro.configure(font="-family {Segoe UI} -size 10 -weight bold")
radio_dinheiro.configure(foreground="#000000")
radio_dinheiro.configure(highlightbackground="#d9d9d9")
radio_dinheiro.configure(highlightcolor="black")
radio_dinheiro.configure(justify='left')
radio_dinheiro.configure(text='''Dinheiro''')
radio_dinheiro.configure(variable="selectedButton")

radio_credito = Radiobutton(app)
radio_credito.place(relx=0.503, rely=0.017, relheight=0.084, relwidth=0.142)
radio_credito.configure(activebackground="#ececec")
radio_credito.configure(activeforeground="#000000")
radio_credito.configure(background="#A9D2F6")
radio_credito.configure(disabledforeground="#a3a3a3")
radio_credito.configure(font="-family {Segoe UI} -size 10 -weight bold")
radio_credito.configure(foreground="#000000")
radio_credito.configure(highlightbackground="#d9d9d9")
radio_credito.configure(highlightcolor="black")
radio_credito.configure(justify='left')
radio_credito.configure(text='''Credito''')
radio_credito.configure(variable="selectedButton")

TCombobox1 = ttk.Combobox(app)
TCombobox1.place(relx=0.716, rely=0.085, relheight=0.046, relwidth=0.255)
TCombobox1.configure(textvariable="combobox")
TCombobox1.configure(takefocus="")

botao_finalizar = Button(app)
botao_finalizar.place(relx=0.678, rely=0.855, height=34, width=97)
botao_finalizar.configure(activebackground="#ececec")
botao_finalizar.configure(activeforeground="#000000")
botao_finalizar.configure(background="#1C86B4")
botao_finalizar.configure(disabledforeground="#a3a3a3")
botao_finalizar.configure(font="-family {Segoe UI} -size 10 -weight bold")
botao_finalizar.configure(foreground="#000000")
botao_finalizar.configure(highlightbackground="#d9d9d9")
botao_finalizar.configure(highlightcolor="black")
botao_finalizar.configure(pady="0")
botao_finalizar.configure(text='''Finalizar''')

msg_produto = Message(app)
msg_produto.place(relx=-0.05, rely=0.034, relheight=0.051, relwidth=0.25)
msg_produto.configure(background="#A9D2F6")
msg_produto.configure(font="-family {Segoe UI} -size 12 -weight bold")
msg_produto.configure(foreground="#000000")
msg_produto.configure(highlightbackground="#d9d9d9")
msg_produto.configure(highlightcolor="black")
msg_produto.configure(text='''Produto''')
msg_produto.configure(width=150)

msg_qtd = Message(app)
msg_qtd.place(relx=0.289, rely=0.034, relheight=0.051, relwidth=0.036)
msg_qtd.configure(background="#A9D2F6")
msg_qtd.configure(font="-family {Segoe UI} -size 11 -weight bold")
msg_qtd.configure(foreground="#000000")
msg_qtd.configure(highlightbackground="#d9d9d9")
msg_qtd.configure(highlightcolor="black")
msg_qtd.configure(text='''Qtd''')
msg_qtd.configure(width=29)

msg_qtd_parcelas = Message(app)
msg_qtd_parcelas.place(relx=0.729, rely=0.034, relheight=0.051, relwidth=0.25)
msg_qtd_parcelas.configure(background="#A9D2F6")
msg_qtd_parcelas.configure(font="-family {Segoe UI} -size 10 -weight bold")
msg_qtd_parcelas.configure(foreground="#000000")
msg_qtd_parcelas.configure(highlightbackground="#d9d9d9")
msg_qtd_parcelas.configure(highlightcolor="black")
msg_qtd_parcelas.configure(text='''Quantidade de Parcelas''')
msg_qtd_parcelas.configure(width=150)

Frame1 = Frame(app)
Frame1.place(relx=0.678, rely=0.171, relheight=0.232, relwidth=0.29)
Frame1.configure(relief='groove')
Frame1.configure(borderwidth="2")
Frame1.configure(relief="groove")
Frame1.configure(background="#F7C155")
Frame1.configure(highlightbackground="#d9d9d9")
Frame1.configure(highlightcolor="black")

msg_valor_total = Message(Frame1)
msg_valor_total.place(relx=0.061, rely=0.096, relheight=0.199, relwidth=0.805)
msg_valor_total.configure(background="#F7C155")
msg_valor_total.configure(font="-family {Segoe UI} -size 15 -weight bold")
msg_valor_total.configure(foreground="#000000")
msg_valor_total.configure(highlightbackground="#d9d9d9")
msg_valor_total.configure(highlightcolor="black")
msg_valor_total.configure(text='''Valor Total''')
msg_valor_total.configure(width=125)

total = Message(Frame1)
total.place(relx=0.056, rely=0.382, relheight=0.478, relwidth=0.857)
total.configure(background="#F7C155")
total.configure(font="-family {Segoe UI} -size 24 -weight bold")
total.configure(foreground="#000000")
total.configure(highlightbackground="#d9d9d9")
total.configure(highlightcolor="black")
total.configure(text='''R$ 0,00''')
total.configure(textvariable="Total")
total.configure(width=141)

input_troco = Entry(app)
input_troco.place(relx=0.603, rely=0.513, height=20, relwidth=0.231)
input_troco.configure(background="white")
input_troco.configure(disabledforeground="#a3a3a3")
input_troco.configure(font="TkFixedFont")
input_troco.configure(foreground="#000000")
input_troco.configure(highlightbackground="#d9d9d9")
input_troco.configure(highlightcolor="black")
input_troco.configure(insertbackground="black")
input_troco.configure(selectbackground="#c4c4c4")
input_troco.configure(selectforeground="black")
input_troco.configure(textvariable="inputTroco")

msg_troco = Message(app)
msg_troco.place(relx=0.49, rely=0.496, relheight=0.075, relwidth=0.118)
msg_troco.configure(background="#A9D2F6")
msg_troco.configure(font="-family {Segoe UI} -size 12 -weight bold")
msg_troco.configure(foreground="#000000")
msg_troco.configure(highlightbackground="#d9d9d9")
msg_troco.configure(highlightcolor="black")
msg_troco.configure(text='''Troco''')
msg_troco.configure(width=70)

Frame2 = Frame(app)
Frame2.place(relx=0.603, rely=0.598, relheight=0.21, relwidth=0.275)
Frame2.configure(relief='groove')
Frame2.configure(borderwidth="2")
Frame2.configure(relief="groove")
Frame2.configure(background="#BBD853")
Frame2.configure(highlightbackground="#d9d9d9")
Frame2.configure(highlightcolor="black")

troco = Message(Frame2)
troco.place(relx=0.059, rely=0.211, relheight=0.65, relwidth=0.826)
troco.configure(background="#BBD853")
troco.configure(font="-family {Segoe UI} -size 22 -weight bold")
troco.configure(foreground="#000000")
troco.configure(highlightbackground="#d9d9d9")
troco.configure(highlightcolor="black")
troco.configure(text='''R$ 0,00''')
troco.configure(textvariable="Troco")
troco.configure(width=136)

botao_troco = Button(app)
botao_troco.place(relx=0.867, rely=0.513, height=24, width=77)
botao_troco.configure(activebackground="#ececec")
botao_troco.configure(activeforeground="#000000")
botao_troco.configure(background="#1C86B4")
botao_troco.configure(disabledforeground="#a3a3a3")
botao_troco.configure(font="-family {Segoe UI} -size 10 -weight bold")
botao_troco.configure(foreground="#000000")
botao_troco.configure(highlightbackground="#d9d9d9")
botao_troco.configure(highlightcolor="black")
botao_troco.configure(pady="0")
botao_troco.configure(text='''Calcular''')
botao_troco.configure(textvariable="CalcularTroco")

porcentagem = ttk.Combobox(app)
porcentagem.place(relx=0.628, rely=0.444, relheight=0.036, relwidth=0.067)
porcentagem.configure(textvariable="combobox")
porcentagem.configure(takefocus="")

radio_desconto = Radiobutton(app)
radio_desconto.place(relx=0.49, rely=0.427, relheight=0.079, relwidth=0.128)
radio_desconto.configure(activebackground="#ececec")
radio_desconto.configure(activeforeground="#000000")
radio_desconto.configure(background="#A9D2F6")
radio_desconto.configure(disabledforeground="#a3a3a3")
radio_desconto.configure(font="-family {Segoe UI} -size 10 -weight bold")
radio_desconto.configure(foreground="#000000")
radio_desconto.configure(highlightbackground="#d9d9d9")
radio_desconto.configure(highlightcolor="black")
radio_desconto.configure(justify='left')
radio_desconto.configure(text='''Desconto''')
radio_desconto.configure(variable="selectedButton")


