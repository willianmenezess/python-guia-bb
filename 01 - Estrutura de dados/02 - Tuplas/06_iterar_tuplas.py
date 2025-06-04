# Tuplas se diferenciam de listas por serem imutáveis, ou seja, não podem ser alteradas após a criação.

def printCarros(carros):
    for carro in carros:
        print(carro)

    for indice, carro in enumerate(carros):
        print(f"{indice}: {carro}")

if __name__ == "__main__":  # Bloco de execução principal, escolho o que executar e sua ordem
    carros = (
    "gol",
    "celta",
    "palio",
)
    printCarros(carros)