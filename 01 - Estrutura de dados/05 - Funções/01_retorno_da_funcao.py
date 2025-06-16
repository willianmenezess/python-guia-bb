def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor # retorna uma tupla com antecessor e sucessor


if __name__ == "__main__":
#Para testar o código localmente sem afetar seu uso como módulo. Para evitar que certas partes do código 
# rodem automaticamente ao serem importadas. É uma boa prática em projetos organizados, reutilizáveis 
# e com múltiplos arquivos.
    print(calcular_total([10, 20, 34]))  # 64
    print(retorna_antecessor_e_sucessor(10))  # (9, 11)
