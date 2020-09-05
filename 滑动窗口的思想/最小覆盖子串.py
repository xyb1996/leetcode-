"""
问题描述：给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"

说明：如果 S 中不存这样的子串，则返回空字符串 ""。
"""

#思路一：基于滑动窗口法，滑动窗口法，通常有两个指针left,right，一般都是一个保持不动，一个移动
#本题，left、right 初始指向0，right开始滑动，直到包含满足t子串的所有字符，right停止
#然后left向右移动，如果left向右移动任满足条件，继续，否则，开始移动right，这样基本扫描了整个原始串，并搜索到了最小的串。


#python中滑动窗口的字母集合用字典来统计，并用一个formed来记录已经包含t的字母的个数


from collections import Counter
class Solution:
	def minWindow(self, s: str, t: str) -> str:
		if len(s) == 0 or len(t) == 0:
			return ''
		length = len(s)
		left = right = 0
		formed = 0
		target = dict(Counter(t))
		required = len(target)
		window_dict = {}
		#ans是个lenght，left，right的三元组
		ans = float('inf'),None,None
		while right < length :
			#right指针右移
			while right < length and formed < required:
				character = s[right]
				#有则加1，无则赋值为0
				window_dict[character] = window_dict.get(character,0)+1
				if character in target.keys() and window_dict[character] == target[character]:
					formed +=1
				right +=1
			#left指针左移

			while left < length and formed ==required:
				tmp = (right - left) , left , right
				if tmp[0] < ans[0]:
					ans = tmp
				character = s[left]
				window_dict[character] = window_dict.get(character,0)-1
				if character in target and window_dict[character]< target[character]:

					formed-=1
				left+=1


		if ans[1] ==None or ans[2] == None :
			return ''
		return s[ans[1]:ans[2]]

solution = Solution()
print(solution.minWindow("A"
,"AA"))