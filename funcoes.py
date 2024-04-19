def cadastro():
    global usuarios,usuarioLogado,senhaLogado,dinheiro,limpar
    print("------- Inicialização de caixa -------")
    usuario = input("Digite o seu usuário: ")
    senha = input("Digite a sua senha: ")

    if usuario in usuarios and usuarios[usuario] == senha:
        usuarioLogado = usuario
        senhaLogado = senha
        dinheiro = float(input("Digite a quantidade de dinheiro disponível: "))
        print("-------- Caixa inicializado --------")
    else:
        print("⚠ Seu usuário ou senha estão errados")
    input("Digite qualquer tecla para voltar ao menu principal")
    limpar()


def Adicionar():
    global produtos
    print("------- Adicionar Produto -------")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    produtos[nome] = preco
    print("Produto: {} adicionado com sucesso".format(nome))

def Alterar():

    print("------- Alterar Produto -------")
    nome = input("Digite o nome do produto a ser alterado: ")
    if nome in produtos:
        novoPreco = float(input("Digite o novo preco para o produto"))
        produtos[nome] = novoPreco
        print("O preço do produto foi modificado para R${}".format(novoPreco))
    else:
        print("Produto não encontrado")
    
def excluir():
    print("------- Remover Produto -------")
    nome = input("Digite o nome do produto a ser removido: ")
    if nome in produtos:
        del produtos[nome]
        print("Produto {} removido com sucesso".format(nome))
    else:
        print("Produto {} não foi encontrado".format(nome))

def pesquisar():
    print("------- Pesquisar Produto -------")
    nome = input("Digite o nome do produto a ser pesquisado: ")
    if nome in produtos:
        print("Produto {}: R${}".format(nome,produtos[nome]))
    else:
        print("O produto {} não foi encontrado".format(nome))

def visualizar():
    if produtos:
        print(produtos)
    else:
        print("Nenhum produto cadastrado ainda")

def passar_comprar():
    if produtos:
        print("Produtos disponíveis para compra:")
        total = 0
        for produto in produtos:
            print("{}: R${:.2f}".format(produto, produtos[produto]))
            total += produtos[produto]
        print("Total da compra: R${:.2f}".format(total))



def bloquear_caixa():
    global bloqueado
    userADM = input("Digite o usuário administrador: ")
    senhaADM = input("Digite a senha do usuário administrador: ")
    if userADM == "adm" and senhaADM == "adm123":
        resposta = input("Tem certeza que deseja bloquear o caixa? (S/N): ")
        if resposta.upper() == "S":
            bloqueado = True
            print("Caixa bloqueado.")
        else:
            print("Operação cancelada.")
    else:
        print("Usuário administrador ou senha incorretos.")


def fechamento_relatorio():
    if produtos:
        dinheiro = sum(produtos.values())
        numero_vendas= len(produtos)
        print("Total de vendas no dia: {}".format(numero_vendas))
        print("Dinheiro arredado: {}".format(dinheiro))
    else:
        print("Nenhuma venda foi feita hoje")
