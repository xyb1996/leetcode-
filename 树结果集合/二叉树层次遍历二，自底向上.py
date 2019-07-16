from collections import deque
class Solution:
	def levelOrderBottom(self, root):

		def levelOrder(root):
			res= []
			if not root:
				return res

			queue = deque([root])
			level = 0

			while queue:
				res.append([])
				length = len(queue)

				for i in range(length):
					p = queue.popleft()
					res[level].append(p.val)
					if p.left:
						queue.append(p.left)
					if p.right:
						queue.append(p.right)
				level+=1
			return res

		tmp = levelOrder(root)
		length = len(tmp)
		res=[[] for _ in range(length)]
		for i in range(length):
			res[i] = tmp[length-1-i]
		return res