"""
思路：
（1）利用位数大的数字乘以位数小的数字，用位数小的数字每一位乘以大数，保存到一个数组中，
（2）写一个处理数组中进位的函数，如果元素值大于10，进位，特别注意的是最后一位要进位的话要append
（3）利用大数相加方法，将位数小的数字乘以大数的每一次中间计算结果相加，得到答案。
"""
#其他的感觉没有模拟大数相乘

class Solution(object):
	def multiply(self,num1,num2):
		if num1 =='0' or num2 =='0':
			return '0'
		l1 = len(num1)
		l2 = len(num2)
		if l2>l1:
			num1,num2 = num2,num1
			l1,l2 = l2,l1

		res = '0'
		#从低位开始×，从第二位开始需要加对应个数的'0'
		num2= num2[::-1]
		for idx,i in enumerate(num2):
			tmp1 = self.StringmultiplyDigit(num1,int(i))+idx*'0'
			res = self.StringplusString(res,tmp1)
		return res


	def StringmultiplyDigit(self,string,num):
		# 这个函数的功能是：计算一个字符串和一个整数的乘积，返回字符串
		# 举例：输入为 "123", 3， 返回"369"
		s = string[::-1]
		multi = [int(s[i])*int(num) for i in range(len(s))]
		#该函数用来处理进位
		res = self.solvecarry(multi)
		res = res[::-1]
		#逆置后输出
		return ''.join([str(i) for i in res])

	def solvecarry(self,nums):
		# 这个函数的功能是：将输入的数组中的每一位处理好进位
		# 举例：输入[15, 27, 12], 返回[5, 8, 4, 1]
		for idx,num in enumerate(nums):
			if  num>9:
				if idx < len(nums) -1:
					nums[idx+1] = nums[idx] //10+nums[idx+1]
				elif idx ==len(nums)-1:
					nums.append(nums[idx] //10)
				nums[idx] %= 10
		return nums

	def StringplusString(self,string1,string2):
		# 这个函数的功能是：计算两个字符串的和。
		# 举例：输入为“123”， “456”, 返回为"579"
		l1 = len(string1)
		l2 = len(string2)
		if l1 <l2:
			string1,string2 = string2,string1
			l1,l2 = l2,l1

		string1 = string1[::-1]
		string2 = string2[::-1]
		res = [int(i) for i in string1]

		for i in range(l2):
			res[i] = int(string1[i])+int(string2[i])

		res = self.solvecarry(res)[::-1]
		return ''.join([str(i) for i in res])

solution = Solution()
print(solution.multiply('123','456'))
