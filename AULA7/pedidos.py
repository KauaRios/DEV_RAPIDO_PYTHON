from pathlib import Path



class Pedido:
    def __init__(self:object,codigo:int,cliente:str,produto:str,email:str,quantidade:int,preco_unit:float,quantidade:int):
        self.codigo=codigo
        self.cliente=cliente
        self.produto=produto
        self.email=email
        self.quantidade=quantidade
        self.preco_unit=preco_unit

    def converter_txt(self):
        return f"{self.codigo};{self.cliente};{self.email};{self.produto},{self.quantidade},{self.preco_unit}"
    
    def calc_total(self):
        total=self.quantidade*self.preco_unit
        return total
    
    
class ImportadorPedidos:
    def __init__(self):
        self.dicionario={}
        base_dir = Path(__file__).parent
        self.arquivo1=base_dir/"pedidos.txt"
        self.arquivo2=base_dir/"pedidos_validos.json"
        self.arquivo3=base_dir/"erros.log"
        self.arquivo4=base_dir/"resumo.txt" ##Gera um resumo com quantidades de registros válidos, inválidos e valor total.
        self.carregar_txt()
        
        
        
    def processar_pedidos(self):
        if not self.arquivo1.exists():
            print("O arquivo nao existe!")
        else:
            try:
                with open(self.arquivo1,"r",encoding="utf-8")as a1:
                    for linha in a1:
                        linha=linha.strip().lower() 
                        if ";"in linha:
                            pedaco=linha.split(";")
                            if len(pedaco)==6:
                                codigo,cliente,email,produto,quantidade,preco_unit=pedaco
                                objs=Pedidos(codigo,cliente,email,produto,quantidade,preco_unit)
                                quantidade=int(valor)
                                preco=float(valor)
                                self.dicionario[codigo]=objs                         
            
        
        
        
   