class Solution:
	def isSubsequence(self, s: str, t: str) -> bool:
		length_s = len(s)
		length_t = len(t)
		count = 0
		i,j =0,0
		while i<length_s and j<length_t:
			if s[i] == t[j]:
				i+=1
				j+=1
				count+=1
			else:j+=1
		return count==length_s