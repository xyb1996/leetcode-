"""
问题描述：有N个比赛队（1<=N<=500），编号依次为1，2，3，。。。。，N进行比赛，
比赛结束后，裁判委员会要将所有参赛队伍从前往后依次排名，但现在裁判委员会不能直接获得每个队的比赛成绩，只知道每场比赛的结果，
即P1赢P2，用P1，P2表示，排名时P1在P2之前。现在请你编程序确定排名。

输入描述：输入有若干组，每组中的第一行为二个数N（1<=N<=500），M；其中N表示队伍的个数，M表示接着有M行的输入数据。
接下来的M行数据中，每行也有两个整数P1，P2表示即P1队赢了P2队。

输出：给出一个符合要求的排名。输出时队伍号之间有空格，最后一名后面没有空格。其他说明：符合条件的排名可能不是唯一的，
此时要求输出时编号小的队伍在前；输入数据保证是正确的，即输入数据确保一定能有一个符合要求的排名。

思路：相当于给定了n个节点，m条边的top排序一样，没有入度的节点的排序肯定是较高的，这时候只需要取其中的min作为最小的
加入到ans里面即可，一直到该入度为0的节点的列表空为止

"""

n, m = map(int, input().strip().split())

#edge[a][b]代表从a指向b的一条边，也即a的排名比b高
#还有一个注意点就是后面出现这种跟排名有关的题目，里面的下标最好从1开始比较好点
edge = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
	a, b = map(int, input().strip().split())
	edge[a].append(b)
	indegree[b] += 1
pre = []
ans = []
for i in range(1, n + 1):
	if indegree[i] == 0:
		pre.append(i)
while pre:
	ans.append(min(pre))
	pre.remove(ans[-1])
	for k in edge[ans[-1]]:
		indegree[k] -= 1
		if indegree[k] == 0:
			pre.append(k)
print(' '.join(map(str, ans)))