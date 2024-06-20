import pandas as pd #A biblioteca "pandas" é um framework para manipular dados no ecxel
from colorama import init, Fore, Style #Importa funcionalidades do módulo colorama para adicionar cores e estilos


class Cadastro:
    def __init__(self):

        #Inicialização da classe com dicionários vazios para Gastos Fixos
        self.gastosFixos = {
            "Medicamentos"          : [ ],
            "Internet"              : [ ],
            "Streaming"             : [ ],
            "Aluguel"               : [ ],
            "Mensalidade Acadêmica" : [ ],
            "Academia"              : [ ],
            "Seguro do Carro"       : [ ]
        }
        
        #Inicialização da classe com dicionários vazios para Gastos Variáveis
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


    #Método para iniciar um novo cadastro
    def IniciarCadastro(self, nome):
        
        self.nome = nome



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
    def mostrarValoresFixos(self):
        print(Fore.GREEN + "\n                         |Exemplificação de gastos com Valores Fixos|         \n" + Style.RESET_ALL)
        contas = self.gastosFixos.copy()
        for conta in contas:
            print(f"{conta}: R$ {contas.get(conta)}")


    #Método para exibir os valores dos Gastos Variáveis    
    def mostrarValoresVariaveis(self):
        print(Fore.GREEN + "\n           |Exemplificação de gastos com Valores Variáveis|         \n" + Style.RESET_ALL)
        contas = self.gastosVariaveis.copy()
        for conta in contas:
            print(f"{conta}: R$ {contas.get(conta)}")


    #Método para adicionar uma nova conta aos Gastos Fixos
    def adicionarValorFixo(self, conta):
        if conta not in self.gastosFixos:
            self.gastosFixos[conta] = []
        
        return


    #Método para adicionar uma nova conta aos Gastos Variáveis
    def adicionarValorVariavel(self, conta):
        if conta not in self.gastosVariaveis:
            self.gastosVariaveis[conta] = []
        
        return


    #Método para remover uma conta dos Gastos Fixos
    def removerValorFixo(self, conta):
        self.gastosFixos.pop(conta)

        return
    

    #Método para remover uma conta dos Gastos Variáveis
    def removerValorVariavel(self, conta):
        self.gastosVariaveis.pop(conta)

        return


    #Método para alterar os valores das contas dos Gastos Fixos e Variáveis
    def alterarValores(self):
        print(Fore.GREEN + "\n                        |Confecção da Tabela|              " + Style.RESET_ALL)
        print(Fore.GREEN + "\n                      |Gastos com Valores Fixos|         \n" + Style.RESET_ALL)
        for conta in self.gastosFixos:
            valor = input(f"{conta} | Valor: ")
            frequencia = input(f"{conta} | Frequência: ")
            print("               ")
            
            total = int(valor) * int(frequencia)
            self.gastosFixos[conta] = [valor, frequencia, total]

        print(Fore.GREEN + "\n                        |Confecção da Tabela|              " + Style.RESET_ALL)
        print(Fore.GREEN + "\n                    |Gastos com Valores Variáveis|         \n" + Style.RESET_ALL)
        for conta in self.gastosVariaveis:
            valor = input(f"{conta} | Valor: ")
            frequencia = input(f"{conta} | Frequência: ")
            print("               ")
            
            total = int(valor) * int(frequencia)
            self.gastosVariaveis[conta] = [valor, frequencia, total]

        dadosFixos = self.gastosFixos.values()
        dadosVariaveis = self.gastosVariaveis.values()

        gastosVariaveis = [x[2] for x in dadosVariaveis]
        gastosFixos = [x[2] for x in dadosFixos]


        total = 0


        for gasto in gastosFixos:
            total += gasto

        for gasto in gastosVariaveis:
            total += gasto


        #Exibe o total da despesa do usuário
        print(Fore.BLUE + f"   |O total de suas despesas no mês foi de R$ {total}|               " + Style.RESET_ALL)

        return
