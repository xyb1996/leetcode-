"""
题目描述：
现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？

"""
#思路：只要给定的关系图中不出现环，就是可学习的
#利用Dfs和Bfs来遍历图，边遍历边记录，如果遍历过程中出现了已经访问的节点或者最终遍历的总节点>n，那么就出现了环

#DFS遍历
class Solution:
	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		from collections import defaultdict
		graph = defaultdict(list)
		# 记录
		visited = set()
		# 建图
		for x, y in prerequisites:
			graph[y].append(x)

		# 深度遍历
		def dfs(i, being_visited):
			if i in being_visited: return False
			#visited表示已经访问过，并且确认是遍历之后没有环的
			if i in visited: return True
			visited.add(i)
			being_visited.add(i)
			for j in graph[i]:
				if not dfs(j, being_visited): return False
			being_visited.remove(i)
			return True
		# 检测每门功课起始是否存在环
		for i in range(numCourses):
			# 已经访问过
			if i in visited: continue
			if not dfs(i, set()): return False
		return True

#BFS遍历

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque
        graph = defaultdict(list)
		#统计每个点的入度信息。
        degree = [0] * numCourses
        # 建图
        for x, y in prerequisites:
            graph[y].append(x)
            degree[x] += 1
        queue = deque([i for i in range(numCourses) if degree[i] == 0])
        #print(queue)
        cnt = 0
        while queue:
			#出度并访问
            i = queue.pop()
            cnt += 1
			#并且减少每个汉字节点的入度，然后将入度为0的点继续入栈
            for j in graph[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    queue.appendleft(j)
        return cnt == numCourses

