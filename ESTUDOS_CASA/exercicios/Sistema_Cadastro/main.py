from warnings import showwarning

from db import Banco
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class InterfaceApp:
    def __init__(self,raiz,controller) -> None:
        self.controller=controller
        self.raiz=raiz
        self.raiz.title("Cadastro")
        self.raiz.geometry("500x400")
        self.criar_treeview()
        self.carregar_usuarios()
        

        self.rotulo=ttk.Label(raiz,text="Nome").grid(row=0, column=0, sticky="e", padx=5, pady=10) 
        
        self.nome = ttk.Entry(raiz)
        self.nome.grid(row=0, column=1, sticky="w", padx=5, pady=10)

        self.rotulo2=ttk.Label(raiz,text="Idade").grid(row=1,column=0,sticky="e",padx=5,pady=10)

        self.idade=ttk.Entry(raiz)
        self.idade.grid(row=1,column=1,sticky="w",padx=5,pady=10)

        self.rotulo3=ttk.Label(raiz,text="Telefone").grid(row=2,column=0,sticky="e",padx=5,pady=10)

        self.telefone=ttk.Entry(raiz)
        self.telefone.grid(row=2,column=1,sticky="w",padx=5,pady=10)
        
        
        self.botao=ttk.Button(raiz,text="Adicionar",command=self.adicionar)

        self.botao.grid(
            row=3,
            column=0,
            padx=10,
            pady=20
        )

        self.botao2=ttk.Button(raiz,text="Remover Usuario",command=self.remover)
        self.botao2.grid(row=3,
                        column=1,
                         padx=10,
                         pady=30)


        

    def adicionar(self):
        nome=self.nome.get()
        idade=self.idade.get()
        telefone=self.telefone.get()

        if not nome or not idade or not telefone:
            messagebox.showwarning(title="Campos não preenchidos",message="Preencha todos os campos")
            return
        self.controller.adicionar(nome,idade,telefone)
        messagebox.showinfo(title="concluido",message="Usuario adicionado com sucesso")
        self.carregar_usuarios()
    def remover(self):
        nome=self.nome.get()
        idade=self.idade.get()
        telefone=self.telefone.get()

        if not nome or not idade or not telefone:
            messagebox.showwarning(title="campos nao preenchidos",message="Preencha todos os campos")
            return
        removidos = self.controller.remover(nome, idade, telefone)

        if removidos > 0:
             messagebox.showinfo("Concluido",f"{removidos} usuarios removidos")
        else:
            messagebox.showwarning("Erro","Nenhum usuario com corresponde aos dados informados")

        self.carregar_usuarios()

    def criar_treeview(self):
        self.tabela=ttk.Treeview(self.raiz,columns=("nome","idade","telefone"),
                                 show="headings"

                                 )

        self.tabela.heading("nome",text="Nome")
        self.tabela.heading("idade",text="Idade")
        self.tabela.heading("telefone",text="Telefone")


        self.tabela.grid(row=4,column=0,columnspan=2,padx=10,pady=10)

    def carregar_usuarios(self):
        self.tabela.delete(*self.tabela.get_children())
        users=self.controller.listar()
        for usuario in users:
            self.tabela.insert("","end",values=usuario)
            
   

  

class InterfaceController:
    def __init__(self):
        self.banco=Banco()

    def adicionar(self,nome,idade,telefone):
        self.banco.adicionar(nome,idade,telefone)
    

    def remover(self,nome,idade,telefone):
        return self.banco.remover(nome, idade, telefone)
    def listar(self):
        return self.banco.listar()
if __name__=="__main__":
    controller=InterfaceController()
    raiz=tk.Tk()
    app=InterfaceApp(raiz,controller)
    raiz.mainloop()
