linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"], sorteia em ordem alfabética
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"], sorteia em ordem alfabética reversa
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"], sorteia pelo tamanho da string,
# key é uma função que recebe um elemento e retorna o valor a ser usado para ordenação
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)

# O Método sort() é um método de lista que ordena a lista original, enquanto a 
# função sorted() retorna uma nova lista ordenada.