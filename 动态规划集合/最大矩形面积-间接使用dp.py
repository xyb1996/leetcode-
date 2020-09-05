
#但是该方法居然通不过时间复杂度
class Solution:
	def maximalRectangle(self, matrix):
		m = len(matrix)
		if m == 0: return 0
		n = len(matrix[0])

		maxarea = 0
		#dp表示以i，j为右下角矩形的最大宽度
		dp = [ [0]*n for _ in range(m)]


		for i in range(0,m):
			for j in range(0,n):
				if int(matrix[i][j]) ==0:
					continue
				width = dp[i][j] = dp[i][j-1]+1 if j else 1

				#计算以i，j为右端顶点的矩形最大面积
				for k in range(i,-1,-1):
					width = min(width,dp[k][j])
					maxarea = max(maxarea,(i-k+1)*width)#计算前i层矩形的高，i-k+1是该矩形的高
		return maxarea



class Solution:

    # Get the maximum area in a histogram given its heights
    def leetcode84(self, heights):
        stack = [-1]

        maxarea = 0
        for i in range(len(heights)):

            #该循环结束后heights[i]肯定大于stack[-1]，所以后面先stack.append(i)
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                tmp = stack.pop()
                maxarea = max(maxarea, heights[tmp] * (i - stack[-1] - 1))
            stack.append(i)

        while stack[-1] != -1:
            maxarea = max(maxarea, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return maxarea


    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        if not matrix: return 0

        maxarea = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                # update the state of this row's histogram using the last row's histogram
                # by keeping track of the number of consecutive ones
				#注意这里的dp，是正对列上连续的1来统计的，然后计算柱状图中的最大矩形面积
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0

            # update maxarea with the maximum area from this row's histogram
            maxarea = max(maxarea, self.leetcode84(dp))
        return maxarea



#下面这个方法是真的秀，用三个方程更新求最大。
#这个矩形的计算公式是（r-l）*h,底边的边界为[l,r)

class Solution:

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [0] * n # initialize left as the leftmost boundary possible
        right = [n] * n # initialize right as the rightmost boundary possible
        height = [0] * n

        maxarea = 0

        for i in range(m):

            cur_left, cur_right = 0, n
            # update height
            for j in range(n):
				#高度的跟新比较直观，如果当前矩阵上数字为1，则为上一行高度+1，否则为0
                if matrix[i][j] == '1': height[j] += 1
                else: height[j] = 0
            # update left
            for j in range(n):
				#left[j]表示能从[i][j]这一点往左延伸的最大左边界，left[j]上一次更到达的最左边界，而cur_left是当前j能到达的
				#最左边界
                if matrix[i][j] == '1': left[j] = max(left[j], cur_left)
                #如果当前[i][j]数字为0，那么left[j]给它赋值为0，表示可以延伸到0，主要是赋值要比j+1小，然后将当前
				#左边界cur_left跟新为j+1，如果下次j+1的matrix[i][j]为1了，就被跟新成cur_left
                else:
                    left[j] = 0
                    cur_left = j + 1
            # update right
			#注意跟新right是从右往左跟新的，因为cur_right需要记录能够到达的最右边界，如果从左往右遍历那么下次需要访问的
			#cur_right的时候居然发现cur_right更小，这是不科学的，所以肯定要从右往左遍历。
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1': right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # update the area
            for j in range(n):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))

        return maxarea



