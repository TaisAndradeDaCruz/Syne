#A biblioteca "pandas" é um framework para manipular dados no ecxel
import pandas as pd


class Cadastro:
    def __init__(this):

        #Inicialização da classe com dicionários vazios para gastos fixos
        this.gastosFixos = {
            "Medicamentos"          : [ ],
            "Internet"              : [ ],
            "Streaming"             : [ ],
            "Aluguel"               : [ ],
            "Mensalidade acadêmica" : [ ],
            "Academia"              : [ ],
            "Seguro do carro"       : [ ]
        }
        
        #Inicialização da classe com dicionários vazios para gastos variáveis
        this.gastosVariaveis = {
            "Conta de Água"         : [ ],
            "Conta de Luz"          : [ ],
            "Supermercado"          : [ ],
            "Combustível"           : [ ],
            "Transporte"            : [ ],
            "Cuidados Pessoais"     : [ ],
            "Lazer"                 : [ ]
        }

        this.totalFixos = 0
        this.totalVariaveis = 0

    #Método para iniciar um novo cadastro com o nome e o número de pessoas na família
    def IniciarCadastro(this, nome, pessoasNaFamilia):
        
        this.nome = nome
        this.pessoasFamilia = pessoasNaFamilia


    #Método para salvar os dados do Cadastro em um arquivo Excel
    def salvarDados(this, jaTemCadastro = False, dadosSalvos = False):
        if (jaTemCadastro == True):
            contas = this.gastosFixos.copy()
            contas.update(this.gastosVariaveis)
            contas.update(dadosSalvos)
            
            dados = pd.DataFrame(data=contas, index=["Valor", "Frequencia", "Total"])
            
            dados.to_excel(f"./Cadastros/{this.nome}.xlsx")
        
        
        
        else:
            
            
            contas = this.gastosFixos.copy()
            contas.update(this.gastosVariaveis)


            dados = pd.DataFrame(data=contas, index=["Valor", "Frequencia", "Total"])  


            dados.to_excel(f"./Cadastros/{this.nome}.xlsx")


    #Método para exibir os valores dos Gastos Fixos
    def mostrarValores(this):
        print ("\n          |Exemplificação de gastos com valores fixos|         \n")
        contas = this.gastosFixos.copy()
        for conta in contas:
            print(f"{conta}: R$ {contas.get(conta)}")


    #Método para adicionar uma nova conta aos Gastos Fixos
    def adicionarValorFixo(this, conta, valor, frequencia):
        total = int(valor) * int(frequencia)
        this.gastosFixos.update({conta : [valor, frequencia, total]})
        
        return
    

    #Método para adicionar uma nova conta aos Gastos Variáveis
    def adicionarValorVariavel(this, conta, valor, frequencia):
        total = int(valor) * int(frequencia)
        this.gastosVariaveis.update({conta: [valor, frequencia, total]})


    #Método para remover uma conta dos Gastos Fixos
    def removerValor(this, conta):
        this.gastosFixos.pop(conta)

        return

    #Método para alterar os valores das contas dos Gastos Fixos
    def alterarValores(this):
        print("\n                 |Confecção da Tabela|              \n")
        for conta in this.gastosFixos:
            valor = input(f"{conta} Valor: ")
            frequencia = input(f"{conta} Frequência: ")
            
            total = int(valor) * int(frequencia)
            this.gastosFixos[conta] = [valor, frequencia, total]


        for conta in this.gastosVariaveis:
            valor = input(f"{conta} Valor: ")
            frequencia = input(f"{conta} Frequência: ")
            
            total = int(valor) * int(frequencia)
            this.gastosVariaveis[conta] = [valor, frequencia, total]
        
        dadosFixos = this.gastosFixos.values()
        dadosVariaveis = this.gastosVariaveis.values()

        gastosFixos = [x[2] for x in dadosFixos]
        gastosVariaveis = [x[2] for x in dadosVariaveis]


        total = 0

        for gasto in gastosFixos:
            total += gasto

        for gasto in gastosVariaveis:
            total += gasto

        print(f"O total de suas contas no mês foi de R$ {total}")


        return
