class Solution(object):
	#中序遍历的顺序是递增的，如果当前值小于等于上一个遍历值，那么逐层地返回False
	def __init__(self):
		self.tmp = -float('inf')
	def isValidBST(self, root):
		"""
        :type root: TreeNode
        :rtype: bool
        """
		if not root:return True
		if not self.isValidBST(root.left):return False

		if root.val<=self.tmp:return False
		self.tmp = root.val

		if not self.isValidBST(root.right):
			return False
		return True