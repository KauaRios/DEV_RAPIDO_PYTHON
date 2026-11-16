from os.path import exists
from pathlib import Path


class Produto:
    def __init__(self,nome:str,preco:float,quantidade:int) -> None:
        self.nome=nome
        self.preco=preco
        self.quantidade=quantidade
    def __str__(self) -> str:
        return f"Nome: {self.nome} | Preço: R$ {self.preco:.2f} | Quantidade: {self.quantidade}"
        
        

class Controle:
    def __init__(self) -> None:
        self.lista=[]
        base_dir=Path(__file__).parent       
        self.arquivo=base_dir/"arquivo.txt"
        self.carregar()
    def carregar(self):
        try:
            if not self.arquivo.exists():
                print("Arquivo nao existe:")
            else:
                with open(self.arquivo,"r",encoding="utf-8")as arquivo:
                    for linha in arquivo:
                        linha=linha.strip()
                        if ";" in linha:
                           pedaco=linha.split(";")
                           if len(pedaco)==3:
                               nome,preco,quantidade=pedaco
                               nome=str(nome)
                               preco=float(preco)
                               quantidade=int(quantidade)
                               novo_produto=Produto(nome,preco,quantidade)
                               self.lista.append(novo_produto)
                               print("Produtos carregados com sucesso")
            
        except Exception as e:       
            print(e)
    def cadastrar_produto(self):
        nome=str(input("Digite o nome do produto: "))
        preco=float(input("Digite o preco do produto: "))
        quantidade=int(input("Digite a quantidade do produto: "))
        novo_produto=Produto(nome,preco,quantidade)
        self.lista.append(novo_produto)
        with open(self.arquivo,"a", encoding="utf-8")as arquivo:
            arquivo.write(f"{novo_produto.nome};{novo_produto.preco};{novo_produto.quantidade}\n")

        print("\nNovo produto cadastrado com sucesso\n")
        
    def listar_produto(self):
        if not self.lista:
            print("A lista está vazia")
            return
        for itens in self.lista:
            print(itens)
    def buscar_nome(self):
        if not self.lista:
            print("A lista está vazia")
            return
        nome=str(input("Digite o nome do produto que deseja procurar: ")).lower()
        encontrou=False
        for i in self.lista:
            if i.nome.lower()==nome:
                print(i)
                encontrou=True
        if encontrou==False:
            print("Item nao Encontrado!")



    def remover_item(self):
        if not self.lista:
            print("A lista está vazia")
        nome=str(input("Digite o item da lisat que deseja remover: ")).lower()
        encontrou=False
        for i in self.lista:
            if i.nome.lower()==nome:
                self.lista.remove(i)
                print(f"Item {i} removido com sucesso")
                if encontrou==True:
                    print("Item nao encontrado")



if __name__ == "__main__":
    controle = Controle()  # Instancia a classe de controle

    while True:
        opcao = input("""
        MENU CADASTRO
        1-Cadastrar Produto
        2-Listar Produto
        3-Buscar Produto pelo nome
        4-Remover Produto pelo nome
        0-Sair

        Escolha uma opcao: """)
        
        match opcao:
            case "1":
                controle.cadastrar_produto()
            case "2":
                controle.listar_produto()
            case "3":
                controle.buscar_nome()
            case "4":
                controle.remover_item()
            case "0":
                print("Saindo do sistema ")
                break
            case _:                                
                print("Opcao invalida!")
                       
