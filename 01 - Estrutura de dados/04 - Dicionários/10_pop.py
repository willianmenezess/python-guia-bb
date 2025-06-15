# pop() remove o item com a chave especificada e retorna o valor associado.

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado) # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(contatos)  # {}

resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)
