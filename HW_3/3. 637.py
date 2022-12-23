# Сложность алгоритма - O(n^2)
class TreeNode:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
	def averageOfLevels(self, root: TreeNode):
		""" Идем по дереву, постепенно считаем среднее и вырезаем с помощью pop

		Args:
			root (TreeNode): мудрое дерево
		"""
		if not root:
			return 0
		q = [root]
		res = [root.val]

		while q:
			size = len(q)
			l = []
			while size:
				front = q.pop(0)
				size-=1

				if front.left:
					q.append(front.left)
					l+=[front.left.val]
				if front.right:
					q.append(front.right)
					l+=[front.right.val]

			if l:
				avg = sum(l)/len(l)
				res.append(avg)

		return res

a = Solution()
print(a.averageOfLevels(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
# answer [3, 14.5, 11.0]
print(a.averageOfLevels(TreeNode(3,TreeNode(9, TreeNode(15), TreeNode(7)), TreeNode(20))))
# answer [3, 14.5, 11.0]