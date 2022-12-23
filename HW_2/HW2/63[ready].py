from typing import List

def uniquePathsWithObstacles(obstacleGrid: List[List[int]]):
    """ Сложность алгоритма - O(n*m), т.к. цикл с вложенным циклом.

    Args:
        obstacleGrid (List[List[int]]): двумерный массив из нулей и единиц.
        Робот двигается из левого верхнего угла в нижний правый.

    Returns:
        dp[-1]: количество возможных уникальных путей, по которым робот 
                может добраться до правого нижнего угла (с учетом преград).
    """
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    
    if obstacleGrid[0][0] == 1:
        return 0
    
    dp = [0] * n
    dp[0] = 1
    print(dp)
    
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[j] = 0
            elif j >= 1:
                dp[j] += dp[j - 1]
    
    return dp[-1]
    