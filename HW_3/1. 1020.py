# Сложность алгоритма - O(n^2)
from typing import List

class Solution:
    def numEnclaves(self, mat: List[List[int]]) -> int:
        """метод для обозначения аргументов для решения задачи

        Args:
            mat (List[List[int]]): двумерный массив из 0 и 1, нужно 
            посчитать количество островков, с которых не сможем выбраться
            row_1 (int): количество списков в mat
            row_2 (int): количество элементов в списках
        """
        row_1,row_2 = len(mat), len(mat[0])
        WATER, LAND = 0, 1
        
        def dfs(mat, i, j):
            """метод для проверки и исправления того факта, что с острова
               можно сбежать

            Args:
                mat (List[List[int]]): двумерный массив из 0 и 1, нужно 
                посчитать количество островков, с которых не сможем выбраться
                i (int), j (int): итое и житое из циклов (номер элемента)
            """
            if i<0 or i>=row_1 or j<0 or j>=row_2 or mat[i][j] == WATER:
                return
            mat[i][j] = 0
            dfs(mat, i+1, j)
            dfs(mat, i-1, j)
            dfs(mat, i, j+1)
            dfs(mat, i, j-1)
            return
        
        for i in range(row_1):
            for j in range(row_2):
                if mat[i][j] == LAND:
                    if i==0 or i==row_1-1 or j == 0 or j==row_2-1:
                        dfs(mat, i, j)
        count = 0

        for i in range(row_1):
            for j in range(row_2):
                if mat[i][j] == LAND:
                    count += 1
        return count
        
a = Solution()
print(a.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))
# answer = 3
b = Solution()
print(b.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))
# answer = 0