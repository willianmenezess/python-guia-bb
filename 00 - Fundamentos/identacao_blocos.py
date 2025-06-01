# Obs: global saldo fora das funções não tem efeito. Em Python, a declaração global deve estar 
# dentro da função onde você quer usar a variável global.

def sacar(valor): # função para sacar dinheiro
    global saldo  # Usando a variável global saldo
    if saldo >= valor:
        saldo -= valor
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")
        print(f"Saldo atual: {saldo}")
    else:
        print("Saldo insuficiente para realizar o saque.")
        print(f"Saldo atual: {saldo}")
        print("Tente um valor menor ou faça um depósito.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")


def depositar(valor):
    global saldo  # Usando a variável global saldo
    saldo += valor
    print(f"Depósito de {valor} realizado com sucesso!")
    print(f"Saldo atual: {saldo}")
    print("Obrigado por ser nosso cliente, tenha um bom dia!")


if __name__ == "__main__": # Bloco de execução principal
    # Testando a função de saque
    saldo = 500  # Definindo um saldo inicial
    sacar(100)
    sacar(600)  # Teste com valor maior que o saldo
    depositar(200)  # Teste de depósito