#Importa a biblioteca "os" responsável por gerenciar arquivos
import os

#A biblioteca "pandas" é um framework para manipular dados no ecxel
import pandas as pd

#Importa a classe "Cadastro"
import Cadastro as Cdstr

#Variável para acessar a pasta onde esta guardado os cadastros
salvoCadastros = "./Cadastros"

#Inicialização do código
def main():

    print("\n𝐒𝐄𝐍𝐀𝐈 - 𝐆𝐄𝐑𝐄𝐍𝐂𝐈𝐀𝐌𝐄𝐍𝐓𝐎 𝐅𝐈𝐍𝐀𝐍𝐂𝐄𝐈𝐑𝐎 𝐃𝐎𝐌𝐄𝐒𝐓𝐈𝐂𝐎")
    print("""\nSeja bem-vindo(a) ao Syne, seu alido na Gestão Financeira Doméstica. 
Com nossa plataforma você adiministra seus gastos de forma ágil e 
eficiente, promovendo um controle financeiro mais econômico e consciente.""")

    #Variável para caso o usuário já tenha um cadastro efetuado
    conta = input("\nVocê possui cadastro nesse serviço? Caso sim insira o nome de ususário. Se não digite Não: ")
    if ( conta == "Não" ):
        novoCadastro()
    else:
        executarSessao(f"{conta}.xlsx")


#Inicia um novo cadastramento
def novoCadastro():
    cadastro = Cdstr.Cadastro()


    #Solicita e armazena o nome completo do usuário e o número de pessoas na família
    print("\n                                       |Cadatro do Usuário|")
    Nome = input("\nInsira seu nome de usuário: ")
    pessoasNaFamilia = input("Quantas pessoas compõe sua família: ")


    #Exibe os valores dos Gastos Fixos
    cadastro.mostrarValores()


    #Inicia o Cadastro do usuário com o nome e o número de pessoas na família
    cadastro.IniciarCadastro(Nome, pessoasNaFamilia)


    #Loop para adicionar novos gastos à tabela de Gastos
    while (input("\nDeseja adicionar um novo gasto fixo a tabela? Sim ou Não: ") == "Sim" ): 
        conta = input("Informe o tipo de gasto: ")
        valor = input("Informe o gasto dessa conta: ")
        frequencia = input("Quantas vezes esse gasto é efetuada ao mês: ")

        cadastro.adicionarValorFixo(conta, valor, frequencia)


    #Loop para adicionar um gasto variável à tabela de Gastos
    while (input("\nDeseja adicionar um novo gasto variável a tabela? Sim ou Não: ") == "Sim" ): 
        conta = input("Informe o tipo de gasto: ")
        valor = input("Informe o gasto médio dessa conta: ")
        frequencia = input("Quantas vezes essa conta acontece ao mês: ")

        cadastro.adicionarValorVariavel(conta, valor, frequencia)


    #Loop para remover valores da tabela de Gastos
    while (input("\nDeseja remover algum valor da tabela? Sim ou Não: ") == "Sim" ):
        conta = input("Informe a conta que deseja excluir: ")
        cadastro.removerValor(conta)


    #Altera os valores dos Gastos na Tabela
    cadastro.alterarValores()

    #Salva os dados cadastrados se o usuário desejar
    if (input("\nDeseja salvar os dados cadastrados? Sim ou Não: ") == "Sim"): 
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
