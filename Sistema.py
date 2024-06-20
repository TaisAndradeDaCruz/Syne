import os
import Usuario
import CaminhoPasta as Pasta

class Sistema:

    def __init__(self):
        
        return
    
    def Logar(self, Nome):
        nome = Nome.strip()

        usuario = Usuario.Usuario(nome)

        return usuario