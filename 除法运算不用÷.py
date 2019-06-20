#除法不使用×÷，mod，那么肯定只能用加减法了。
class Solution:
	def divide(self, divd, dior):
		res = 0
		sign = 1 if divd ^dior >0 else -1
		divd = abs(divd)
		dior = abs(dior)

		while divd >=dior:
			#tmp用来表示当前除数，i用来代表tmp的倍数
			tmp,i = dior,1
			while divd >=tmp:
				#倍增除数
				divd -=tmp
				res+=i
				tmp <<=1
				i<<=1

		res = res *sign
		#这一行用来控制数字范围在-2**31-2**31）之间
		return min(max(res, -2 ** 31), 2 ** 31 - 1)

solution = Solution()
print(solution.divide(15,3))