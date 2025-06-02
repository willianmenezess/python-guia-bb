carros = ["gol", "celta", "palio"]

for carro in carros: # percorre cada elemento da lista carros
    print(carro)


for indice, carro in enumerate(carros): # enumerate adiciona o índice de cada elemento
    print(f"{indice}: {carro}")
