from os import system
from funcoes import *


produtos = {}


#Professor, nota-se que na opção que o senhor pede para verificar a segurança,nao pede nenhuma senha ou algo do tipo para o bloqueio,por isso crie um usuario de adm e senha para que a pessoa que esta no caixa se sinta mais segura caso alguem mal intencionado tente fazer o bloqueio clicando apenas no "s".'''
usuarios = {"Alessandro":"123","Joana":"qwe"}

usuarioLogado = None
senhaLogado = None
dinheiro = 0
bloqueado = False


def limpar():
    system("cls")

limpar()

while True:
    if bloqueado:
        print("### 🔐 Seu caixa está bloqueado ####")
        senha = input("Digite a senha do usuário para desbloquear: ")
        if senha == "123":
            bloqueado = False
    else:
        print('✅1 - Inicializar caixa')
        print("🍎 2 - Gerenciar Produtos")
        print("💰 3 - Passar Compras")
        print("❌ 4 - Bloqueio de Caixa")
        print("🔐 5 - Fechar Caixa")
        print("🔴 6 - Sair do Sistema")

        opcaoSelecionada = int(input("Qual é sua escolha:"))

        if opcaoSelecionada == 1:
            cadastro()
        elif opcaoSelecionada == 2:
            print("------- Gerenciar Produtos -------")
            print("A-Adicionar")
            print("B-Alterar")
            print("C-Excluir")
            print("D-Visualizar")
            print("E-Pesquisar")
            opcaoo = str(input("Digite a opcao desejavel: "))
            if opcaoo.upper() == "A":
                Adicionar()
            elif opcaoo.upper() == "B":
                Alterar()
            elif opcaoo.upper() == "C":
                excluir()
            elif opcaoo.upper() == "D":
                visualizar()
            elif opcaoo.upper() == "E":
                pesquisar()
            else:
                print("Opção inválida.")
        elif opcaoSelecionada == 3:
            if not produtos:
                print("Não há produtos disponíveis para compra.")
                continue
            print("------- Passar Compras -------")
            passar_comprar()
        elif opcaoSelecionada == 4:
            print("------- Bloqueio do caixa -------")
            bloquear_caixa()
        elif opcaoSelecionada == 5:
            print("------- Fechar caixa ------")
            fechamento_relatorio()
        elif opcaoSelecionada == 6:
            print("------- Saindo do sistema de mercado ------")
            exit()
        else:
            print("Atenção❗: você digitou uma opção inválida ")
