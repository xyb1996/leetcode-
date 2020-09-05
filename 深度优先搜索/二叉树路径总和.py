#Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def hasPathSum(self, root: TreeNode, sum: int) -> bool:
		if not root:
			return False
		sum-=root.val
		if  not root.left and not root.right and sum == 0:
			return True
		return self.hasPathSum(root.left) or self.hasPathSum(root.right)
	def hasPathSum2(self,root,sum):
		if not root:
			return False
		de = [(root,sum-root.val)]

		while de:
			node,cur_sum = de.pop()
			if not node.left and not node.right and cur_sum ==0:
				return True
			if node.right:
				de.append((node.right,cur_sum-node.right.val))
			if node.left:
				de.append((node.left,cur_sum-node.left.val))
		return False