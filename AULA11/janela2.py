import tkinter as tk
from tkinter import messagebox


def monstrar_nome():
    nome=entrada.get().strip()

    if nome:
        messagebox.showinfo("Cadastro",f"Olá,{nome}!")
    else:
        messagebox.showwarning("Atencao","informe seu nome.")

def janela_nome():
    global entrada
    janela.title("Sistema de cadastro")
    tk.Label(janela,text="nome:").pack(pady=5)
    entrada=tk.Entry(janela)
    entrada.pack(padx=16)
    tk.Button(janela,text="Enviar",command=monstrar_nome).pack(pady=10)


def frames():
    frame_a=tk.Frame()
    frame_b=tk.Frame()
    label_a=tk.Label(master=frame_a,text="Frame A")
    label_a.pack()

    label_b=tk.Label(master=frame_b,text="Frame B")
    label_b.pack()

    frame_b.pack()
    frame_a.pack()

def effects():
    border_effects={
        "flat":tk.FLAT,
        "afundado":tk.SUNKEN,
        "elevado":tk.RAISED,
        "borda":tk.GROOVE,
        "ondulado":tk.RIDGE,
    }

    for relief_name,relief in border_effects.items():
        frame=tk.Frame(master=janela,relief=relief,borderwidth=5)
        frame.pack(side=tk.LEFT)
        label=tk.Label(master=frame,text=relief_name)
        label.pack()
    








if __name__ =="__main__":
    janela=tk.Tk()
    effects()
    janela.mainloop()

