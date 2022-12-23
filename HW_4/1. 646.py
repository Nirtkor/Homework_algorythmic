# Сложность алгоритма - O(n^2)
from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """Алгоритм позволяет пройти по всему двумерному массиву
           и без повторений указать количество связей
        """
        pairs.sort()
        dp = [1]*len(pairs)
        for i in range(len(pairs)):
            for j in range(len(pairs)):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        print(dp)
        return max(dp)

a = Solution()
print(a.findLongestChain([[1,2],[2,3],[3,4]]))
# answer = 2
print(a.findLongestChain([[1,2],[7,8],[4,5]]))
# answer = 3