"""
题目描述：给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

输入: [2,1,5,6,2,3]
输出: 10
"""
#解法1、暴力遍历0(n^2)个区间，找到这么多个区间的最大值
#每个区间的最大值等于该区间长度乘以区间中的最小值。

def largestRectangleArea1(height):
	length  = len(height)
	maxarea = 0
	for i in range(length):
		minValue = float('inf')
		for j in range(i,length):

			minValue = min(minValue,height[j])
			maxarea = max(maxarea,minValue*(j-i+1))

	return maxarea


#解法二：分治法，首先找到该区间中的最小值，然后返回（1）区间最小值乘以区间长度（2）左子区间最小值（3）右子区间最小值的最大者

def largestRectangleArea2(height):
	if len(height) ==1:
		return height[0]
	minValue = min(height)
	min_idx =  height.index(minValue)
	ans = minValue*len(height)
	left = largestRectangleArea2(height[0:min_idx])
	right = largestRectangleArea2(height[min_idx+1:])
	return max(ans,left,right)


#解法三：该方法找到每个以heigh[i]为高的左边第一个小于height[i]的顶点和右边第一个小于height[i]的顶点，长度区间长度就=right-left-1
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        n = len(heights)
        left_i = [0] * n
        right_i = [0] * n
        left_i[0] = -1
        right_i[-1] = n
        for i in range(1, n):
            tmp = i - 1
            while tmp >= 0 and heights[tmp] >= heights[i]:
                tmp = left_i[tmp]
            left_i[i] = tmp
        for i in range(n - 2, -1, -1):
            tmp = i + 1
            while tmp < n and heights[tmp] >= heights[i]:
                tmp = right_i[tmp]
            right_i[i] = tmp
        # print(left_i)
        # print(right_i)
        res = 0
        for i in range(n):
            res = max(res, (right_i[i] - left_i[i] - 1) * heights[i])
        return res

#解法四：利用单调栈的方法
#如果height[i] >height[i-1]，则入栈，否则出栈，当前出栈元素为最高，那么他的第一个小于它的元素就是当前正在遍历的下标，
# 而左边第一个小于它的明显就是他的左边一个元素。
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        #就是在最左边和最右边都设置一个最小值
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            #print(stack)
			#如果栈顶元素大于当前正在遍历的元素，那么出栈进行一次计算
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
				#因为先出栈了，所以此时的stack[-1]就是当前栈顶元素左边的一个元素。
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res

