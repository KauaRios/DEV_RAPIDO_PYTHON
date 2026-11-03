import tkinter as tk
from tkinter import ttk


class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade


class Aplicativo:
    def __init__(self, raiz):
        raiz.title("Preeview")
        raiz.geometry("500x400")
        self.tabela = ttk.Treeview(raiz, columns=("nome", "idade"), show="headings")
        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("idade", text="Idade")
        self.tabela.column("nome", width=330)
        self.tabela.column("idade", width=100, anchor="center")
        self.tabela.pack(fill="both", expand=True, padx=20, pady=20)


class ArvorePessoa:
    def __init__(self):
        self.nome
        self.idade
        

    def inserir_arvore(self):
       self.tabela.insert("","end",values=("Ana","20"))
       self.tabela.insert("","end",values=("Bruno",29))

        

      



        
