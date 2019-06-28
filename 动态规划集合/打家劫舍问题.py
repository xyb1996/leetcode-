class Solution:
    def rob(self, nums) -> int:

        max_sum = 0
        length = len(nums)
        if length == 0:
            return 0
        elif length ==1:
            return nums[0]
        else:
            #这里也可以用append，这样就不用用下表访问了
            dp =[0]*(length)

            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2,length):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            #return dp[-1]更简洁
            return dp[length-1]

solution = Solution()
print(solution.rob([2,1,1,2]))