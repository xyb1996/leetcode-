class Solution:
    #该动态规划，递推法很好，因为第一列和第一行是边界，所有只会有一种方法，所以都赋值为1，其余的位置来自
    #左边的方法数+上边的方法数。
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
#该优化不错，因为计算dp[i][j]每次只要前面一个数，加上上面一个数，所以，当遍历完一行的时候，
#直接令pre = cur，在开始遍历下一行就ok了
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j-1]
            pre = cur[:]
        return pre[-1]

#这个优化就更牛逼了，慢慢体会，可悟不可语。
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]




solution =Solution()
print(solution.uniquePaths(7,3))


