# coding: utf-8

from Models.Contato import Contato
import pickle

ARQUIVO = r"lista.dat"

opcao = ""
lista = []

def novo():
    nome = input("Nome?\n")
    telefone = input("Telefone?\n")
    contato = Contato(nome, telefone)
    lista.append(contato)
    salvar()


def editar():
    nome = input("Nome?\n")
    novo_nome = input("Novo nome? (Deixe vazio se não quiser alterar)\n")
    novo_telefone = input("Novo telefone? (Deixe vazio se não quiser alterar)\n")
    for i in range(len(lista)):
        if lista[i].nome == nome:
            lista[i].nome = novo_nome
            lista[i].telefone = novo_telefone
            break
    salvar()


def remover():
    nome = input("Nome?\n")
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
        print(c)


def salvar():
    pickle.dump(lista, open(ARQUIVO, "wb"))


def carregar():
    global lista
    try:
        lista = pickle.load(open(ARQUIVO, "rb"))
    except:
        pickle.dump(lista, open(ARQUIVO, "wb"))


carregar()


while opcao != "0":
    print("#############################\n0: sair | 1: novo | 2: listar | 3: editar | 4: remover")
    opcao = input("O que deseja fazer?")
    if opcao == "1":
        novo()
    elif opcao == "2":
        listar()
        input()
    elif opcao == "3":
        editar()
    elif opcao == "4":
        remover()