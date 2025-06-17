class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    # Essa função é chamada quando a instância da classe é destruída
    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("auau")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)

if __name__ == "__main__":
    c = Cachorro("Chappie", "amarelo")
    c.falar()

    print("Ola mundo")

    del c

    print("Ola mundo")
    print("Ola mundo")
    print("Ola mundo")

    criar_cachorro()
