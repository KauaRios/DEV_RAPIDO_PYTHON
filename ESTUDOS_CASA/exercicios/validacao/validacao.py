def pedir_dados():
    while True:
        nome=str(input("Digite seu nome: ")).strip()
        if nome:
            break
        print("Nome vazio!")
    while True:
        try:
            preco=float(input("Digite o preco: "))
            if preco < 0:
                print(f"Não é permitido valores negativos: {preco}")
            else:
                print(f"valor:{preco} salvo com sucesso")
                break
        except ValueError:
            print("Digite um numero!")
    while True:
        try:
            quantidade=int(input("Digite a quantidade: "))
            if quantidade < 0:
                print(f"Não é permitido valores negativos:{quantidade}" )
            else:
                print(f"quantidade:{quantidade}salva com sucesso")
                break
        except ValueError:
            print("Digite um numero!")




if __name__ =="__main__":
    pedir_dados()
