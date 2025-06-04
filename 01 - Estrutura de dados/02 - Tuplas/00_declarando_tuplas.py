# Tuplas se diferenciam de listas por serem imutáveis, ou seja, não podem ser alteradas após a criação.
# São úteis quando você precisa de uma coleção de itens que não deve ser alterada, como coordenadas 
# geográficas, cores RGB, etc.

frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)
