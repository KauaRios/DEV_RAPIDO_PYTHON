import sqlite3
from pathlib import Path

bancodir=Path(__file__).resolve().parent/"DB"
bancodir.mkdir(exist_ok=True)
class Banco:
    def __init__(self) -> None:
       self.conexao=sqlite3.connect(bancodir/"usuarios.db")
       self.cursor=self.conexao.cursor()
       self.criar_tabela()


    def criar_tabela(self):
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios(
                nome TEXT NOT NULL,
                idade INTEGER,
                telefone TEXT
                )
        """)
            self.conexao.commit()
        except sqlite3.Error as erro:
            self.conexao.rollback()
            print(f"Erro ao criar tabela: {erro}")
            raise


            
    def adicionar(self,nome,idade,telefone):
        self.cursor.execute("INSERT INTO usuarios(nome,idade,telefone) VALUES(?,?,?)",(nome,idade,telefone))

        self.conexao.commit()
    def remover(self,nome,idade,telefone):
        self.cursor.execute("""DELETE FROM usuarios WHERE nome=? AND idade=? AND telefone=?""",(nome,idade,telefone))
        self.conexao.commit()
        removidos=self.cursor.rowcount
        return removidos

    def listar(self):
        self.cursor.execute("SELECT * FROM usuarios")
        return self.cursor.fetchall()

    


    def fechar(self):
        self.conexao.close()
