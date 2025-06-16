# Escopo Local e Global
# Variáveis locais são aquelas definidas dentro de uma função e só podem ser acessadas dentro dessa função.
# Variáveis globais são aquelas definidas fora de qualquer função e podem ser acessadas por qualquer função no mesmo escopo.
# Variáveis globais podem ser modificadas dentro de uma função usando a palavra-chave `global`.

salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return print(salario)

if __name__ == "__main__":
    salario_bonus(500)  # 2500
