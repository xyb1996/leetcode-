"""
问题描述：
编写一个算法来判断一个数是不是“快乐数”。

一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

实例：输入: 19
输出: true
解释:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

#思路：对于一个不是快乐数的数字，那么它会出现死循环，比如20，像19会出现循环，但是出现循环最后结果是1，是我们想要的结果

class Solution:
	def isHappy(self, n: int) -> bool:
		num_dict = {}
		while n not in num_dict.keys():
			num_dict[n] = 1
			sum1 = 0
			while n!=0:
				sum1+=(n %10) **2
				n = n //10
			n = sum1
		if n ==1:
			return True
		else:
			return False
solution = Solution()
print(solution.isHappy(7))