# Сложность алгоритма - O(n^2)
from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """метод для обозначения аргументов для решения задачи

        Args:
            grid (List[List[int]]): двумерный массив, в котором нужно найти ограниченные водой острова
            row_1 (int): количество списков в grid
            row_2 (int): количество элементов в списках
        """
        row_1 = len(grid)
        row_2 = len(grid[0])
    
        def check(i, j):
            """чекер для островов

            Args:
                i (int), j (int): итое и житое из цикла
            """
            if not(i < 0 or j < 0 or i == row_1 or j == row_2):
                if grid[i][j] == 1:
                    return 1
                grid[i][j] = 1
                if check(i - 1, j) and check(i + 1, j) and check(i, j + 1) and check(i, j - 1):
                    return 1
                else:
                    return 0
        
        count = 0
        for i in range(row_1):
            for j in range(row_2):
                if grid[i][j] == 0:
                    result = check(i, j)
                    if result:
                        count += result
        return count

a = Solution()
print(a.numEnclaves([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))