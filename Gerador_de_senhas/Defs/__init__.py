import random


def truefalse(com_numeros, com_simbolos, com_letras, total):
    total_de_caracteres = int(total)
    if com_simbolos and com_numeros and com_letras:
        new_senha = todos(total_de_caracteres)
        return new_senha
    elif com_letras and com_numeros:
        new_senha = letraenumero(total_de_caracteres)
        return new_senha
    elif com_letras and com_simbolos:
        new_senha = letraesimbolo(total_de_caracteres)
        return new_senha
    elif com_numeros and com_simbolos:
        new_senha = numeroesimbolo(total_de_caracteres)
        return new_senha
    elif com_simbolos == False and com_letras == False:
        new_senha = sonumeros(total_de_caracteres)
        return new_senha
    elif com_numeros == False and com_simbolos == False:
        new_senha = soletras(total_de_caracteres)
        return new_senha
    if com_letras == False and com_numeros == False:
        new_senha = sosimbolos(total_de_caracteres)
        return new_senha
    else:
        new_senha = 'Escolha uma opção acima !'
        return new_senha


def numeroesimbolo(n):
    char_list = '0123456789@,.-_#!%*&/?/^+-"'
    char = random.choices(char_list, k=int(n))
    new_pass = ''.join(char)
    return new_pass


def letraesimbolo(n):
    char_list = 'abcdefghijlmnopqrstuvxyz@,.-_#!%*&/?/^+-"'
    char = random.choices(char_list, k=int(n))
    new_pass = ''.join(char)
    return new_pass


def letraenumero(n):
    char_list = 'abcdefghijlmnopqrstuvxyz0123456789'
    char = random.choices(char_list, k=int(n))
    new_pass = ''.join(char)
    return new_pass


def todos(n):
    char_list = 'abcdefghijlmnopqrstuvxyz0123456789@,.-_#!%*&/?/^+-"'
    char = random.choices(char_list, k=int(n))
    new_pass = ''.join(char)
    return new_pass


def semsimbolos(n):
    char_list = 'abcdefghijlmnopqrstuvxyz0123456789'
    char = random.choices(char_list, k=int(n))
    new_pass = ''.join(char)
    return new_pass


def semletras(n):
    char_list = '0123456789@,.-_#!%*&/?/^+-"'
    char = random.choices(char_list, k=int(n))
    new_pass = ''.join(char)
    return new_pass


def semnumero(n):
    char_list = 'abcdefghijlmnopqrstuvxyz@,.-_#!%*&/?/^+-"'
    char = random.choices(char_list, k=int(n))
    new_pass = ''.join(char)
    return new_pass


def soletras(n):
    char_list = 'abcdefghijlmnopqrstuvxyz'
    char = random.choices(char_list, k=int(n))
    new_pass = ''.join(char)
    return new_pass


def sonumeros(n):
    char_list = '0123456789'
    char = random.choices(char_list, k=int(n))
    new_pass = ''.join(char)
    return new_pass


def sosimbolos(n):
    char_list = '@,.-_#!%*&/?/^+-"'
    char = random.choices(char_list, k=int(n))
    new_pass = ''.join(char)
    return new_pass
