"""
问题描述：国的手机号码由且仅由 N 位十进制数字(0-9)组成。一个手机号码中有至少 K 位数字相同则被定义为靓号

输出要求第一行包含一个整数，表示修改成一个靓号，最少需要的金额。
第二行包含 N 个数字字符，表示最少花费修改的新手机号。若有多个靓号花费都最少，则输出字典序最小的靓号。
"""
from collections import Counter

#计算以t为靓号中的众数，的花费是多少
def distance(dic, k, t):
	ret = 0
	#如果原来的字符串中有大于等于k个t，则ret = 0
	if dic[t] >= k: return ret
	k -= dic[t]
	for i in range(1, 10):
		#i表示距离t的距离，从靠近t的元素开始两边搜索
		if t + i < 10:
			if dic[t + i] >= k:
				ret += i * k
				return ret
			else:
				k -= dic[t + i]
				ret += i * dic[t + i]
		if t - i >= 0:
			if dic[t - i] >= k:
				ret += i * k
				return ret
			else:
				k -= dic[t - i]
				ret += i * dic[t - i]


def modify(s, dic, k, t):
	if dic[t] >= k: return
	k -= dic[t]
	for i in range(1, 10):
		if t + i < 10:
			#t+i大于t，表示如果靓号众数小于当前数字，则从左往右开始修改
			for j in range(len(s)):
				#如果k为0，则表示修改结束
				if k == 0: return
				if s[j] == t + i:
					s[j] = t
					k -= 1
		#t-i小于t，当前数字小于众数，从后往前替换众数
		if t - i >= 0:
			for j in range(len(s) - 1, -1, -1):
				if k == 0: return
				if s[j] == t - i:
					s[j] = t
					k -= 1


if __name__ == "__main__":
	n, k = map(int, input().strip().split())
	s = list(map(int, list(input().strip())))
	dic = Counter(s)
	for i in range(10):
		if i not in dic:
			dic[i] = 0
			#设置ans为最大值
	ans_cost, ans_num = float("inf"), -1
	for i in range(10):
		#记录以i为众数的花费，选择最大值并记录t
		tmp = distance(dic, k, i)
		if ans_cost > tmp:
			ans_cost = tmp
			ans_num = i
	modify(s, dic, k, ans_num)
	print(ans_cost)
	print(''.join(map(str, s)))