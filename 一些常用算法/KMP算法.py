
#思路：
"""
kmp中有求next有下标从0开始的，也有从-1开始的，
如果从-1开始，那么求next的时候不用长度+1

还有就是求nextval数组，也就是next数组的进阶版的时候，如果next[j]的字符 和i的字符相同，那么nextval[i] = nextval[next[i]]
否则nextval[i] = next[i]
"""


def getNext(str1,next):

	next[0] = -1
	i,j = 0,-1

	while i < len(str1):
		if j == -1 or str1[i] == str1[j]:
			i+=1
			j+=1
			next[i] =j
		else:
			j = next[j]
	return

inputstr = 'abababca'
next = [0]*len(inputstr)

getNext(inputstr,next)

#t为主串，p是模式串
def kmp(t,p):
	i,j = 0,-1
	while i <len(t) and j <len(p):
		if j ==-1 or t[i] ==p[j]:
			i+=1
			j+=1
		else:
			j = next[j]
	if j ==len(p):
		return i-j
	else:
		return -1