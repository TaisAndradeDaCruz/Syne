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

    #Inicia o Cadastro do usuário com o nome e o número de pessoas na família
    cadastro.IniciarCadastro(Nome, pessoasNaFamilia)

    #Exibe os valores dos Gastos Fixos
    time.sleep(0.9)
    cadastro.mostrarValoresFixos()

    time.sleep(1.3)
    print(Fore.GREEN + "\n                         |Alteração dos Dados|              " + Style.RESET_ALL)
    #Loop para adicionar novos gastos à tabela de Gastos
    while (input("\nDeseja adicionar um novo Gasto Fixo na tabela? Sim (S) ou Não (N): ") == "S" ): 
        conta = input("Informe o tipo de gasto: ")

        cadastro.adicionarValorFixo(conta)

    #Loop para remover valores da tabela de Gastos
    while (input("\nDeseja remover algum valor Fixo da tabela? Sim (S) ou Não (N): ") == "S" ): 
        conta = input("Informe a conta que deseja excluir: ")

        cadastro.removerValorFixo(conta)

    #Exibe os valores dos Gastos Fixos
    time.sleep(0.9)
    cadastro.mostrarValoresVariaveis()

    time.sleep(1.3)
    print(Fore.GREEN + "\n                         |Alteração dos Dados|              " + Style.RESET_ALL)

    #Loop para adicionar um gasto variável à tabela de Gastos
    while (input("\nDeseja adicionar um novo Gasto Variável na tabela? Sim (S) ou Não (N): ") == "S" ):  
        conta = input("Informe o tipo de gasto: ")

        cadastro.adicionarValorVariavel(conta)

    while (input("\nDeseja remover algum valor Variável da tabela? Sim (S) ou Não (N): ") == "S" ): 
        conta = input("Informe a conta que deseja excluir: ")

        cadastro.removerValorVariavel(conta)

    #Altera os valores dos Gastos na Tabela
    cadastro.alterarValores()


    #Exibe os valores dos Gastos Fixos
    time.sleep(0.9)
    cadastro.salvarDados()

    #Salva os dados cadastrados se o usuário desejar
    if (input("\nDeseja salvar os dados cadastrados? Sim (S) ou Não (N): ") == "S" ): 
        cadastro.salvarDados(False)


# Exibir uma conta já existente
def executarSessao(arquivo):
    cadastro = Cdstr.Cadastro()

    if os.path.exists(f"{salvoCadastros}/{arquivo}"):
        dadosJaFeitos = pd.read_excel(f"{salvoCadastros}/{arquivo}", index_col=None)
        print(dadosJaFeitos)

        modificarGastosFixos(cadastro, "fixo")
        modificarGastosVaria(cadastro, "variável")

        cadastro.alterarValores()
        cadastro.salvarDados(jaTemCadastro=True)
    

#Roda o código
if __name__ == "__main__": 
    main()
