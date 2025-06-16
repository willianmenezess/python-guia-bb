def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"): # argumento default
    print(f"Seja bem vindo {nome}!")

if __name__ == "__main__":
#Para testar o código localmente sem afetar seu uso como módulo. Para evitar que certas partes do código 
# rodem automaticamente ao serem importadas. É uma boa prática em projetos organizados, reutilizáveis 
# e com múltiplos arquivos.
    exibir_mensagem()
    exibir_mensagem_2("Guilherme") # ou exibir_mensagem_2(nome="Guilherme")
    exibir_mensagem_3()
    exibir_mensagem_3("Chappie") # ou exibir_mensagem_3(nome="Chappie")