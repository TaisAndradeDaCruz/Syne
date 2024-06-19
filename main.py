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

    #Variável para caso o usuário já tenha um cadastro efetuado
    conta = input("\nVocê possui cadastro nesse serviço? Caso sim insira o nome de ususário. Se não digite (N): ")
    if ( conta == "N" ):
        novoCadastro()
    else:
        executarSessao(f"{conta}.xlsx")


#Inicia um novo cadastramento
def novoCadastro():
    cadastro = Cdstr.Cadastro()


    #Solicita e armazena o nome completo do usuário e o número de pessoas na família
    print(Fore.GREEN + "\n                                    |Cadastro do Usuário|" + Style.RESET_ALL)
    Nome = input("\nInsira seu nome de usuário: ")
    pessoasNaFamilia = input("Quantas pessoas compõe sua família: ")

    #Exibe os valores dos Gastos Fixos
    time.sleep(0.9)
    cadastro.mostrarValores()

    #Inicia o Cadastro do usuário com o nome e o número de pessoas na família
    cadastro.IniciarCadastro(Nome, pessoasNaFamilia)

    time.sleep(1.3)
    print(Fore.GREEN + "\n                         |Alteração dos Dados|              " + Style.RESET_ALL)

    #Loop para adicionar novos gastos à tabela de Gastos
    while (input("\nDeseja adicionar um novo Gasto Fixo a tabela? Sim (S) ou Não (N): ") == "S" ): 
        conta = input("Informe o tipo de gasto: ")
        valor = input("Informe o gasto dessa conta: ")
        frequencia = input("Quantas vezes esse gasto é efetuada ao mês: ")

        cadastro.adicionarValorFixo(conta, valor, frequencia)


    #Loop para adicionar um gasto variável à tabela de Gastos
    while (input("\nDeseja adicionar um novo Gasto Variável a tabela? Sim (S) ou Não (N): ") == "S" ):  
        conta = input("Informe o tipo de gasto: ")
        valor = input("Informe o gasto médio dessa conta: ")
        frequencia = input("Quantas vezes essa conta acontece ao mês: ")

        cadastro.adicionarValorVariavel(conta, valor, frequencia)


    #Loop para remover valores da tabela de Gastos
    while (input("\nDeseja remover algum valor da tabela? Sim (S) ou Não (N): ") == "S" ): 
        conta = input("Informe a conta que deseja excluir: ")

        cadastro.removerValor(conta)


    #Altera os valores dos Gastos na Tabela
    cadastro.alterarValores()


    #Salva os dados cadastrados se o usuário desejar
    if (input("\nDeseja salvar os dados cadastrados? Sim (S) ou Não (N): ") == "S" ): 
        cadastro.salvarDados(False)


#Exibir uma conta já existente
def executarSessao(arquivo):
    cadastro = Cdstr.Cadastro()
    
    dadosJaFeitos = pd.read_excel(f"{salvoCadastros}/{arquivo}", index_col=None)
    print(dadosJaFeitos)

    #Exibe os valores dos Gastos Fixos
    cadastro.mostrarValores()


#Roda o código
if __name__ == "__main__": 
    main()
