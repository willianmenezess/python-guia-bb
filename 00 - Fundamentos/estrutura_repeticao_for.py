texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


# Exemplo utilizando um iterável
for letra in texto: # percorre cada letra do texto, que tbm é iterável
    if letra.upper() in VOGAIS: # verifica se a letra é uma vogal
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5): # percorre de 0 a 50, pulando de 5 em 5
    print(numero, end=" ")
