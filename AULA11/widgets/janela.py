import tkinter as tk
from tkinter import messagebox

def constroi(texto:str="Padrao"):
    ola=tk.Label(text=texto)
    ola.pack()

def janela_perso():
    label=tk.Label(
        text="Brincando com Tkinter",
        foreground="red",
        background="black"
    )
    label.pack()

def janela_seletor_cor():
    label=tk.Label(
        text="Brincando com Tkinter",
        fg="#0000FF",
        bg="#00FFFF",
        width=40,
        height=40
    )
    botao=tk.Button(
        text="Botao",
        width="25",
        heigh="5"
    )
    label.pack()
    botao.pack()

def botao():
    botao=tk.Button(
        text="Botao",
        width=25,
        height=5,
        bg="blue",
        fg="yellow"
    )
    botao.pack()




