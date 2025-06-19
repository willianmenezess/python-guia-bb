# Polimorfismo é a capacidade de diferentes classes responderem ao mesmo método de forma diferente.
# É um conceito fundamental na programação orientada a objetos que permite que objetos de diferentes 
# classes sejam tratados como objetos de uma classe comum, desde que implementem o mesmo método.

class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


# NOTE: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")


def plano_voo(obj):
    obj.voar()

if __name__ == "__main__":
    # Exemplo de polimorfismo
    plano_voo(Pardal())
    plano_voo(Avestruz())
    plano_voo(Aviao())
