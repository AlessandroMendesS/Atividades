from os import system
from funcoes import *


## TODO: trocar esse sistema de autenticação por dicionários
usuario1 = "vini"
usuario2 = "jonas"
senha1 = "123"
senha2 = "qwe"

dicionario = {"Alessandro":"123","Joana":"qwe"}

## TODO: trocar por dicionários também
usuarioLogado = ""
senhaLogado = ""
dinheiro = 0
bloqueado = False

dicionario2 = {"":"","dinheiro":0,"bloqueado":False}



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
 	    ## TODO: fazer uso de funções para isolar essa funcionalidade em um bloco de código separado
	    ## TODO: refatorar esse código para que ele valide usuario e senha com base no dicionário criado

    

        
        elif opcaoSelecionada == 2:
            print("------- Gerenciar Produtos -------")
            opcaoo = int(input("Qual opçaõ deseja? A-Adicionar,B-Alterar,C-Excluir,D-Visualizar e E-Pesquisar: "))
            if opcaoo == "A":
                Adicionar()
            if opcaoo == "B":
                Alterar()
            if opcaoo == "C":
                

	    ## TODO: criar uma forma de adicionar, alterar, excluir, visualizar e pesquisar produtos do mercado (use listas ou dicionarios)

        elif opcaoSelecionada == 3:
            print("------- Passar Compras -------")
	    ## TODO: criar uma forma de "passar as compras" dos clientes e registrar essas compras. Lembre-se que ao final você precisará exibir um relatório do dia.
	    ## TODO: aqui é importante validar, se não houver produtos, não é possível passar compras.
            ## TODO: encontrar outras validações que fazem sentido!


        elif opcaoSelecionada == 4:
	    ## TODO: eu acho que aqui temos um problema de segurança, verificar
            print("------- Bloqueio do caixa -------")
            resposta = input("Tem certeza que deseja bloquear o caixa? (S/N)")
            if resposta == "S" or resposta == "s":
                bloqueado = True
                limpar()

        elif opcaoSelecionada == 5:
            print("------- Fechar caixa ------")
	    ## TODO: criar essa lógica: ao acionar o fechar caixa, deve-se exibir um relatório completo contendo
	    ###      - O total de vendas do dia; total de dinheiro arrecadado; 
	    ###      - O débito e o crédito devem devem se anular.

        elif opcaoSelecionada == 6:
            print("------- Saindo do sistema de mercado ------")
            exit()
        else:
            print("Atenção❗: você digitou uma opção inválida ")
