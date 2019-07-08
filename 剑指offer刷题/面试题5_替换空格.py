"""
问题描述：
将一个字符串中所有的空格替换成%20
思路：
1、先遍历一遍该字符串，统计该字符串的空格数，计算出替换后的长度
2、用两个指针遍历字符串，一个指向该字符串末尾，一个指向替换后的末尾，遇到空格则替换
"""
def ReplaceBlank(string):
	length = len(string)
	if string==None or length ==0:
		return  -1
	count_blank = 0
	for i in string:
		if i ==' ':
			count_blank+=1
	length_expand = length+2*count_blank
	list_string = [string[i] if i < length else  ' '  for i in range(length_expand) ]
	p1 = length-1
	p2 = length_expand-1
	while p1>=0:
		if string[p1]!=' ':
			list_string[p2] = list_string[p1]
			p2-=1
			p1-=1
		else:
			list_string[p2] = '0'
			list_string[p2-1] = '2'
			list_string[p2-2] = '%'
			p2-=3
			p1-=1
	return ''.join(list_string)

print(ReplaceBlank('a'))