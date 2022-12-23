# Сложность алгоритма - (n)
class TreeNode:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root):
        """Проходим по мудрому дереву, рассматривая отдельно левую и правую
        ветвь (в случае если звеньев будет много, цикл будет заново
        вызывать метод и записывать более длинные ответы в result)
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        result = []
        if root.left: 
            for path in self.binaryTreePaths(root.left):
                result.append(str(root.val) + "->" + path)
        if root.right: 
            for path in self.binaryTreePaths(root.right):
                result.append(str(root.val) + "->" + path)
        return result

a = Solution()
print(a.binaryTreePaths(TreeNode(1, TreeNode(2, TreeNode(5)),  TreeNode(3))))
# answer = ['1->2->5', '1->3']
print(a.binaryTreePaths(TreeNode(1)))
# answer = ['1']