# Classe Abstrata: uma classe que não pode ser instanciada diretamente.
# Ela serve como um modelo para outras classes, definindo métodos e propriedades que devem ser implementadas pelas subclasses.
# Classes Abstratas são usadas para definir uma interface comum para um grupo de classes relacionadas.

from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC): # ABC é a classe base abstrata
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property # Decorator para definir uma propriedade abstrata
    @abstractproperty # Caiu em desuso, use @property e @abstractmethod
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"

if __name__ == "__main__":
    controle = ControleTV()
    controle.ligar()
    controle.desligar()
    print(controle.marca)

    controle = ControleArCondicionado()
    controle.ligar()
    controle.desligar()
    print(controle.marca)
