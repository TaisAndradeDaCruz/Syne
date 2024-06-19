import Sistema as sistema


def main():
    Sistema = sistema.Sistema()


    usuario = input("Bem vindo ao Syne! Insira seu nome aqui: ")

    usuario = Sistema.Logar(usuario)




if __name__ == "__main__":
    main()