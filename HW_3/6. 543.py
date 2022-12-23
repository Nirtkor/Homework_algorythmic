# Сложность алгоритма - O(n)
class TreeNode:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        queue = [root]
        result = 0

        while queue:
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            elif not (queue[0].right and queue[0].left):
                result += 1
            queue.pop(0)
        return result

a = Solution()
print(a.diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))))
# answer = 3