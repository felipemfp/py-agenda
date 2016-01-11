# coding: utf-8

from Models.Contato import Contato
import sqlite3

ARQUIVO_DB = "data.db"

con = sqlite3.connect(ARQUIVO_DB)
cur = con.cursor()

opcao = ""
lista = []

def novo():
    nome = input("Nome?\n")
    telefone = input("Telefone?\n")
    sql = "INSERT INTO Contato (Nome, Telefone) VALUES (?, ?)"
    cur.execute(sql, (nome, telefone))
    salvar()


def editar():
    nome = input("Nome?\n")
    novo_nome = input("Novo nome? (Deixe vazio se não quiser alterar)\n")
    novo_telefone = input("Novo telefone? (Deixe vazio se não quiser alterar)\n")

    set = ""
    if novo_telefone:
        set += "Telefone = ?"

    if novo_nome:
        if set:
            set += ", "
        set += "Nome = ?"

    sql = "UPDATE Contato " \
          "SET " + set + \
          " WHERE Nome LIKE ?"

    if novo_nome and novo_telefone:
        cur.execute(sql, (novo_nome, novo_telefone, nome))
    elif novo_nome:
        cur.execute(sql, (novo_nome, nome))
    elif novo_telefone:
        cur.execute(sql, (novo_telefone, nome))

    salvar()


def remover():
    nome = input("Nome?\n")
    sql = "DELETE FROM Contato " \
          "WHERE Nome LIKE ?"
    cur.execute(sql, (nome,))
    salvar()


def listar():
    for contato in lista:
        print(contato)


def salvar():
    con.commit()
    carregar()


def carregar():
    global lista
    try:
        lista = []
        cur.execute("SELECT * FROM Contato")
        for row in cur.fetchall():
            lista.append(Contato(row[1], row[2]))
    except:
        sql = "CREATE TABLE Contato " \
              "(Id INTEGER PRIMARY KEY AUTOINCREMENT, " \
              "Nome VARCHAR(255) NOT NULL, " \
              "Telefone VARCHAR(255) NOT NULL)"
        cur.execute(sql)


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


con.close()