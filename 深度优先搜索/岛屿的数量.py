"""
描述:
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
11110
11010
11000
00000

输出: 1

输入:
11000
11000
00100
00011

输出: 3
"""

class Solution:

	def numIslands(self, grid):

		rows = len(grid)
		if rows ==0:
			return 0
		cols = len(grid[0])
		if rows ==0 and cols==0:
			return 0
		self.used= [[False for _ in range(cols) ] for j in range(rows) ]
		self.res = 0
		def helper(row,col,height=0):

			for x,y in  [(-1,0),(1,0),(0,1),(0,-1)]:
				temp_x,temp_y = row+x,col+y

				if 0<=temp_x<rows and 0<=temp_y<cols and int(grid[temp_x][temp_y]) ==1 and  not self.used[temp_x][temp_y] :

					self.used[temp_x][temp_y] = True

					helper(temp_x, temp_y, height + 1)


		for i in  range(rows):
			for j in range(cols):
				# self.used[i][j] =True
				if not self.used[i][j] and int(grid[i][j]) ==1:
					self.res+=1
					helper(i,j)
		return self.res

solution = Solution()
print(solution.numIslands(
[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))

