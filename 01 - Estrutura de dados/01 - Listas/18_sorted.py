# Sorted é uma função que retorna uma nova lista ordenada a partir de um iterável.

linguagens = ["python", "js", "c", "java", "csharp"]

if __name__ == "__main__": # Bloco de execução principal
    print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
    print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

# Qual o mais eficiente, sort ou sorted?
# sorted é mais eficiente, pois não modifica a lista original, enquanto sort modifica a lista original.