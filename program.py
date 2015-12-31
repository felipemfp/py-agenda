# coding: utf-8

from Models.Contato import Contato

opcao = ""
lista = []


def novo():
    nome = raw_input("Nome?\n")
    telefone = raw_input("Telefone?\n")
    contato = Contato(nome, telefone)
    lista.append(contato)
    salvar()


def editar():
    nome = raw_input("Nome?\n")
    novo_nome = raw_input("Novo nome? (Deixe vazio se não quiser alterar)\n")
    novo_telefone = raw_input("Novo telefone? (Deixe vazio se não quiser alterar)\n")
    for i in range(len(lista)):
        if lista[i].nome == nome:
            lista[i].nome = novo_nome
            lista[i].telefone = novo_telefone
            break
    salvar()


def remover():
    nome = raw_input("Nome?\n")
    index = -1
    for i in range(len(lista)):
        if lista[i].nome == nome:
            index = i
            break
    if index > -1:
        del(lista[index])
        salvar()


def listar():
    for c in lista:
        print(c.tostring())


def salvar():
    arquivo = open(r"lista.txt", "w")
    linhas = []
    for c in lista:
        linhas.append(c.tostring()+"|")
    arquivo.writelines(linhas)
    arquivo.close()


def carregar():
    arquivo = open(r"lista.txt")
    linhas = arquivo.read().split("|")
    arquivo.close()
    for l in linhas:
        if l != "":
            c = l.split(": ")
            lista.append(Contato(c[0], c[1]));


carregar()


while opcao != "0":
    print("---------------------\n0: sair\n1: novo\n2: listar\n3: editar\n4: remover")
    opcao = raw_input("O que deseja fazer?")

    if opcao == "1":
        novo()
    elif opcao == "2":
        listar()
        raw_input()
    elif opcao == "3":
        editar()
    elif opcao == "4":
        remover()