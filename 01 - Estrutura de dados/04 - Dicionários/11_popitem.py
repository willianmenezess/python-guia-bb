# popitem() remove e retorna o último par de chave-valor inserido no dicionário.

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado)
print(contatos)  # {}

# contatos.popitem()  # KeyError
