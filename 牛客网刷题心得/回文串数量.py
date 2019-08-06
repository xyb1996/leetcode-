"""
问题描述：
输入一个字符串S 例如“aabcb”(1 <= |S| <= 50), |S|表示字符串S的长度。

符合条件的字符串有"a","a","aa","b","c","b","bcb"

所以答案:7

注意这道题目和分割回文串还有点不一样，这里是求回文串的数量，那么是求一种分割方案。
"""


#双重遍历
s = input()
count = 0
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        if s[i:j] == s[i:j][::-1]:
            count += 1
print(count)

#我的回溯法：
s= input().strip()
length = len(s)
count = 0
dict1 = {}
def backtrace(start,):
	global length
	global count
	if start >=length:
		return


	for end in range(start+1,length+1):
		substr = s[start:end]
		if substr == substr[::-1]:
			if '%d-%d'%(start,end) not in dict1:
				count += 1
				dict1['%d-%d'%(start,end)] = 1
			backtrace(end)
backtrace(0)
print(count)

#上面的两种方法都弱爆了,如果出现回文串的问题，最好想到这dP和动态规划这两种方案。
#可以考虑下面的动态规划方法或中心扩散法：


#dp[i][j]表示从s[i]到s[j]的字串是否是回文串
import sys

s = sys.stdin.readline().strip()

n = len(s)
dp = [[0] * n for i in range(n)]
num = 0

for i in range(n):
	for j in range(i, -1, -1):
		if s[j] == s[i] and (i - j <= 2 or dp[j + 1][i - 1] == 1):
			dp[j][i] = 1
			num += 1
print(num)



#也可以用中心扩散法：
ans = 0

def centerspread(s,i,j):
	while i>=0 and j<len(s):
		if s[i] ==s[j]:
			count+=1
			i-=1
			j+=1
		else:
			break

for i in range(len(s)):
	centerspread(s,i,i)
	centerspread(s,i,i+1)

print(ans)