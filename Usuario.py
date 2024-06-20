import pandas as pd
import os
import CaminhoPasta as Pasta
from colorama import init, Fore, Style
import time

class Usuario:
    def __init__(self, Usuario):
        self.Usuario = Usuario

        if not os.path.exists(f"{Pasta.diretorio}/{self.Usuario}/"):
            os.mkdir(f"{Pasta.diretorio}/{self.Usuario}")

            self.TabelaFixos = {
                "Medicamentos":          {"Valor" : 0, "Frequência" : 0, "Total" : 0},
                "Internet":              {"Valor" : 0, "Frequência" : 0, "Total" : 0},
                "Streaming":             {"Valor" : 0, "Frequência" : 0, "Total" : 0},
                "Aluguel":               {"Valor" : 0, "Frequência" : 0, "Total" : 0},
                "Mensalidade Acadêmica": {"Valor" : 0, "Frequência" : 0, "Total" : 0},
                "Academia":              {"Valor" : 0, "Frequência" : 0, "Total" : 0},
                "Seguro do Carro":       {"Valor" : 0, "Frequência" : 0, "Total" : 0}
            }

            self.TabelaVariaveis = {
                "Conta de Luz" :      {"Valor" : 0, "Frequência" : 0, "Total" : 0}, 
                "Supermercado" :      {"Valor" : 0, "Frequência" : 0, "Total" : 0},
                "Combustível" :       {"Valor" : 0, "Frequência" : 0, "Total" : 0}, 
                "Transporte" :        {"Valor" : 0, "Frequência" : 0, "Total" : 0},
                "Cuidados Pessoais" : {"Valor" : 0, "Frequência" : 0, "Total" : 0},
                "Lazer" :             {"Valor" : 0, "Frequência" : 0, "Total" : 0}
            }

            open(f"{Pasta.diretorio}/{self.Usuario}/Fixos.xlsx", 'a')
            open(f"{Pasta.diretorio}/{self.Usuario}/Variaveis.xlsx", 'a')

            self.caminhoTabelaFixos = f"{Pasta.diretorio}/{self.Usuario}/Fixos.xlsx"
            self.caminhoTabelaVariaveis = f"{Pasta.diretorio}/{self.Usuario}/Variaveis.xlsx"

            self.salvarDados()
            
            return

        self.caminhoTabelaFixos = f"{Pasta.diretorio}/{self.Usuario}/Fixos.xlsx"
        self.caminhoTabelaVariaveis = f"{Pasta.diretorio}/{self.Usuario}/Variaveis.xlsx"
        
        
        self.TabelaFixos = pd.read_excel(self.caminhoTabelaFixos, engine="openpyxl").to_dict(index=["Valor", "Frequência", "Total"])
        self.TabelaVariaveis = pd.read_excel(self.caminhoTabelaVariaveis, engine="openpyxl").to_dict(index=["Valor", "Frequência", "Total"])

        return


    def VerMinhasContasFixas(self):
        time.sleep(0.9)
        print(Fore.GREEN + "\n                         |Exemplificação de gastos com Valores Fixos|         \n" + Style.RESET_ALL)
        
        print(self.TabelaFixos)
        
        for conta in self.TabelaFixos:
            print(f"{conta}: R$ {conta[0]}, {conta[1]} ao mês")


    def VerMinhasContasVariaveis(self):
        time.sleep(0.9)
        print(Fore.GREEN + "\n           |Exemplificação de gastos com Valores Variáveis|         \n" + Style.RESET_ALL)
        
        for conta in self.TabelaVariaveis:
            print(f"{conta}: R$ {conta[0]}, {conta[1]} ao mês")



    def EditarGastos(self, tipoGasto):
        if (tipoGasto == 'fixo'):
            for conta, dados in self.TabelaFixos.items():
                valor = input(f"Insira o valor de {conta}: ")
                frequencia = input(f"Insira a frequencia de {conta}: ")

                self.TabelaFixos[conta] = {"Valor" : valor, "Frequencia" : frequencia, "Total" : int(valor) * int(frequencia)}
            
            return

        for conta, dados in self.TabelaVariaveis.items():
            valor = input(f"Insira o valor de {conta}: ")
            frequencia = input(f"Insira a frequencia de {conta}: ")

            self.TabelaVariaveis[conta] = {"Valor" : valor, "Frequencia" : frequencia, "Total" : int(valor) * int(frequencia)}

        return

    def AdicionarGasto(self, tipoGasto, gasto, valor, frequencia):
        
        if (tipoGasto == "fixo"):
            self.TabelaFixos[gasto] = {"Valor" : valor, "Frequencia" : frequencia, "Total" : int(valor) * int(frequencia)}
            return

        self.TabelaVariaveis[gasto] = {"Valor" : valor, "Frequencia" : frequencia, "Total" : int(valor) * int(frequencia)}
        return


    def RemoverGasto(self, tipoGasto, gasto):
        if (tipoGasto == 'fixo'):
            self.TabelaFixos.pop(gasto)
            return
        
        self.TabelaVariaveis.pop(gasto)



    def salvarDados(self):

        tabelaFixos = pd.DataFrame(self.TabelaFixos)
        tabelaVariaveis = pd.DataFrame(self.TabelaVariaveis)
        
        tabelaFixos.to_excel(self.caminhoTabelaFixos, index=["Valor", "Frequência", "Total"])
        tabelaVariaveis.to_excel(self.caminhoTabelaVariaveis, index=["Valor", "Frequência", "Total"])
        