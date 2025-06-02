# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0] # Compreensão de lista para filtrar números pares
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)

# Obs: Filtrar lista sem compreensão de lista
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)