import os #Importa a biblioteca "os" responsável por gerenciar arquivos
import pandas as pd #A biblioteca "pandas" é um framework para manipular dados no ecxel
import Cadastro as Cdstr #Importa a classe "Cadastro"
from colorama import init, Fore, Style #Importa funcionalidades do módulo colorama para adicionar cores e estilos
import time #Importa a biblioteca "time" na qual cria um atraso de tempo

salvoCadastros = "./Cadastros" #Variável para acessar a pasta onde esta guardado os cadastros

#Inicialização do código
def main(): 

    init()
    print(Fore.GREEN + "\n|Seja bem-vindo(a) ao Syne, seu alido na Gestão Financeira Doméstica.        |" + Style.RESET_ALL)
    print("|Com nossa plataforma você adiministra seus gastos de forma ágil e eficiente,|")
    print("|promovendo um controle financeiro mais econômico e consciente.              | ")

    #Variável para o cadastro do usuário
    conta = input("\nVocê possui cadastro nesse serviço? Caso não possua digite (N): ")
    novoCadastro()


#Inicia um novo cadastramento
def novoCadastro():
    cadastro = Cdstr.Cadastro()


    #Solicita e armazena o nome de usuário da pessoa
    print(Fore.GREEN + "\n                      |Cadastro do Usuário|" + Style.RESET_ALL)
    Nome = input("\nInsira seu nome de usuário: ")


    #Inicia o Cadastro do usuário com o nome
    cadastro.IniciarCadastro(Nome)


    #Exibe os valores dos Gastos Fixos
    time.sleep(0.9)
    cadastro.mostrarValoresFixos()


    time.sleep(1.3)
    print(Fore.GREEN + "\n                         |Alteração dos Dados|              " + Style.RESET_ALL)
    #Loop para adicionar novos gastos à tabela de Gastos Fixos
    while (input("\nDeseja adicionar um novo Gasto Fixo na tabela? Sim (S) ou Não (N): ") == "S" ): 
        conta = input("Informe o tipo de gasto: ")

        cadastro.adicionarValorFixo(conta)


    #Loop para remover valores da tabela de Gastos Fixos
    while (input("\nDeseja remover algum valor Fixo da tabela? Sim (S) ou Não (N): ") == "S" ): 
        conta = input("Informe a conta que deseja excluir: ")

        cadastro.removerValorFixo(conta)


    #Exibe os valores dos Gastos Variáveis
    time.sleep(0.9)
    cadastro.mostrarValoresVariaveis()

    time.sleep(1.3)
    print(Fore.GREEN + "\n                         |Alteração dos Dados|              " + Style.RESET_ALL)

    #Loop para adicionar um gasto variável à tabela de Gastos Variáveis
    while (input("\nDeseja adicionar um novo Gasto Variável na tabela? Sim (S) ou Não (N): ") == "S" ):  
        conta = input("Informe o tipo de gasto: ")

        cadastro.adicionarValorVariavel(conta)


    #Loop para remover valores da tabela de Gastos Variáveis
    while (input("\nDeseja remover algum valor Variável da tabela? Sim (S) ou Não (N): ") == "S" ): 
        conta = input("Informe a conta que deseja excluir: ")

        cadastro.removerValorVariavel(conta)


    #Altera os valores dos Gastos na Tabela
    cadastro.alterarValores()


    time.sleep(0.9)
    cadastro.salvarDados()


    #Salva os dados cadastrados se o usuário desejar
    if (input("\nDeseja salvar os dados cadastrados? Sim (S) ou Não (N): ") == "S" ): 
        cadastro.salvarDados(False)


#Roda o código
if __name__ == "__main__": 
    main()
