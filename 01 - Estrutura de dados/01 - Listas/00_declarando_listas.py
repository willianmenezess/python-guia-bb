# Os itens da lista são ordenados, alteráveis e permitem valores duplicados. Os itens da lista são 
# indexados, o primeiro item possui índice [0], o segundo item possui índice [1], etc. Quando dizemos 
# que as listas estão ordenadas, significa que os itens têm uma ordem definida, e essa ordem não 
# será alterada. Se você adicionar novos itens a uma lista, os novos itens serão colocados 
# no final da lista.

frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10)) # ou: numeros = list(range(0, 10))
print(numeros)

# Em python, listas podem conter diferentes tipos de dados:
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)
