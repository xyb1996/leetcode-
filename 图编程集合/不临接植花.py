"""
问题描述：
有 N 个花园，按从 1 到 N 标记。在每个花园中，你打算种下四种花之一。
paths[i] = [x, y] 描述了花园 x 到花园 y 的双向路径。
另外，没有花园有 3 条以上的路径可以进入或者离开。
你需要为每个花园选择一种花，使得通过路径相连的任何两个花园中的花的种类互不相同。
以数组形式返回选择的方案作为答案 answer，其中 answer[i] 为在第 (i+1) 个花园中种植的花的种类。
花的种类用  1, 2, 3, 4 表示。保证存在答案。
"""

#思路：首先对第一个点涂1，然后，然后从第二个点开始循环执行以下操作，首先找出该点所有的邻接点，并用一个result
#用来记录已经涂好色的节点，对于未涂色的节点跳过，对于节点编号小于等于result的节点进行判断，如果他们还是领节点，
#则该点进行涂色的颜色集合中要去掉该点，然后选颜色集合的第一个颜色值进行涂色，循环执行下去就ok了。
class Solution:
	def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
		route = {}
		for i in range(1,N+1):
			route[str(i)] = []

		for i in paths:
			route[str(i[0])].append(i[1])
			route[str(i[1])].append(i[0])

		res = [1]

		for i in range(2,N+1):
			colors= [1,2,3,4]
			#表示该节点的邻接点
			adjnodes = route[str(i)]
			for j in adjnodes:
				#j大于res长度，表示这些邻接点还没有被涂色，不用考虑
				if j >len(res):
					continue
				else:
					if res[j-1] in colors:
						colors.remove(res[j-1])
			res.append(colors[0])
		return res