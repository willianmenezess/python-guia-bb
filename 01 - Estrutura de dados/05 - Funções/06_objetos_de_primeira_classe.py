# Funções são objetos de primeira classe, ou seja, podem ser passadas como argumentos para outras funções
# e também podem ser retornadas por outras funções.

def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

if __name__ == "__main__":
    exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
