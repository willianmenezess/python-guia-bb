# Encapsulamento é o conceito de esconder os detalhes internos de uma classe, permitindo que os usuários 
# interajam com a classe apenas através de métodos públicos.
# Isso ajuda a proteger os dados e a manter a integridade do estado do objeto.
# Em Python, o encapsulamento é alcançado através do uso de atributos e métodos privados (prefixados com 
# um único ou duplo underscore) e propriedades (decoradores `@property`).

class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        # ...
        return self._saldo

if __name__ == "__main__":
    conta = Conta("0001", 100)
    conta.depositar(100)
    print(conta.nro_agencia)
    print(conta.mostrar_saldo())
