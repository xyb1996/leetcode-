"""
问题描述：第一行 n, k (1 <= n, k <= 105) ，表示这堂课持续多少分钟，以及叫醒小易一次使他能够保持清醒的时间。
第二行 n 个数，a1, a2, ... , an(1 <= ai <= 104) 表示小易对每分钟知识点的感兴趣评分。
第三行 n 个数，t1, t2, ... , tn 表示每分钟小易是否清醒, 1表示清醒。

输出：小易这堂课听到的知识点的最大兴趣值。
"""

#如果采用暴力解法，AC率只有50

#采用一次遍历的方式求解即可通过，这种连续区间的问题，一般都可以这样做去掉区间最前面的一个数，加上后面一个新的树入区间，思想
#滑动窗口

n,k =list(map(int,input().split()))
a = list(map(int,input().split()))
t= list(map(int,input().split()))

maxsum =0
score = 0
cur_sum = 0

for i in range(n):
	if t[i] == 1:
		score+=a[i]
	else:
		cur_sum+=a[i]
	if i-k>=0:
		removeNum = a[i-k] if t[i-k] ==0 else 0
		cur_sum-=removeNum
	if cur_sum >maxsum:
		maxsum = cur_sum
print(score+maxsum)