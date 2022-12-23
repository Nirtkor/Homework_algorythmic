from typing import List

def countSquares(matrix: List[List[int]]):
    """Сложность алгоритма - O(m*n), т.к. два вложенных цикла для перебора
                                          двумерного массива

    Args:
        matrix (List[List[int]]): матрица с нулями и единицами

    Returns:
        countSquares: на выход подается целочисленное значение квадратов,
        которые строятся из единиц (различных размеров 1x1, 2x2, 3x3)
    """
    countSquares = 0
    dp = [[0 for i in matrix[0]] for j in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] and i > 0 and j > 0:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1
            else:
                dp[i][j] = matrix[i][j]
            countSquares += dp[i][j]
    return countSquares
