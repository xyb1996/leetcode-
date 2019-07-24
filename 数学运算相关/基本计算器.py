class Solution:
	def calculate(self, s: str) -> int:
		def cal(num1,num2,op):
			if op =='+':
				return num1+num2
			elif op =='-':
				return num1-num2
			elif op =='*':
				return num1*num2
			else:
				if num2 ==0:
					raise ValueError
				else:
					return num1 // num2
		priority = {'*':1,'/':1,'+':0,'-':0}
		stack_op = []
		stack_num = []
		s_new = s.strip()
		for idx,i in enumerate(s_new):
			if idx ==0:
				stack_num.append(int(i))
				continue
			if i.isspace():continue

			if i.isdigit() and   s_new[idx-1].isdigit() ==False:

				stack_num.append(int(i))
				continue
			if i.isdigit() and s_new[idx-1].isdigit():
				tmp = stack_num.pop()
				tmp = tmp*10+int(i)
				stack_num.append(tmp)
				continue

			else:
				if len(stack_op) ==0:
					stack_op.append(i)
				else:
					while len(stack_op)!=0 and priority[i]<=priority[stack_op[-1]]:
						k = stack_num.pop()
						j = stack_num.pop()
						op = stack_op.pop()
						stack_num.append(cal(j,k,op))

					stack_op.append(i)
		while len(stack_op) >0:
			k = stack_num.pop()
			j = stack_num.pop()
			op = stack_op.pop()
			stack_num.append(cal(j, k, op))
		return stack_num[-1]


solution = Solution()
print(solution.calculate("1*2-3/4+5*6-7*8+9/10"))