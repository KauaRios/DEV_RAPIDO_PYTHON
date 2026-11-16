class Produto:
    def __init__(self,nome:str,preco:float,quantidade:int) -> None:
        self.nome=nome
        self.preco=preco
        self.quantidade=quantidade
        

    def valor_total(self):
        valor=self.preco*self.quantidade
        return valor 
    
    def exibir(self,valor):
        print(f"Produto:{self.nome} Preco:{self.preco} quantidade: {self.quantidade} ValorTotal:{valor}")
        


if __name__ =="__main__":
    Produto1=Produto("Teclado",195,2)   
    Produto2=Produto("Mesa",1200,3)
    valor1=Produto1.valor_total()
    valor2=Produto2.valor_total()
    
    Produto1.exibir(valor1)
    Produto2.exibir(valor2)


    
