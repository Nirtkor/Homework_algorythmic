# Сложность алгоритма - n(1)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int):
        """Постригаем кусты согласно поставленым ограничениям
        """
        def trim(node):
            if not node:
                return 
            if node.val<low:
                return trim(node.right)
            elif node.val>high:
                return trim(node.left)
            else:
                node.left, node.right = trim(node.left), trim(node.right)
                return node
        return trim(root)
        

a = Solution()
prostatit = a.trimBST(TreeNode(1, TreeNode(0),  TreeNode(2)), 1, 2)
stack = [prostatit]
while stack:
    stack.append(stack[0].left) if stack[0].left else None
    stack.append(stack[0].right) if stack[0].right else None
    print(stack.pop(0).val)

# на литкоде все работает и без простатита, но как это реализовать тут без понятия...