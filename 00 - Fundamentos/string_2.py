nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28}

print("Nome: %s Idade: %d" % (nome, idade)) # Formatação antiga

print("Nome: {} Idade: {}".format(nome, idade)) # Formatação com .format()

print("Nome: {1} Idade: {0}".format(idade, nome)) # Formatação com .format() e índices
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome)) # Formatação com .format() e índices repetidos

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}") # Formatação com f-strings (Python 3.6+)
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}") # Formatação com f-strings e formatação de float
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}") # Formatação com f-strings e formatação de float com largura mínima
