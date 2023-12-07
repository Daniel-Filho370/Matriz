from functools import reduce

# Função para criar uma matriz
def criar_matriz(linhas, colunas):
    return [[0] * colunas for _ in range(linhas)]

# Função para imprimir uma matriz
def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

# Função para somar duas matrizes
def adicionar_matrizes(matriz1, matriz2):
    return [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]

# Função para multiplicar duas matrizes
def multiplicar_matrizes(matriz1, matriz2):
    resultado = criar_matriz(len(matriz1), len(matriz2[0]))
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            resultado[i][j] = sum(matriz1[i][k] * matriz2[k][j] for k in range(len(matriz2)))
    return resultado

# Função para transpor uma matriz
def transpor_matriz(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

# Função para calcular o determinante de uma matriz 2x2
def determinante_2x2(matriz):
    return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

# Função para calcular o determinante de uma matriz
def determinante(matriz):
    if len(matriz) == len(matriz[0]):
        if len(matriz) == 2:
            return determinante_2x2(matriz)
        else:
            det = 0
            for i in range(len(matriz)):
                det += ((-1) ** i) * matriz[0][i] * determinante([linha[:i] + linha[i+1:] for linha in matriz[1:]])
            return det
    else:
        raise ValueError("A matriz não é quadrada")

# Exemplo de uso
matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]

print("Matriz 1:")
imprimir_matriz(matriz1)

print("\nMatriz 2:")
imprimir_matriz(matriz2)

print("\nAdição de matrizes:")
imprimir_matriz(adicionar_matrizes(matriz1, matriz2))

print("\nMultiplicação de matrizes:")
imprimir_matriz(multiplicar_matrizes(matriz1, matriz2))

print("\nTransposição da Matriz 1:")
imprimir_matriz(transpor_matriz(matriz1))

print("\nDeterminante da Matriz 1:")
print(determinante(matriz1))
