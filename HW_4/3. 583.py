# Сложность алгоритма - O(n)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """Метод ищет одинаковые части слова циклом, затем в return
           выдает кол-во действий, чтобы короткое слово превратить в длинное 
        """
        temp = ""
        long = max(word1, word2)
        short = min (word1, word2)
        for i in range(len(long)):
            if temp + long[i] in short:
                temp += long[i]
                print(temp)
        return (len(long) - len(temp) * 2 + len(short))

a = Solution()
print(a.minDistance("leetcode", "etco"))