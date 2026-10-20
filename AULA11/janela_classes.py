import tkinter as tk
from tkinter import ttk



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
        a.grid(row=0,column=0,sticky="nsew")
        b=tk.Label(raiz,text="B",bg="blue",fg="white")
        b.grid(row=1,column=0,sticky="sw")
                    


if __name__=="__main__":
    raiz=tk.Tk()
    GradeApp(raiz)
    raiz.mainloop()
