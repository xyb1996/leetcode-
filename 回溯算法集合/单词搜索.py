class Solution:
	def exist(self, board, word: str):

		used={()}
		rows = len(board)
		cols = len(board[0])


		def backtrace(index,row,col):

			if index ==len(word):
				return True

			for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
				temp_x = row+x
				temp_y = col+y
				if 0<=temp_x<rows and 0<=temp_y<cols and (temp_x,temp_y) not in used and board[temp_x][temp_y] ==word[index]:
					used.add((temp_x, temp_y))
					if backtrace(index+1,temp_x,temp_y):
						return True

					used.remove((temp_x,temp_y))
			return False

		for i in range(rows):
			for j in range(cols):
				used.add((i, j))
				if  board[i][j] == word[0] and  backtrace(1,i,j):

					return True
				used.remove((i,j))
		return False

solution = Solution()
print(solution.exist([
	["a", "b"]]
	,"ba"
))
