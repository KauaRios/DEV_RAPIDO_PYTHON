import math
import sqlite3
from pathlib import Path


class DB:
    def __init__(self, caminho=None):
        if caminho is None:
            diretorio = Path(__file__).resolve().parent / "DB"
            diretorio.mkdir(exist_ok=True)
            caminho = diretorio / "banco.db"
        self.conexao = sqlite3.connect(caminho)
        self.criar_tabela()

    def criar_tabela(self):
        with self.conexao:
            self.conexao.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    preco REAL NOT NULL,
                    quantidade INTEGER NOT NULL DEFAULT 0
                )
            """)

    def cadastrar_produtos(self, nome, preco, quantidade):
        with self.conexao:
            self.conexao.execute(
                "INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)",
                (nome, preco, quantidade),
            )

    def listar_produtos(self):
        return self.conexao.execute(
            "SELECT id, nome, preco, quantidade FROM produtos ORDER BY id"
        ).fetchall()

    def buscar_produto(self, nome):
        return self.conexao.execute(
            "SELECT id, nome, preco, quantidade FROM produtos WHERE nome LIKE ? ORDER BY id",
            (f"%{nome}%",),
        ).fetchall()

    def atualizar_produto(self, id, nome, preco, quantidade):
        with self.conexao:
            cursor = self.conexao.execute(
                "UPDATE produtos SET nome = ?, preco = ?, quantidade = ? WHERE id = ?",
                (nome, preco, quantidade, id),
            )
            return cursor.rowcount > 0

    def excluir_produto(self, id):
        with self.conexao:
            cursor = self.conexao.execute("DELETE FROM produtos WHERE id = ?", (id,))
            return cursor.rowcount > 0

    def fechar(self):
        self.conexao.close()


def pedir_nome():
    while True:
        nome = input("Digite o nome do produto: ").strip()
        if nome:
            return nome
        print("O nome não pode ficar vazio.")


def pedir_numero(mensagem, tipo):
    while True:
        try:
            valor = tipo(input(mensagem))
            if valor < 0 or (tipo is float and not math.isfinite(valor)):
                print("Digite um número válido que não seja negativo.")
                continue
            return valor
        except ValueError:
            print("Digite um número válido.")


def mostrar_produtos(produtos):
    if not produtos:
        print("Nenhum produto encontrado.")
        return
    for id, nome, preco, quantidade in produtos:
        print(f"ID: {id} | Nome: {nome} | Preço: R$ {preco:.2f} | Quantidade: {quantidade}")


def main():
    db = DB()
    try:
        while True:
            opcao = input("""
        MENU CADASTRO
        1 - Cadastrar produto
        2 - Listar produtos
        3 - Buscar produto pelo nome
        4 - Remover produto pelo ID
        5 - Atualizar produto pelo ID
        0 - Sair

        Escolha uma opção: """).strip()

            if opcao == "0":
                print("Saindo do sistema.")
                break
            try:
                if opcao == "1":
                    nome = pedir_nome()
                    preco = pedir_numero("Digite o preço: ", float)
                    quantidade = pedir_numero("Digite a quantidade: ", int)
                    db.cadastrar_produtos(nome, preco, quantidade)
                    print("Produto cadastrado com sucesso.")
                elif opcao == "2":
                    mostrar_produtos(db.listar_produtos())
                elif opcao == "3":
                    nome = pedir_nome()
                    mostrar_produtos(db.buscar_produto(nome))
                elif opcao == "4":
                    id = pedir_numero("Digite o ID do produto: ", int)
                    print("Produto removido." if db.excluir_produto(id) else "ID não encontrado.")
                elif opcao == "5":
                    id = pedir_numero("Digite o ID do produto: ", int)
                    nome = pedir_nome()
                    preco = pedir_numero("Digite o novo preço: ", float)
                    quantidade = pedir_numero("Digite a nova quantidade: ", int)
                    atualizado = db.atualizar_produto(id, nome, preco, quantidade)
                    print("Produto atualizado." if atualizado else "ID não encontrado.")
                else:
                    print("Opção inválida.")
            except sqlite3.Error as erro:
                print(f"Erro no banco de dados: {erro}")
    finally:
        db.fechar()


if __name__ == "__main__":
    main()
