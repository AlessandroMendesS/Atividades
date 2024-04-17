from os import system
from funcoes import *

#Professor, nota-se que na opção que o senhor pede para verificar a segurança,nao pede nenhuma senha ou algo do tipo para o bloqueio,por isso crie um usuario de adm e senha para que a pessoa que esta no caixa se sinta mais segura caso alguem mal intencionado tente fazer o bloqueio clicando apenas no "s".'''
usuarios = {"Alessandro":123,"Joana":"qwe","adm":123}

usuarioLogado = ""
senhaLogado = ""
dinheiro = 0
bloqueado = False

produtos = {}


def limpar():
    system("cls")

limpar()

while True:

    if bloqueado == True:
        print("### 🔐 Seu caixa está bloqueado ####")
        senha = input("digite a senha do usuário para desbloquear")
        if senha == senhaLogado:
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
            opcaoo = str(input("Qual opçaõ deseja? A-Adicionar,B-Alterar,C-Excluir,D-Visualizar e E-Pesquisar: ")).upper()
            if opcaoo == "A":
                Adicionar()
            elif opcaoo == "B":
                Alterar()
            elif opcaoo == "C":
                excluir()
            elif opcaoo == "D":
                pesquisar()
            elif opcaoo == "E":
                visualizar()

	  
        elif opcaoSelecionada == 3:
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
            
