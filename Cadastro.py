import pandas as pd #A biblioteca "pandas" é um framework para manipular dados no ecxel
from colorama import init, Fore, Style #Importa funcionalidades do módulo colorama para adicionar cores e estilos


class Cadastro:
    def __init__(self):

        #Inicialização da classe com dicionários vazios para gastos fixos
        self.gastosFixos = {
            "Medicamentos"          : [ ],
            "Internet"              : [ ],
            "Streaming"             : [ ],
            "Aluguel"               : [ ],
            "Mensalidade acadêmica" : [ ],
            "Academia"              : [ ],
            "Seguro do carro"       : [ ]
        }
        
        #Inicialização da classe com dicionários vazios para gastos variáveis
        self.gastosVariaveis = {
            "Conta de Água"         : [ ],
            "Conta de Luz"          : [ ],
            "Supermercado"          : [ ],
            "Combustível"           : [ ],
            "Transporte"            : [ ],
            "Cuidados Pessoais"     : [ ],
            "Lazer"                 : [ ]
        }

        self.totalFixos = 0
        self.totalVariaveis = 0


    #Método para iniciar um novo cadastro com o nome e o número de pessoas na família
    def IniciarCadastro(self, nome, pessoasNaFamilia):
        
        self.nome = nome
        self.pessoasFamilia = pessoasNaFamilia


    #Método para salvar os dados do Cadastro em um arquivo Excel
    def salvarDados(self, jaTemCadastro = False, dadosSalvos = False):
        if (jaTemCadastro == True):
            contas = self.gastosFixos.copy()
            contas.update(self.gastosVariaveis)
            contas.update(dadosSalvos)
            
            dados = pd.DataFrame(data=contas, index=["Valor", "Frequencia", "Total"])
            dados.to_excel(f"./Cadastros/{self.nome}.xlsx")
        
        else:
            
            contas = self.gastosFixos.copy()
            contas.update(self.gastosVariaveis)

            dados = pd.DataFrame(data=contas, index=["Valor", "Frequencia", "Total"])  
            dados.to_excel(f"./Cadastros/{self.nome}.xlsx")


    #Método para exibir os valores dos Gastos Fixos
    def mostrarValores(self):
        print(Fore.GREEN + "\n                         |Exemplificação de gastos com Valores Fixos|         \n" + Style.RESET_ALL)
        contas = self.gastosFixos.copy()
        for conta in contas:
            print(f"{conta}: R$ {contas.get(conta)}")
        
        print(Fore.GREEN + "\n                       |Exemplificação de gastos com Valores Variáveis|         \n" + Style.RESET_ALL)
        contas = self.gastosVariaveis.copy()
        for conta in contas:
            print(f"{conta}: R$ {contas.get(conta)}")


    #Método para adicionar uma nova conta aos Gastos Fixos
    def adicionarValorFixo(self, conta, valor, frequencia):
        total = int(valor) * int(frequencia)
        self.gastosFixos.update({conta : [valor, frequencia, total]})
        
        return


    #Método para adicionar uma nova conta aos Gastos Variáveis
    def adicionarValorVariavel(self, conta, valor, frequencia):
        total = int(valor) * int(frequencia)
        self.gastosVariaveis.update({conta: [valor, frequencia, total]})


    #Método para remover uma contselfa dos Gastos Fixos
    def removerValor(self, conta):
        self.gastosFixos.pop(conta)
        self.gastosFixos.pop(conta)

        return


    #Método para alterar os valores das contas dos Gastos Fixos e Variáveis
    def alterarValores(self):
        print(Fore.GREEN + "\n                        |Confecção da Tabela|              " + Style.RESET_ALL)
        print(Fore.GREEN + "\n                      |Gastos com Valores Fixos|         \n" + Style.RESET_ALL)
        for conta in self.gastosFixos:
            valor = input(f"{conta} Valor: ")
            frequencia = input(f"{conta} Frequência: ")
            print("               ")
            
            total = int(valor) * int(frequencia)
            self.gastosFixos[conta] = [valor, frequencia, total]

        print(Fore.GREEN + "\n                    |Gastos com Valores Variáveis|         \n" + Style.RESET_ALL)
        for conta in self.gastosVariaveis:
            valor = input(f"{conta} Valor: ")
            frequencia = input(f"{conta} Frequência: ")
            print("               ")
            
            total = int(valor) * int(frequencia)
            self.gastosVariaveis[conta] = [valor, frequencia, total]
        
        dadosFixos = self.gastosFixos.values()
        dadosVariaveis = self.gastosVariaveis.values()

        gastosFixos = [x[2] for x in dadosFixos]
        gastosVariaveis = [x[2] for x in dadosVariaveis]


        total = 0


        for gasto in gastosFixos:
            total += gasto

        for gasto in gastosVariaveis:
            total += gasto


        print(Fore.BLUE + f"                  |O total de suas despesas no mês foi de R$ {total}|               " + Style.RESET_ALL)

        return
