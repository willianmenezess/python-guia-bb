matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

if __name__ == "__main__": # Bloco de execução principal, escolho o que executar e sua ordem
    print(matriz[0])  # (1, "a", 2)
    print(matriz[0][0])  # 1
    print(matriz[0][-1])  # 2
    print(matriz[-1][-1])  # "c"
