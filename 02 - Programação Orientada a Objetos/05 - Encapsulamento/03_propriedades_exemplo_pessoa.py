class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property # Decorator para definir uma propriedade. É uma forma de encapsular o acesso ao atributo.
    def idade(self):
        _ano_atual = 2025
        return _ano_atual - self._ano_nascimento

if __name__ == "__main__":
    pessoa = Pessoa("Guilherme", 1994)
    print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
