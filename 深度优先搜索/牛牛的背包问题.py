"""
输入：输入包括两行
第一行为两个正整数n和w(1 <= n <= 30, 1 <= w <= 2 * 10^9),表示零食的数量和背包的容量。
第二行n个正整数v[i](0 <= v[i] <= 10^9),表示每袋零食的体积。

输出：输出一个正整数, 表示牛牛一共有多少种零食放法。
"""
#这种回溯法太暴力的，效率太低了,AC(80%)
n, w = list(map(int, input().split()))
volume = list(map(int, input().split()))
volume.sort(reverse=True)

count = 1
used = [False]*n

def backtrace(start,cur_sum):
	global count
	if cur_sum >w:
		count-=1
		return


	for i in range(start,n):
		if not used[i]:
			used[i] = True
			count += 1
			backtrace(i+1,cur_sum+volume[i])
			used[i] = False

backtrace(0,0)
print(count)



#采用下面这种递归的方式好像利用了更多的剪枝信息
#需要利用更多的剪枝，才能优化一定的效率
n, w = list(map(int, input().split()))
volume = list(map(int, input().split()))
volume.sort(reverse=True)

def countNum(w,volume):
	if w>0 and len(volume)>0:
		#如果容量够大，每一个零食都可以装或者不装
		if sum(volume) <= w:
			return 2**len(volume)
		else:
			#可以考虑装或者不装
			if w >= volume[0]:
				return countNum(w-volume[0],volume[1:])+countNum(w,volume[1:])
			else:
				#否则只能不装最大的那个，从后面的继续装找下第二大的数字进行尝试
				return countNum(w,volume[1:])
	else:
		return 1

print(countNum(w,volume))

