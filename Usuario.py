import pandas as pd
import os
import CaminhoPasta as Pasta

class Usuario:
    def __init__(self, Usuario):
        self.Usuario = Usuario.split()

        if not os.path.exists(f"{Pasta.diretorio}/Nome"):
            self.TabelaFixos = pd.DataFrame({
                "Água": [0, 0, 0],
                "Luz": [0, 0, 0],
            }, index=["Valor", "Frequencia", "Total"])

            self.TabelaVariaveis = pd.DataFrame({
                "Medicametos" : [0, 0, 0],
                "Pedro pedro pedro pedro pe" : [0, 0, 0] 
            }, index=["Valor", "Frequencia", "Total"])
            os.mkdir(f"{Pasta.diretorio}/{self.Usuario}")

            self.caminhoTabelaFixos = os.open(f"{Pasta.diretorio}/{self.Usuario}/Fixos.xlsx", 'w')
            self.caminhoTabelaVariaveis = os.open(f"{Pasta.diretorio}/{self.Usuario}/Variaveis.xlsx", 'w')

            self.TabelaFixos.to_excel(self.caminhoTabelaFixos)
            self.TabelaVariaveis.to_excel(self.caminhoTabelaVariaveis)
            
            return

        self.caminhoTabelaFixos = f"{Pasta.diretorio}/{self.Usuario}/Fixos.xlsx"
        self.caminhoTabelaVariaveis = f"{Pasta.diretorio}/{self.Usuario}/Variaveis.xlsx"
        
        
        self.TabelaFixos = pd.read_excel(self.caminhoTabelaFixos)
        self.TabelaVariaveis = pd.read_excel(self.caminhoTabelaVariaveis)

        return



    def VerMinhasContas(self):
        print(self.TabelaFixos)
        print(self.TabelaVariaveis)



    def EditarGasto(self, tipoGasto, gasto):
        conta = pd.DataFrame(gasto, index=["Valor", "Frequencia", "Total"])
        
        if (tipoGasto == "Fixo"):
            self.caminhoTabelaFixos.loc[:, gasto.keys()[0]] = conta

            return


        self.caminhoTabelaVariaveis.loc[:, gasto.keys()[0]] = conta

        return



    def AdicionarGastos(self, tipoGasto, gasto):
        conta = pd.DataFrame(gasto)

        if (tipoGasto == "fixo"):
            pd.merge(self.TabelaFixos, conta, on='key', how='inner')
            return


        pd.merge(self.TabelaVariaveis, conta, on='key', how='inner')



    def RemoverGastos(self, tipoGasto, gasto):
        if (tipoGasto == 'fixo'):
            self.TabelaFixos.drop(gasto, axis=1, inplace=True)
            return
        
        self.TabelaVariaveis.drop(gasto, axis=1, inplace=True)



    def salvarDados(self):

        self.TabelaFixos.to_excel(self.caminhoTabelaFixos)
        self.TabelaVariaveis.to_excel(self.caminhoTabelaVariaveis)