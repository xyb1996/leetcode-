class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

#自顶向下遍历的方法:

class Solution:

	def isBalanced(self, root: TreeNode) -> bool:
		if not root:
			return True
		if abs(self.height(root.left)-self.height(root.right))<2 and self.isBalanced(root.left) and self.isBalanced(root.right):
			return True
		return False

	def height(self,root):
		if not root:
			return 0
		left = self.height(root.left)
		right = self.height(root.right)
		return max(left,right)+1

#采用自底向上遍历的方法
	def isBalanced(self,root):
		self.res = True
		def helper(root):
			if not root:
				return 0
			left= helper(root.left)+1
			right = helper(root.right)+1

			if abs(left - right)>1:
				self.res = False
			return max(left,right)
		helper(root)
		return self.res