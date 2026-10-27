import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random



class App:
    def __init__(self,raiz):
        self.label=ttk.Label(raiz,text="Pronto!") 
        self.label.pack(pady=12)
        ttk.Button(raiz,text="clique",
                   command=self.clicar).pack()

    def clicar(self):
        self.label.config(text="Voce clicou!")


class PackApp:
    def __init__(self,raiz):
        tamanhos=[(100,"red"),(50,"green"),(25,"blue")]
        for tamanho,cor in tamanhos:
            frame=tk.Frame(
                raiz,width=tamanho,height=tamanho,bg=cor
            )
            frame.pack()

class PackFillApp:
    def __init__(self,raiz):
        tamanhos=[(100,"red"),(50,"green"),(25,"blue")]
        for tamanho,cor in tamanhos:
            frame=tk.Frame(
                raiz,width=tamanho,height=tamanho,bg=cor
            )
            frame.pack(fill=tk.X)

class PackSideApp:
    def __init__(self,raiz):
        tamanhos=[(200,"red"),(100,"green"),(50,"blue")]
        for tamanho,cor in tamanhos:
            frame=tk.Frame(
                raiz,width=tamanho,height=tamanho,bg=cor
            )
            frame.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

class PlaceApp:
    def __init__(self,raiz):
        area=tk.Frame(raiz,width=260,height=210)
        area.pack()
        a=tk.Label(area,text="X:0 / Y:0",bg="red")
        b=tk.Label(area,text="X:75 / Y:75",bg="lightblue")
        a.place(x=0,y=0)
        b.place(x=75,y=75)

class GridApp:
    def __init__(self,raiz):
        for linha in range(3):
            for coluna in range(3):
                frame=tk.Frame(raiz,relief=tk.RAISED,bd=1)
                frame.grid(row=linha,column=coluna,padx=5,pady=5)
                texto=f"Linha {linha}\nColuna{coluna}"
                tk.Label(frame,text=texto).pack()

class GridResponsivoApp:
    def __init__(self,raiz):
            for posicao in range(3):
                raiz.columnconfigure(posicao,weight=1,minsize=75)
                raiz.rowconfigure(posicao,weight=1,minsize=50)
            for linha in range(3):
                for coluna in range(3):
                    texto=f"{linha},{coluna}"
                    label=tk.Label(raiz,text=texto,relief=tk.RAISED)
                    label.grid(row=linha,column=coluna,padx=5,pady=5,sticky="nsew")

class GradeApp:
    def __init__(self,raiz):
        raiz.title("Exemplo de sticky")
        raiz.columnconfigure(0,minsize=250)
        raiz.rowconfigure((0,1),minsize=100)
        a=tk.Label(raiz,text="A",bg="red",fg="white")
        a.grid(row=0,column=0,sticky="ne")
        b=tk.Label(raiz,text="B",bg="blue",fg="white")
        b.grid(row=1,column=0,sticky="sw")


class EventoApp:
    def __init__(self,raiz):
        raiz.title("Evento de botão")
        self.label=ttk.Label(raiz,text="Olá tkinter")
        self.label.pack(pady=10)
        botao=ttk.Button(raiz,text="Clique em mim",command=self.clicado)
        botao.pack(pady=10)


    def clicado(self):
        self.label.config(text="botão clicado")                    

class FocoApp:
    def __init__(self,raiz):
        self.texto_padrao="Digite seu nome aqui"
        self.entrada=tk.Entry(raiz,fg="gray",width=30)
        self.entrada.insert(0,self.texto_padrao)
        self.entrada.pack(pady=20)
        self.entrada.bind("<FocusIn>",self.limpar)
        self.entrada.bind("<FocusOut>",self.restaurar)
        self.entrada2=tk.Entry(raiz,fg="gray",width=30)
        self.entrada2.insert(0,self.texto_padrao)
        self.entrada2.pack(pady=20)

    def limpar(self,_):
        if self.entrada.get()==self.texto_padrao:
            self.entrada.delete(0,tk.END)
            self.entrada.config(fg="black")
    def restaurar(self,_):
        if not self.entrada.get()==self.texto_padrao:
            self.entrada.delete(0,tk.END)
            self.entrada.config(fg="gray")
class MenuApp:

    def __init__(self, raiz):
        self.raiz = raiz
        raiz.title ("Menu da aplicação")
        raiz.geometry("360x220") 
        barra = tk.Menu(raiz)
        arquivo = tk.Menu(barra, tearoff=False)
        arquivo.add_command(label="Novo", command=self.novo)
        arquivo.add_separator()
        arquivo.add_command(label="Sair", command=raiz.destroy)
        barra.add_cascade(label="Arquivo", menu=arquivo)
        ajuda = tk.Menu(barra, tearoff=False)
        ajuda.add_command(label="Sobre", command=self.sobre)
        barra.add_cascade(label="Ajuda", menu=ajuda)
        raiz.config(menu=barra)  


    def novo(self):
        messagebox.showinfo("Novo", "Novo cadastro.")
    def sobre(self):
        janela_sobre = tk.Toplevel(self.raiz)
        janela_sobre.title("Sobre")
        tk.Label(janela_sobre,
                    text="Aplicação didática de RAD").pack(
                     padx=20, pady=20
                    )


class AppMeses:
    def __init__(self, raiz):
        raiz.geometry("270x130")
        raiz.title("Exemplo Combobox")
        ttk.Label(raiz, text="Selecione um mês:").pack(pady=5)
        meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        self.combo = ttk.Combobox(raiz, values=meses,
                                  state="readonly")
        self.combo.pack(pady=5)
        self.combo.current(0)
        self.combo.bind("<<ComboboxSelected>>", self.selecionar)

    def selecionar(self, _):
        print(f"Mês escolhido: {self.combo.get()}")


class CoresApp:
    def __init__(self, raiz):
        self.raiz = raiz
        self.cores = ["red", "blue", "green", "purple", "pink"]
        raiz.title("Janela do ain pai para")
        raiz.geometry("300x200")
        tk.Label(raiz, text="Janela Sobre!",
                 font=("Arial", 14)).pack(pady=20)
        tk.Button(raiz, text="Mudar Cor",
                  command=self.mudar_cor).pack(pady=10)

    def mudar_cor(self):
        self.raiz.config(bg=random.choice(self.cores))

if __name__=="__main__":
    raiz=tk.Tk()
    CoresApp(raiz)
    raiz.mainloop()
