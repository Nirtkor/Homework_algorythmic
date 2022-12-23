from typing import List

def getDescentPeriods(prices: List[int]):
    """Сложность алгоритма - O(n), т.к. один цикл

    Args:
        prices (List[int]): целочисленный массив с ценами.

    Returns:
        sum(dp): возвращаем сумму единиц в массиве, который отражает
        количество дней с плавным спуском цен.
    """
    n = len(prices)
    dp = [1]*n

    for i in range(1,n):
        if prices[i] +1 == prices[i-1]:
            dp[i] += dp[i-1]

    return sum(dp)

print(getDescentPeriods([3,2,1,4]))
    