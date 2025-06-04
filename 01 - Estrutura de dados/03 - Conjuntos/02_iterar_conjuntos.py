# Para iterar sobre um conjunto, podemos usar um loop for
# ou a função enumerate para obter o índice (variável) e o valor do elemento.

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
