def cadastro():
     if (usuario1 == usuario and senha1 == senha) or (usuario2 == usuario and senha2 == senha):
        usuarioLogado = usuario
        senhaLogado = senha
        dinheiro = float(input("Digite a quantidade de dinheiro disponivel:"))
         print(" -------- Caixa inicializado -------- ")
     else:
         print("⚠ Seu usuário ou senha estão errados")
         opcao = input("Digite (V) para voltar")
     if opcao == "v" or opcao == "V":
        limpar()
        continue

def Adicionar():
    dicionario = {}
    produto = str(input("Qual produto deseja adicionar: "))
    preco = float(input("Digite o preço do produto: "))
    dicionario[produto] = preco
    print(dicionario)
def Alterar():
    dicionario = {}
    produto = str(input("Digite o produto que quer substituir o preço: "))
    novo = float(input("Digite o novo preço: "))
    dicionario[produto] = novo
    print(dicionario)
def excluir():
    dicionario = {}
    produto = str(input("Qual o produto que deseja excluir: "))
    del(dicionario[produto])
    print(dicionario)
