"""问题描述:小多采购了 N 个品种的树，每个品种的数量是 Ai (树的总数量恰好为 M)。
但是他希望任意两棵相邻的树不是同一品种的。"""
"""输入：第一行包含一个正整数 N，表示树的品种数量。
第二行包含 N 个正整数，第 i (1 <= i <= N) 个数表示第 i 个品种的树的数量。
数据范围：
1 <= N <= 1000
1 <= M <= 2000"""
"""输出：输出一行，包含 M 个正整数，分别表示第 i 棵树的品种编号 (品种编号从1到 N)。
若存在多种可行方案，则输出字典序最小的方案。若不存在满足条件的方案，则输出"-"。"""
from functools import reduce

class Solution(object):
	def __init__(self):
		self.n = int(input())
		self.tree = list(map(int,input().split()))
		self.m = int(reduce(lambda x,y:x+y,self.tree))
		self.ans = []
	def check(self,left):
		for i in range(self.n):
			if self.tree[i] >(left+1) //2:
				return False
		return True
	def dfs(self,idx):
		if not (self.check(self.m-idx)):
			return False
		if idx ==self.m:
			return True
		else:
			for i in range(self.n):
				if idx ==0 or (self.tree[i]>0 and (i+1)!=self.ans[idx-1] ):
					self.tree[i]-=1
					self.ans.append(i+1)
					if self.dfs(idx+1):
						return True
					self.ans.pop()
					self.tree[i]+=1
		return False
#对小空间貌似行
solution = Solution()
if solution.dfs(0):
	print(solution.ans)
else:
	print('-')

