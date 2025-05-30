saldo = 2000
saque = 2500

status = "Sucesso" if saldo >= saque else "Falha" # condicional ternária

print(f"{status} ao realizar o saque!") # Saída: Falha ao realizar o saque!
