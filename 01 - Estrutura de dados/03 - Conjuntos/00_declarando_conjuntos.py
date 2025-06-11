# Conjuntos são coleções de elementos únicos e não ordenados.
# Eles são úteis quando você precisa garantir que não haja duplicatas em uma coleção de itens.
# São declarados usando chaves `{}` ou a função `set()`.
# Conjuntos são mutáveis, mas não suportam indexação ou fatiamento, pois não são ordenados.

numeros = set([1, 2, 3, 1, 3, 4]) # ou numeros = {1, 2, 3, 1, 3, 4}
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}
