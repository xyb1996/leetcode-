class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
#这是递归版
class Solution:
	def pathSum(self, root: TreeNode, sum: int):
		result = []
		if not root:return result
		def helper(root,cur,tmp=[]):

			cur = cur+root.val
			tmp = tmp+[root.val]
			if not root.left and not root.right:
				if cur ==sum:
					result.append(tmp)
				return
			if root.left:
				helper(root.left,cur,tmp)
			if root.right:
				helper(root.right,cur,tmp)
			tmp.pop()
		helper(root,0,[])
		return result
