# Сложность алгоритма - O(1)
class LinkedList:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    
class Solution:
    def getDecimalValue(self, head: LinkedList):
        """создаем строку, в неё вписываем значения, проходя по связанному
        списку, затем из двоичной записи переводим в десятичную
        """
        s = ''
        while head:
            s += str(head.val)
            head = head.next
        return int(s, 2)

a = Solution()
print(a.getDecimalValue(LinkedList(1, LinkedList(0, LinkedList(1)))))
# answer = 5
print(a.getDecimalValue(LinkedList(0)))
# answer = 0