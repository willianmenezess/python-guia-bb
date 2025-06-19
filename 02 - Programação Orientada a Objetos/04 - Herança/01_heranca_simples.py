# Herança é um conceito fundamental da Programação Orientada a Objetos (POO) que permite que uma classe herde atributos e métodos de outra classe.
# Isso promove a reutilização de código e a criação de hierarquias de classes.
# Em Python, a herança é implementada através da definição de uma classe filha que estende uma classe pai.
# A classe filha herda todos os atributos e métodos da classe pai,
# e pode adicionar novos atributos e métodos ou sobrescrever os existentes.
# Herança simples é quando uma classe herda de apenas uma classe pai.

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo): # Python nao usa a palavra-chave "extends" para herança
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas) # O super() chama o construtor da classe pai
        self.carregado = carregado

    def esta_carregado(self):
        return f"{'Sim' if self.carregado else 'Não'} estou carregado"

if __name__ == "__main__":
    moto = Motocicleta("preta", "abc-1234", 2)
    carro = Carro("branco", "xde-0098", 4)
    caminhao = Caminhao("roxo", "gfd-8712", 8, True)

    print(moto)
    print(carro)
    print(caminhao)
    print(caminhao.esta_carregado())