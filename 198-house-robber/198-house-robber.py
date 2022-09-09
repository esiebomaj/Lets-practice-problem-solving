class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)+1)
        
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        print(dp)
        return dp[len(nums)-1]
        