# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
		if p==None and q ==None:
			return True
		left =right =False
		if p and q:
			left = self.isSameTree(p.left,q.left)
		if p and q:
			right = self.isSameTree(p.right,q.right)
		if left and right and p.val==q.val:
			return True
		return False
