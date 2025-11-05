#codigo python que verifica se um nome é SENAC
nome=input("Qual o seu nome")
sobrenome=input("Digite o sobrenome")
nome=nome.upper()
if (nome == "SENAC" and sobrenome=="SANTA LUZIA"):
    print(f"seja bem vindo {nome}")
else:
    print("não é senac")    