"""
问题描述：
对于某些固定的 N，如果数组 A 是整数 1, 2, ..., N 组成的排列，使得：

对于每个 i < j，都不存在 k 满足 i < k < j 使得 A[k] * 2 = A[i] + A[j]。

那么数组 A 是漂亮数组。


给定 N，返回任意漂亮数组 A（保证存在一个）。

思路：如果一个数组是漂亮的，那么对其进行仿射变换后仍然是漂亮的，
那么我们就可以采用分治的算法，将奇数都放置在数组左边，偶数都放置在右边，，那么i从左边取出一个数，j从右边取出一个数，由于
递归的左边和右边都是漂亮的了，已经考虑过了。
那么肯定不满足上面的条件

"""
class Solution(object):
	def beautifulArray(self,N):
		memo = {1:[1]}
		def f(N):
			if N not in memo:
				odds = f((N+1)/2)
				evens = f(N /2)
				memo[N] = [2*x-1 for x in odds] +[2*x for x in evens ]
				return memo[N]
		return f(N)