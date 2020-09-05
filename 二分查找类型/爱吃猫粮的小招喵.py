"""
题目描述：小招喵喜欢吃喵粮。这里有 N 堆喵粮，第 i 堆中有 p[i] 粒喵粮。喵主人离开了，将在 H 小时后回来。

小招喵可以决定她吃喵粮的速度 K （单位：粒/小时）。每个小时，她将会选择一堆喵粮，从中吃掉 K 粒。如果这堆喵粮少于 K 粒，她将吃掉这堆的所有喵粮，然后这一小时内不会再吃更多的喵粮。

小招喵喜欢慢慢吃，但仍然想在喵主人回来前吃掉所有的喵粮。

返回她可以在 H 小时内吃掉所有喵粮的最小速度 K（K 为整数）。
"""

#思路：通过二分查找法来查找最小速度。首先肯定存在一个最快的速度，就是max(p)
#最慢的速度就是每次sum(p) / h
import math
p = [int(i) for i in input().split()]
h = int(input())

left = sum(p) // h
right = max(p)

while left<=right:
	mid = (left + right) >> 1
	#如果速度mid用的时间大了，说明肯定是速度满了，加快速度。
	if sum([math.ceil(i / mid)  for i in p]) >h:
		left = mid+1
	#如果速度mid用的时间少了，就是速度太快，减慢速度
	elif sum([math.ceil(i / mid) for i in p]) <= h:
		right = mid-1
	#如果该速度所用时间相等，其实还有可能速度较少，尽量吃的更慢。

#该循环知道left=right时跳出循环
print(left)

