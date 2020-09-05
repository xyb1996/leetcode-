#暴力求解法

import sys
def fun(a, b):
	temp = {}
	i = 0
	j = 0
	start = -1
	end = -1
	while i < len(a):
		if a[i] == b[j]:
			j += 1
			if start == -1:
				start = i
				end = i
			else:
				end = i
			if j == len(b):
				if end - start in temp:
					if start < temp[end - start][0]:
						temp[end - start] = [start, end]
				else:
					temp[end - start] = [start, end]
				i = start
				start = -1
				j = 0
		i += 1
	if len(temp) > 0:
		ans = temp[min(temp.keys())]
	else:
		ans = (-1, -1)
	print(ans[0], ans[1])


lines = sys.stdin.readlines()
for i in range(len(lines)):
	a, b = lines[i].strip().split()
	fun(a, b)


