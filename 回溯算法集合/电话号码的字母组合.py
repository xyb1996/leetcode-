class Solution(object):
	def letterCombinations(self,digits):
		num2letter=  {2:['a','b','c'],
                 3:['d','e','f'],
                 4:['g','h','i'],
                 5:['j','k','l'],
                 6:['m','n','o'],
                 7:['p','q','r','s'],
                 8:['t','u','v'],
                 9:['w','x','y','z']}
		res = []
		if len(digits) ==0:
			return []
		if len(digits) ==1:
			return num2letter[int(digits[0])]
		other = self.letterCombinations(digits[1:])
		for i in num2letter[int(digits[0])]:
			for j in other:
				res.append(i+j)
		return res
solution = Solution()
print(solution.letterCombinations('23'))


class Solution:
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		phone = {'2': ['a', 'b', 'c'],
				 '3': ['d', 'e', 'f'],
				 '4': ['g', 'h', 'i'],
				 '5': ['j', 'k', 'l'],
				 '6': ['m', 'n', 'o'],
				 '7': ['p', 'q', 'r', 's'],
				 '8': ['t', 'u', 'v'],
				 '9': ['w', 'x', 'y', 'z']}

		def backtrack(combination, next_digits):
			# if there is no more digits to check
			if len(next_digits) == 0:
				# the combination is done
				output.append(combination)
			# if there are still digits to check
			else:
				# iterate over all letters which map
				# the next available digit
				for letter in phone[next_digits[0]]:
					# append the current letter to the combination
					# and proceed to the next digits
					backtrack(combination + letter, next_digits[1:])

		output = []
		if digits:
			backtrack("", digits)
		return output




