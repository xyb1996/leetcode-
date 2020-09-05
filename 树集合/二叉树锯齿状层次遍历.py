from collections import deque
class Solution:
	def zigzagLevelOrder(self, root):
		res = []
		if not root:
			return res

		queue = deque([root,])
		level = 0

		while queue:
			tmp =[]
			length = len(queue)

			for i in range(length):
				p = queue.popleft()
				tmp.append(p.val)
				if p.left :
					queue.append(p.left)
				if p.right:
					queue.append(p.right)
			if level %2 ==1:
				tmp = tmp[::-1]
			res.append(tmp)
			level+=1
		return res


