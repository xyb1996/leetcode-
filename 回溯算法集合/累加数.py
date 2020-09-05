class Solution:
	def isAdditiveNumber(self, num: str) -> bool:
		def isinValidpat(string1):
			if len(string1) > 1 and string1[0] == '0':
				return True
			return False

		def backtrace(firstNum, secondNum, left):
			sum_string = str(int(firstNum) + int(secondNum))
			if sum_string == left:
				return True
			if len(sum_string) > len(left):
				return False
			# 如果长度还有剩余子串，返回子串是否为累加数，逐层向上返回
			if sum_string == left[:len(sum_string)]:
				return backtrace(secondNum, left[:len(sum_string)], left[len(sum_string):])

		if len(num) < 3:
			return False

		for i in range(1, len(num) + 1):
			for j in range(i + 1, len(num)):
				firstNum, secondNum, left = num[:i], num[i:j], num[j:]
				if isinValidpat(firstNum) or isinValidpat(secondNum):
					continue
				if backtrace(firstNum, secondNum, left):
					return True

		return False
