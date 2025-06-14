# intersection() retorna um novo conjunto com os elementos comuns entre dois conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b)
print(resultado)

# intersection_update() atualiza o conjunto com a interseção de dois conjuntos
conjunto_a.intersection_update(conjunto_b)
print(conjunto_a)
