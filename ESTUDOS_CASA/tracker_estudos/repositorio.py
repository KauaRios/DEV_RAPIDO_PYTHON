import sqlite3
from datetime import date
from materia import Materia
from sessao import Sessao

class Repositorio:
    def __init__(self:object,caminho):
        self.conn=sqlite3.connect(caminho)
        self._criar_tabelas()

    def _criar_tabelas(self):
        cur = self.conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS materias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE NOT NULL,
            meta_semanal INTEGER
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS sessoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            materia TEXT NOT NULL,
            minutos INTEGER NOT NULL,
            data TEXT NOT NULL
        )
    """)

        self.conn.commit()

    def salvar_materia(self, materia):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO materias (nome, meta_semanal) VALUES (?, ?)",
            (materia.nome, materia.meta_semanal),
        )
        self.conn.commit()

    def listar_materias(self):
        cur = self.conn.cursor()
        cur.execute("SELECT nome, meta_semanal FROM materias")
        return [Materia(nome, meta) for nome, meta in cur.fetchall()]

    def salvar_sessao(self, sessao):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO sessoes (materia, minutos, data) VALUES (?, ?, ?)",
            (sessao.materia.nome, sessao.minutos, sessao.data.isoformat()),
        )
        self.conn.commit()

    def listar_sessoes(self):
        cur = self.conn.cursor()
        cur.execute("SELECT materia, minutos, data FROM sessoes")
        return [
            Sessao(Materia(nome, 0), minutos, date.fromisoformat(data))
            for nome, minutos, data in cur.fetchall()
        ]



