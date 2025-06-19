# Atributo de classe: um atributo que é compartilhado por todas as instâncias da classe.
# Atributo de instância: um atributo que é específico para cada instância da classe

class Estudante:
    escola = "DIO" # Atributo de classe

    def __init__(self, nome, matricula):
        self.nome = nome # Atributo de instância
        self.matricula = matricula # Atributo de instância

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

if __name__ == "__main__":
    # Exemplo de atributos de classe e instância
    aluno_1 = Estudante("Guilherme", 1)
    aluno_2 = Estudante("Giovanna", 2)
    mostrar_valores(aluno_1, aluno_2)
    # Modificando o atributo de classe
    Estudante.escola = "Python"
    aluno_3 = Estudante("Chappie", 3)
    mostrar_valores(aluno_1, aluno_2, aluno_3)
