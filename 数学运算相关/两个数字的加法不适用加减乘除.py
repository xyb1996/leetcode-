def pluswithout(num1,num2):

	while True:
		sum = num1 ^num2
		#一定不要忘记这里的左移一位
		carry = (num1 & num2) <<1
		num1= sum
		num2 = carry
		if num2 ==0:
			break
	return num1

print(pluswithout(2,1))
