"""Primeiro exemplo de janela gráfica com Tkinter."""

import tkinter as tk


if __name__ == "__main__":
    janela = tk.Tk()
    janela.title("Minha primeira janela")
    janela.geometry("400x300")
    janela.mainloop()
