"""
利用回溯法,其实就是递归地暴力求解，加上一些判断，减少很多执行步骤。
回溯算法需要好好理解理解。
"""

class Solution:
	def generateParenthesis(self, n: int) -> [str]:
		result = []
		def backtrack(S='',left=0,right=0):
			if len(S) ==2*n:
				result.append(S)
				return
			if left< n:
				backtrack(S+'[',left+1,right)
			if right <left:
				backtrack(S+']',left,right+1)
		backtrack()
		return result


#下面的这种方法简直就是艺术啊
class Solution2:
	def generateParenthesis(self,n):
		result = []

		if n ==0:
			return ['']
		#共生成多少对括号
		for i in range(n):
			for left in self.generateParenthesis(i):
				for right in self.generateParenthesis(n-1-i):
					result.append("({})({})".format(left,right))
		return result