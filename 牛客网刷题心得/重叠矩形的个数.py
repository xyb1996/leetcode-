#遍历所有可能的店就ok了。

import sys
lines = sys.stdin.readlines()
n = int(lines[0])
x1 = list(map(int,lines[1].split()))
y1 = list(map(int,lines[2].split()))
x2 = list(map(int,lines[3].split()))
y2 = list(map(int,lines[4].split()))
# 遍历所有点的组合（包含了矩形所有角以及交点），看一下有多少矩形包含它
res = 1
for x in x1+x2:
    for y in y1+y2:
        cnt = 0
        for i in range(n):
            if x > x1[i] and y > y1[i] and x <= x2[i] and y <= y2[i]:
                cnt += 1
        res = max(res,cnt)
print(res)


#下面是大佬的想法
import sys

lines = sys.stdin.readlines()
n = int(lines[0].strip())
xs1 = map(int, lines[1].strip().split())
ys1 = map(int, lines[2].strip().split())
xs2 = map(int, lines[3].strip().split())
ys2 = map(int, lines[4].strip().split())
nums = []
for x1, x2, y1, y2 in zip(xs1, xs2, ys1, ys2):
	nums.append((x1, 1, y1, y2))
	nums.append((x2, -1, y1, y2))
#排序完成后案x大小进行排序，如果flag是1，则是左下角，否则是右上角。
nums.sort()



temp, res = [], 1
for x, flag, y1, y2 in nums:
	#flag等于1说明它是左下角，并且还未出现一个flag =-1的右下角，加入temp中，准备数数重叠区域有多个
	# 通过这个if-else统计统计在（x1-x2）内出现的x
	if (flag == 1):
		temp.append((y1, 1))
		temp.append((y2, -1))
	else:
		count = 0
		#tmp中保存的元素均是x1，左下标的店，并且按照y坐标排列，如果tmp中连续出现 1和-1表示两个矩形不相交
		temp.sort()
		#y1是左下脚的高度，肯定小于y2，res就是记录
		for y, f in temp:
			count += f
			res = max(res, count)
#去掉第一个矩形的点，它的重叠部分已经统计完了。
		temp.remove((y1, 1))
		temp.remove((y2, -1))
print(res)
