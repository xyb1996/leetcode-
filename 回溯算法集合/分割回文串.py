#1、利用回溯法实现
class Solution(object):
	def partition(self,s):
		split_result = []
		length = len(s)
		if length  == 0:
			return split_result
		def back(start =0,res=[]):

			if start >=length:
				split_result.append(res)
				return
			#如果这里end不为length+1，那么end取不到length，永远不会appendr（res），
			for end in range(start+1,length+1):
				split_str = s[start:end]
				#如果当前串是回文串，则继续递归下去
				#这里组注意一个坑点，智能用下面这种方式逆序字符串，用end-1：start-1：-1不行，
				if split_str == s[start:end][::-1]:
					back(end,res+[split_str])
		back()
		return split_result
solution1 = Solution()
print(solution1.partition('aab'))