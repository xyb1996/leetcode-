#我的思路
class Solution:
	def exist(self, board, word: str):

		used={()}
		rows = len(board)
		cols = len(board[0])


		def backtrace(index,row,col):

			if index ==len(word):
				return True
#在这个for循环中递归调用backtrace，就代表下次调用的时候有几条路可以走。
			for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
				temp_x = row+x
				temp_y = col+y
				if 0<=temp_x<rows and 0<=temp_y<cols and (temp_x,temp_y) not in used and board[temp_x][temp_y] ==word[index]:
					used.add((temp_x, temp_y))
					if backtrace(index+1,temp_x,temp_y):
						return True

					used.remove((temp_x,temp_y))
			return False
#在外层等循环中，依次遍历每个点，注意每次遍历前，讲点加进去，遍历完后再恢复原本状态。
		for i in range(rows):
			for j in range(cols):
				used.add((i, j))
				if  board[i][j] == word[0] and  backtrace(1,i,j):

					return True
				used.remove((i,j))
		return False


#别人的思路
class Solution:
	def exist(self, board: List[List[str]], word: str) -> bool:
		row = len(board)
		col = len(board[0])

		def helper(i, j, k, visited):
			# print(i,j, k,visited)
			if k == len(word):
				return True
			for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
				tmp_i = x + i
				tmp_j = y + j
				if 0 <= tmp_i < row and 0 <= tmp_j < col and (tmp_i, tmp_j) not in visited \
						and board[tmp_i][tmp_j] == word[k]:
					visited.add((tmp_i, tmp_j))
					if helper(tmp_i, tmp_j, k + 1, visited):
						return True
					visited.remove((tmp_i, tmp_j))  # 回溯
			return False

		for i in range(row):
			for j in range(col):
				if board[i][j] == word[0] and helper(i, j, 1, {(i, j)}):
					return True
		return False



print(solution.exist([
	["a", "b"]]
	,"ba"
))
