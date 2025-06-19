# Metodo de classe: um método que é chamado na classe e não em uma instância.
# Ele pode acessar e modificar o estado da classe, mas não o estado de instâncias específicas.

# Metodo estático: um método que não recebe a instância ou a classe como primeiro argumento
# Ele não pode acessar ou modificar o estado da classe ou de instâncias específicas
# Ele é usado para definir funções que não dependem do estado da classe ou de instâncias

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome): # cls é a classe que está chamando o método
        idade = 2025 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

if __name__ == "__main__":
    p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme") # p é uma instância de Pessoa
    print(p.nome, p.idade)
    print(Pessoa.e_maior_idade(18))
    print(Pessoa.e_maior_idade(8))
