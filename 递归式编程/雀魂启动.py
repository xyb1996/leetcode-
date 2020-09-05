from collections import Counter

"""
问题描述：

1 1 1 2 2 2 6 6 6 7 7 7 9 9 可以组成1,2,6,7的4个刻子和9的雀头，可以和牌
1 1 1 1 2 2 3 3 5 6 7 7 8 9 用1做雀头，组123,123,567,789的四个顺子，可以和牌
1 1 1 2 2 2 3 3 3 5 6 7 7 9 无论用1 2 3 7哪个做雀头，都无法组成和牌的条件。

输入：输入只有一行，包含13个数字，用空格分隔，每个数字在1~9之间，数据保证同种数字最多出现4次。
输出：输出同样是一行，包含1个或以上的数字。代表他再取到哪些牌可以和牌。若满足条件的有多种牌，
请按从小到大的顺序输出。若没有满足条件的牌，请输出一个数字0

输出同样是一行，包含1个或以上的数字。代表他再取到哪些牌可以和牌。若满足条件的有多种牌，
请按从小到大的顺序输出。若没有满足条件的牌，请输出一个数字0
"""


#其实这也是动态规划的思想，就是大问题能不能用小问题来替代，只不过这是自顶向下的方式，
#动态规划是一种思想，递归知识这种的思想的实现形式。

def isHu(nums):
	"""
	判断是否可以胡牌
	:param nums:
	:return:
	"""
	#分析子问题时的递归终止条件
	if not nums:
		return True
	n = len(nums)
	count0 = nums.count(nums[0])
	# 没出现过雀头，且第一个数字出现的次数 >= 2,去掉雀头剩下的能不能和牌
	if n % 3 != 0 and count0 >= 2 and isHu(nums[2:]) == True:
		return True
	# 如果第一个数字出现次数 >= 3，去掉这个刻子后看剩下的能和牌
	if count0 >= 3 and isHu(nums[3:]) == True:
		return True
	# 如果存在顺子，移除顺子后剩下的能和牌
	if nums[0] + 1 in nums and nums[0] + 2 in nums:
		last_nums = nums.copy()
		last_nums.remove(nums[0])
		last_nums.remove(nums[0] + 1)
		last_nums.remove(nums[0] + 2)
		if isHu(last_nums) == True:
			return True
	# 以上条件都不满足，则不能和牌
	return False


def main(nums):
	"""
	遍历所有可以抓到的牌看能不能胡牌
	:return:
	"""
	d = {}
	for i in nums:
		d[i] = d.get(i, 0) + 1
	card_list = set(range(1, 10)) - {i for i, v in d.items() if v == 4}
	res = []
	for i in card_list:
		if isHu(sorted(nums + [i])):  # 如果这种抽牌方式可以和牌
			res.append(i)  # 加入和牌类型列表
	res = ' '.join(str(x) for x in sorted(res)) if res else '0'
	print(res)


s = input()
nums = [int(x) for x in s.split()]
main(nums)
