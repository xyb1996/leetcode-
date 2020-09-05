"""
题目描述：我们来做一个简单的密码破译游戏。破译的规则很简单，将数字转换为字母，1转化为a，2转化为b，依此类推，26转化为z。
现在输入的密码是一串数字，输出的破译结果是该数字串通过转换规则所能产生的所有字符串。

输入：
多行数据，每行为一个数字串。
保证数字串的总长度不超过1000，每行数据的答案至少有1个且不超过1000个。

输出：
多行数据，每行对应输出通过数字串破译得到的所有字符串，并按照字符串顺序排列，
字符串之间用单个空格分隔。每行开头和结尾不允许有多余的空格。

用递归的搜索法去变成的结果的字典序一定是最小的

注意点：本道题目的思路不是很难，主要是测试用例需要自己多想，比如37行 &39行的条件判断本来我没有考虑，结果就没有全部通过。

考试的时候需要自己多试试测试用例，特别是一些特殊点，比如这道题里面的字符'0'
"""








while True:
	try:
		dict1 = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',
				 18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
		num = [int(i) for i in input()]
		length = len(num)
		ans =[]
		def helper(start,tmp):
			if start >=length:
				ans.append(tmp[::])
				return

			if num[start]in dict1:
				helper(start+1,tmp+dict1[num[start]])
			if start+1<length and num[start]!=0 and 1<=num[start]*10+num[start+1]<=26:
				helper(start+2,tmp+dict1[num[start]*10+num[start+1]])
		helper(0,'')
		print(' '.join(ans))

	except:
		break





