#对min到max范围内的每个可能值进行判断，二分法查找该能量值是否满足要求
#满足的话，那么往值小的空间查找，否则往值大的空间查找

"""
问题描述：机器人正在玩一个古老的基于DOS的游戏。游戏中有N+1座建筑——从0到N编号，从左到右排列。编号为0的建筑高度为0个单位，
编号为i的建筑的高度为H(i)个单位。

起初， 机器人在编号为0的建筑处。每一步，它跳到下一个（右边）建筑。假设机器人在第k个建筑，且它现在的能量值是E,
下一步它将跳到第个k+1建筑。它将会得到或者失去正比于与H(k+1)与E之差的能量。
如果 H(k+1) > E 那么机器人就失去 H(k+1) - E 的能量值，否则它将得到 E - H(k+1) 的能量值。

游戏目标是到达第个N建筑，在这个过程中，能量值不能为负数个单位。
现在的问题是机器人以多少能量值开始游戏，才可以保证成功完成游戏？
"""

n = int(input())
high = list(map(int, input().split()))

left, right = min(high), max(high)


def fun(power):
	for i in range(n):
		if power > high[i]:
			power += power - high[i]
		else:
			power -= high[i] - power
		if power < 0:
			return False
	return True


while left < right:
	mid = (left + right) >> 1

	#fun函数表示如果满足该要求，那么放回true，否则放回false
	if fun(mid):
		#如果为True,那么能量点还有可以下降的空间
		right = mid
	#否则初始能量点太低，必须得提高
	else:
		left = mid + 1

print(left)