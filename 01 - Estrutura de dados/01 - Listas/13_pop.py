linguagens = ["python", "js", "c", "java", "csharp"]

# pop remove o último elemento da lista e o retorna
print(linguagens.pop())  # csharp
print(linguagens)  # ["python", "js", "c", "java"]
print(linguagens.pop())  # java
print(linguagens)  # ["python", "js", "c"]
print(linguagens.pop())  # c
print(linguagens)  # ["python", "js"]
print(linguagens.pop(0))  # python
print(linguagens)  # ["js"]
