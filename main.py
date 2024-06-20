import Sistema as sistema
import time
from colorama import init, Fore, Style

def main():
    Sistema = sistema.Sistema()

    init()
    print(Fore.GREEN + "\n|Seja bem-vindo(a) ao Syne, seu alido na Gestão Financeira Doméstica.        |" + Style.RESET_ALL)
    print("|Com nossa plataforma você adiministra seus gastos de forma ágil e eficiente,|")
    print("|promovendo um controle financeiro mais econômico e consciente.              | ")

    usuario = input("\nInforme seu nome de usuário cadastrado ou se cadastre agora: ")
    
    usuario = Sistema.Logar(usuario)

    time.sleep(0.9)
    usuario.VerMinhasContasFixas()


    time.sleep(1.3)
    print(Fore.GREEN + "\n                         |Alteração dos Dados|              " + Style.RESET_ALL)


    while (input("\nDeseja adicionar um novo Gasto Fixo na tabela? Sim (S) ou Não (N): ") == "S" ):  
        gasto = input("Informe o tipo do gasto: ")
        valor = input("Informe o valor de gasto: ")
        frequencia = input("Informe a frequência ao mês desse gasto: ")

        usuario.AdicionarGasto("fixo", gasto, valor, frequencia)

    while (input("\nDeseja remover algum valor Fixo da tabela? Sim (S) ou Não (N): ") == "S" ):   
        gasto = input("Informe o tipo do gasto: ")

        usuario.RemoverGasto("fixo", gasto)

    time.sleep(0.9)
    usuario.VerMinhasContasVariaveis()


    time.sleep(1.3)
    print(Fore.GREEN + "\n                         |Alteração dos Dados|              " + Style.RESET_ALL)


    while (input("\nDeseja adicionar um novo Gasto Variável na tabela? Sim (S) ou Não (N): ") == "S" ):  
        gasto = input("Informe o tipo de gasto: ")
        valor = input("Informe o valor de gasto: ")
        frequencia = input("Informe a frequência ao mês desse gasto: ")

        usuario.AdicionarGasto("variavel", gasto, valor, frequencia)


    while (input("\nDeseja remover algum valor Variável da tabela? Sim (S) ou Não (N): ") == "S" ):   
        gasto = input("Informe o tipo do gasto: ")

        usuario.RemoverGasto("variavel", gasto)


    if (input(Fore.BLUE + f"\n             |Gostaria de mudar algum valor determinado?|" + Style.RESET_ALL) == "S"):
        
        usuario.EditarGastos('fixo')


    usuario.salvarDados()


if __name__ == "__main__":
    main()