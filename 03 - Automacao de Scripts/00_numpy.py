"""
===============================================
MÓDULO: NumPy (Numerical Python)
===============================================

O NumPy é uma biblioteca fundamental para computação científica com Python.
Ela oferece suporte para:

- Arrays multidimensionais (ndarray), com operações eficientes e vetorizadas.
- Funções matemáticas, estatísticas, lógicas e de álgebra linear otimizadas.
- Leitura e gravação de dados em arquivos binários e texto.
- Integração com outras bibliotecas científicas como SciPy, Pandas, Matplotlib etc.

Instalação (caso ainda não tenha):
    pip install numpy

-----------------------------------------------
IMPORTANTE:
-----------------------------------------------
- O principal objeto do NumPy é o ndarray: um array N-dimensional de elementos do mesmo tipo.
- Operações com arrays são vetorizadas (mais rápidas que loops tradicionais em Python).
- É amplamente usado em análise de dados, machine learning, deep learning, simulações numéricas e muito mais.

-----------------------------------------------
EXEMPLOS BÁSICOS:
-----------------------------------------------
"""

# Importando a biblioteca
import numpy as np

# Criando arrays
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])

# Operações elementares
soma = a + 2               # [3 4 5]
produto = a * 3            # [3 6 9]
quadrado = a ** 2          # [1 4 9]

# Funções úteis
media = np.mean(a)         # 2.0
soma_total = np.sum(b)     # 21
transposta = b.T           # Transposição da matriz b

# Criando arrays especiais
zeros = np.zeros((2, 3))   # Matriz 2x3 de zeros
identidade = np.eye(3)     # Matriz identidade 3x3
sequencia = np.arange(0, 10, 2)  # [0 2 4 6 8]
espaco_linear = np.linspace(0, 1, 5)  # [0.   0.25 0.5  0.75 1.]

# Indexação e fatiamento
print(a[1])         # 2
print(b[0, 2])      # 3
print(b[:, 1])      # Segunda coluna: [2 5]

# Álgebra Linear
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
produto_matricial = np.dot(mat1, mat2)  # [[19 22], [43 50]]

# Reshape (mudança de forma)
vetor = np.array([1, 2, 3, 4, 5, 6])
matriz = vetor.reshape((2, 3))  # [[1 2 3], [4 5 6]]

# Desvio-padrao
x = np.array([1, 2, 2, 3, 5])
desvio_padrao = np.std(x, ddof=1)  # 1.5811388300841898 (ddof=1 para amostra)

"""
Referência oficial: https://numpy.org
"""
