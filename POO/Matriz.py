class Matriz:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.data = [[0] * colunas for _ in range(linhas)]

    def imprimir(self):
        for linha in self.data:
            print(linha)

    def adicionar(self, outra_matriz):
        if self.linhas == outra_matriz.linhas and self.colunas == outra_matriz.colunas:
            resultado = Matriz(self.linhas, self.colunas)
            resultado.data = [[self.data[i][j] + outra_matriz.data[i][j] for j in range(self.colunas)] for i in range(self.linhas)]
            return resultado
        else:
            raise ValueError("As matrizes não têm as mesmas dimensões para adição")

    def multiplicar(self, outra_matriz):
        if self.colunas == outra_matriz.linhas:
            resultado = Matriz(self.linhas, outra_matriz.colunas)
            for i in range(self.linhas):
                for j in range(outra_matriz.colunas):
                    resultado.data[i][j] = sum(self.data[i][k] * outra_matriz.data[k][j] for k in range(self.colunas))
            return resultado
        else:
            raise ValueError("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz para multiplicação")

    def transpor(self):
        resultado = Matriz(self.colunas, self.linhas)
        resultado.data = [[self.data[j][i] for j in range(self.linhas)] for i in range(self.colunas)]
        return resultado

    def determinante(self):
        if self.linhas == self.colunas:
            if self.linhas == 2:
                return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
            else:
                det = 0
                for i in range(self.linhas):
                    det += ((-1) ** i) * self.data[0][i] * self.submatriz(0, i).determinante()
                return det
        else:
            raise ValueError("A matriz não é quadrada")

    def submatriz(self, i, j):
        submatriz = Matriz(self.linhas - 1, self.colunas - 1)
        submatriz.data = [linha[:j] + linha[j+1:] for linha in (self.data[:i] + self.data[i+1:])]
        return submatriz

# Exemplo de uso
matriz1 = Matriz(2, 2)
matriz1.data = [[1, 2], [3, 4]]

matriz2 = Matriz(2, 2)
matriz2.data = [[5, 6], [7, 8]]

print("Matriz 1:")
matriz1.imprimir()

print("\nMatriz 2:")
matriz2.imprimir()

print("\nAdição de matrizes:")
resultado_soma = matriz1.adicionar(matriz2)
resultado_soma.imprimir()

print("\nMultiplicação de matrizes:")
resultado_multiplicacao = matriz1.multiplicar(matriz2)
resultado_multiplicacao.imprimir()

print("\nTransposição da Matriz 1:")
resultado_transposicao = matriz1.transpor()
resultado_transposicao.imprimir()

print("\nDeterminante da Matriz 1:")
det_matriz1 = matriz1.determinante()
print(det_matriz1)
