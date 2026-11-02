import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class CadastroApp:
    def __init__(self, raiz):

        raiz.columnconfigure(0, weight=1)
        raiz.columnconfigure(1, weight=1)

        ttk.Label(
            raiz, text="Nome:"
        ).grid(row=0, column=0, sticky="e", padx=5, pady=10)

        self.nome = ttk.Entry(raiz)
        self.nome.grid(row=0, column=1, sticky="w", padx=5, pady=10)

        ttk.Label(
            raiz, text="Telefone:"
        ).grid(row=1, column=0, sticky="e", padx=5, pady=10)

        self.telefone = ttk.Entry(raiz)
        self.telefone.grid(row=1, column=1, sticky="w", padx=5, pady=10)


        self.botao = ttk.Button(
            raiz,
            text="Cadastrar",
            command=self.cadastrar
        )

        self.botao.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=20
        )
        self.lista=tk.Listbox(raiz,height=10,width=45)
        self.lista.grid(row=3,column=0,columnspan=2,pady=10)
    def cadastrar(self):
        nome=self.nome.get().strip()
        telefone=self.telefone.get().strip()

        if not nome or not telefone:
            messagebox.showwarning("Atenção","Preencha todos os campos")
            return
        if not telefone.isdigit():
            messagebox.showerror("Erro","O telefone deve conter numeros")
            return
        
        

        self.lista.insert(tk.END,f"Contato:{nome} Telefone:{telefone}")
        self.nome.delete(0,tk.END)
        self.telefone.delete(0,tk.END)



if __name__ == "__main__":
    raiz = tk.Tk()
    raiz.title("Cadastro")
    raiz.geometry("500x600")

    CadastroApp(raiz)
    raiz.mainloop()

