# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
from collections import deque
class Solution:
	def LevelOrder(self, root: TreeNode):
		levels = []
		if not root:
			return levels

		level = 0
		queue = deque([root,])

		while len(queue) >0:
			#如果当前层次等于结果数组的层数

			levels.append([])
			length = len(queue)

			for i in range(length):

				p = queue.popleft()
				levels[level].append(p.val)
				if  p.left:
					queue.append(p.left)
				if p.right:
					queue.append(p.right)
			level+=1
		return levels


