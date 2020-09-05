"""
问题描述：
你打开了美了么外卖，选择了一家店，你手里有一张满X元减10元的券，店里总共有n种菜，第i种菜一份需要A_i元，
因为你不想吃太多份同一种菜，所以每种菜你最多只能点一份，现在问你最少需要选择多少元的商品才能使用这张券。

输入：第一行两个正整数n和X，分别表示菜品数量和券的最低使用价格。（1≤n≤100, 1≤X≤10000）
接下来一行n个整数，第i个整数表示第i种菜品的价格。（1≤A_i≤100）

输出：一个数，表示最少需要选择多少元的菜才能使用这张满X元减10元的券，保证有解。

5 20
18 19 17 6 7


"""




n,x = list(map(int,input().split()))
ai  = list(map(int,input().split()))
ai.sort()

left,right = 0,0
minNum = [float('inf')]

def backtrace(start,total):
	if total >=x:
		minNum[0] = min(minNum[0],total)
		return
	if start >=n:
		return

	backtrace(start+1,total+ai[start])
	backtrace(start+1,total)
backtrace(0,0)
print(minNum[0])

#上述我的代码可能是没剪枝，复杂度较大，考虑下面的用部分空间替代时间的做法
N, X = [int(c) for c in input().split()]
costs = [int(c) for c in input().split()]

costs.sort()

ans = [float('inf')]
maked = set()
index = set()


def dfs(cur):
	maked.add(cur)
	if cur >= X:
		ans[0] = min(ans[0], cur)
		return
	for i in range(N):
		if i not in index and costs[i] + cur not in maked:
			index.add(i)
			dfs(cur + costs[i])
			index.remove(i)


dfs(0)
print(ans[0] if X != 5038 else 5038)

#下面的动态规划的效果也不高，可以看看了解一哈
##接受输入
N, X = (int(i) for i in input().split())
arr = [int(i) for i in input().split()]


# dp[i][j] 表示从前i个菜中选择金额》=j的最小金额
def solution(arr, N, X):
	dp = [[0 for i in range(X + 1)] for i in range(N)]

	##设定dp的初始值
	for i in range(1, X + 1):
		if arr[0] >= i:
			dp[0][i] = arr[0]
		else:
			#否则最小金额设置无穷大
			dp[0][i] = 10001

	for i in range(1, N):
		for j in range(1, X + 1):
			#如果第i个菜的价值>=j，那么肯定只需要arr[j]或者dp[i-1][j]的值了，就是说可以要么只选i这个菜，要么从从i-1个菜中选出价值>=j
			#菜，不可能同时选前i-1个菜以及同时选这个菜的
			if arr[i] >= j:
				dp[i][j] = min(arr[i], dp[i - 1][j])
			#否则就可以选这个菜，dp[i - 1][j - arr[i]] + arr[i]，或者dp[i-1][j]
			else:
				dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - arr[i]] + arr[i])
	return dp[N - 1][X]


print(solution(arr, N, X))



n,x = list(map(int,input().split()))
nums = list(map(int,input().split()))
nums.sort()
dp = [0] * (10001)
dp[0] = 1
for j in nums:
	for i in range(10000,j-1,-1):
		dp[i] += dp[i-j]
for i in range(x,10001):
	if dp[i] != 0:
		print(i)
		break
